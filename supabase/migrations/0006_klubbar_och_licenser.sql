-- Klubbar, licenser, medlemmar och inbjudningar.
-- Alla ändringar görs via funktionerna längre ner, som kontrollerar behörighet och antal platser.
-- Tabellerna går bara att läsa direkt, och bara för den som hör till klubben (eller är admin).

create table if not exists public.app_admins (
  user_id uuid primary key references auth.users(id) on delete cascade,
  created_at timestamptz not null default now()
);

create table if not exists public.clubs (
  id uuid primary key default gen_random_uuid(),
  name text not null check (char_length(name) between 2 and 120),
  created_at timestamptz not null default now(),
  created_by uuid default auth.uid()
);

create table if not exists public.licenses (
  id uuid primary key default gen_random_uuid(),
  club_id uuid not null references public.clubs(id) on delete cascade,
  seats int not null default 6 check (seats between 1 and 500),
  valid_until date not null,
  note text,
  created_at timestamptz not null default now()
);
create index if not exists licenses_club on public.licenses (club_id);

create table if not exists public.club_members (
  club_id uuid not null references public.clubs(id) on delete cascade,
  user_id uuid not null references auth.users(id) on delete cascade,
  role text not null default 'coach' check (role in ('owner', 'coach')),
  email text,
  joined_at timestamptz not null default now(),
  primary key (club_id, user_id)
);
create index if not exists club_members_user on public.club_members (user_id);

create table if not exists public.club_invites (
  token text primary key default (replace(gen_random_uuid()::text, '-', '') || replace(gen_random_uuid()::text, '-', '')),
  club_id uuid not null references public.clubs(id) on delete cascade,
  role text not null default 'coach' check (role in ('owner', 'coach')),
  label text,
  created_by uuid default auth.uid(),
  created_at timestamptz not null default now(),
  expires_at timestamptz not null default now() + interval '30 days',
  used_by uuid references auth.users(id) on delete set null,
  used_at timestamptz,
  revoked boolean not null default false
);
create index if not exists club_invites_club on public.club_invites (club_id);

-- Hjälpfunktioner (security definer så att säkerhetsreglerna inte loopar)
create or replace function public.is_admin() returns boolean language sql stable security definer set search_path = public as $$
  select exists (select 1 from app_admins where user_id = auth.uid())
$$;
create or replace function public.club_role(cid uuid) returns text language sql stable security definer set search_path = public as $$
  select role from club_members where club_id = cid and user_id = auth.uid()
$$;
create or replace function public.club_license(cid uuid) returns licenses language sql stable security definer set search_path = public as $$
  select * from licenses where club_id = cid order by valid_until desc limit 1
$$;
create or replace function public.club_used(cid uuid) returns int language sql stable security definer set search_path = public as $$
  select (select count(*) from club_members where club_id = cid)::int
       + (select count(*) from club_invites where club_id = cid and used_by is null and not revoked and expires_at > now())::int
$$;

alter table public.app_admins enable row level security;
alter table public.clubs enable row level security;
alter table public.licenses enable row level security;
alter table public.club_members enable row level security;
alter table public.club_invites enable row level security;

drop policy if exists "admin: se sig själv" on public.app_admins;
create policy "admin: se sig själv" on public.app_admins for select to authenticated using (user_id = auth.uid());
drop policy if exists "klubb: medlemmar läser" on public.clubs;
create policy "klubb: medlemmar läser" on public.clubs for select to authenticated using (is_admin() or club_role(id) is not null);
drop policy if exists "licens: medlemmar läser" on public.licenses;
create policy "licens: medlemmar läser" on public.licenses for select to authenticated using (is_admin() or club_role(club_id) is not null);
drop policy if exists "medlemmar: kollegor läser" on public.club_members;
create policy "medlemmar: kollegor läser" on public.club_members for select to authenticated using (is_admin() or club_role(club_id) is not null);
drop policy if exists "inbjudan: ägare läser" on public.club_invites;
create policy "inbjudan: ägare läser" on public.club_invites for select to authenticated using (is_admin() or club_role(club_id) = 'owner');

revoke all on public.app_admins, public.clubs, public.licenses, public.club_members, public.club_invites from anon;
revoke insert, update, delete on public.app_admins, public.clubs, public.licenses, public.club_members, public.club_invites from authenticated;
grant select on public.app_admins, public.clubs, public.licenses, public.club_members, public.club_invites to authenticated;

-- Vad har jag tillgång till?
create or replace function public.my_access() returns jsonb language sql stable security definer set search_path = public as $$
  select jsonb_build_object(
    'admin', is_admin(),
    'clubs', coalesce((select jsonb_agg(jsonb_build_object(
        'id', c.id, 'name', c.name, 'role', m.role,
        'seats', (club_license(c.id)).seats, 'valid_until', (club_license(c.id)).valid_until,
        'active', coalesce((club_license(c.id)).valid_until >= current_date, false),
        'used', club_used(c.id)) order by c.name)
      from club_members m join clubs c on c.id = m.club_id where m.user_id = auth.uid()), '[]'::jsonb))
$$;

-- Ägare (eller admin) skapar en inbjudningslänk till en kollega
create or replace function public.create_invite(cid uuid, invite_label text default null) returns text
language plpgsql security definer set search_path = public as $$
declare lic licenses; t text;
begin
  if auth.uid() is null then raise exception 'Du måste vara inloggad'; end if;
  if not (is_admin() or club_role(cid) = 'owner') then raise exception 'Bara klubbens ansvariga kan bjuda in'; end if;
  lic := club_license(cid);
  if lic.id is null or lic.valid_until < current_date then raise exception 'Klubbens licens är inte aktiv'; end if;
  if club_used(cid) >= lic.seats then raise exception 'Alla % platser är använda', lic.seats; end if;
  insert into club_invites (club_id, role, label) values (cid, 'coach', nullif(trim(invite_label), '')) returning token into t;
  return t;
end $$;

create or replace function public.revoke_invite(invite_token text) returns void
language plpgsql security definer set search_path = public as $$
declare cid uuid;
begin
  select club_id into cid from club_invites where token = invite_token;
  if cid is null then raise exception 'Inbjudan finns inte'; end if;
  if not (is_admin() or club_role(cid) = 'owner') then raise exception 'Inte behörig'; end if;
  update club_invites set revoked = true where token = invite_token and used_by is null;
end $$;

-- Den inbjudna tar emot inbjudan efter att ha skapat konto / loggat in
create or replace function public.accept_invite(invite_token text) returns jsonb
language plpgsql security definer set search_path = public as $$
declare inv club_invites; lic licenses; members int; cname text;
begin
  if auth.uid() is null then raise exception 'Du måste vara inloggad'; end if;
  select * into inv from club_invites where token = invite_token for update;
  if inv.token is null or inv.revoked then raise exception 'Inbjudan gäller inte längre'; end if;
  select name into cname from clubs where id = inv.club_id;
  if exists (select 1 from club_members where club_id = inv.club_id and user_id = auth.uid()) then
    return jsonb_build_object('club', cname, 'already', true);
  end if;
  if inv.used_by is not null then raise exception 'Inbjudan är redan använd'; end if;
  if inv.expires_at < now() then raise exception 'Inbjudan har gått ut'; end if;
  lic := club_license(inv.club_id);
  if lic.id is null or lic.valid_until < current_date then raise exception 'Klubbens licens är inte aktiv'; end if;
  select count(*) into members from club_members where club_id = inv.club_id;
  if members >= lic.seats then raise exception 'Klubbens platser är slut'; end if;
  insert into club_members (club_id, user_id, role, email) values (inv.club_id, auth.uid(), inv.role, auth.jwt() ->> 'email');
  update club_invites set used_by = auth.uid(), used_at = now() where token = invite_token;
  return jsonb_build_object('club', cname, 'role', inv.role);
end $$;

-- Ägare tar bort en kollega (frigör platsen)
create or replace function public.remove_member(cid uuid, member uuid) returns void
language plpgsql security definer set search_path = public as $$
declare r text;
begin
  select role into r from club_members where club_id = cid and user_id = member;
  if r is null then return; end if;
  if not (is_admin() or (club_role(cid) = 'owner' and r <> 'owner')) then raise exception 'Inte behörig'; end if;
  delete from club_members where club_id = cid and user_id = member;
end $$;

-- Admin: skapa klubb med licens och ägarlänk
create or replace function public.admin_create_club(club_name text, seat_count int, valid date) returns jsonb
language plpgsql security definer set search_path = public as $$
declare cid uuid; t text;
begin
  if not is_admin() then raise exception 'Bara admin'; end if;
  insert into clubs (name) values (trim(club_name)) returning id into cid;
  insert into licenses (club_id, seats, valid_until) values (cid, seat_count, valid);
  insert into club_invites (club_id, role, label, expires_at) values (cid, 'owner', 'Ägare', now() + interval '60 days') returning token into t;
  return jsonb_build_object('club_id', cid, 'token', t);
end $$;

create or replace function public.admin_owner_link(cid uuid) returns text
language plpgsql security definer set search_path = public as $$
declare t text;
begin
  if not is_admin() then raise exception 'Bara admin'; end if;
  insert into club_invites (club_id, role, label, expires_at) values (cid, 'owner', 'Ägare', now() + interval '60 days') returning token into t;
  return t;
end $$;

create or replace function public.admin_set_license(cid uuid, seat_count int, valid date) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not is_admin() then raise exception 'Bara admin'; end if;
  update licenses set seats = seat_count, valid_until = valid where id = (club_license(cid)).id;
end $$;

create or replace function public.admin_clubs() returns jsonb language sql stable security definer set search_path = public as $$
  select case when not is_admin() then '[]'::jsonb else coalesce((select jsonb_agg(jsonb_build_object(
    'id', c.id, 'name', c.name, 'seats', (club_license(c.id)).seats, 'valid_until', (club_license(c.id)).valid_until,
    'members', (select count(*) from club_members where club_id = c.id),
    'used', club_used(c.id),
    'owners', (select coalesce(jsonb_agg(email), '[]'::jsonb) from club_members where club_id = c.id and role = 'owner')) order by c.name)
    from clubs c), '[]'::jsonb) end
$$;

revoke execute on function public.my_access, public.create_invite, public.revoke_invite, public.accept_invite, public.remove_member,
  public.admin_create_club, public.admin_owner_link, public.admin_set_license, public.admin_clubs from anon, public;
grant execute on function public.my_access, public.create_invite, public.revoke_invite, public.accept_invite, public.remove_member,
  public.admin_create_club, public.admin_owner_link, public.admin_set_license, public.admin_clubs to authenticated;
