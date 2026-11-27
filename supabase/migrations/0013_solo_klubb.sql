-- Solo-klubb: egen licens för en enskild tränare som inte hör till någon klubb med licens.
-- En solo-klubb är en vanlig klubb i databasen men med kind = 'solo':
--   * alltid exakt 1 plats (tränaren själv), inga inbjudningar av kollegor
--   * inget märke, ingen lagkatalog och inget klubbmaterial (t.ex. JFA:s läroplan)
--   * tränaren lägger själv upp sitt lag (namn, kön och födelseår) i own_teams
-- Licenskontroll, skyddad lagring, enhetsgräns och molnsynk fungerar precis som för klubbar.

alter table public.clubs
  add column if not exists kind text not null default 'club' check (kind in ('club', 'solo')),
  add column if not exists home_club text check (char_length(home_club) <= 120);   -- klubben tränaren säger att hen tränar i (bara text)

alter table public.club_members
  add column if not exists own_teams jsonb not null default '[]'::jsonb;           -- solo: [{id, name, g, y}]

create or replace function public.is_solo(cid uuid) returns boolean language sql stable security definer set search_path = public as $$
  select coalesce((select kind = 'solo' from clubs where id = cid), false)
$$;

-- Vad har jag tillgång till? (nu med kind, home_club och own_teams)
create or replace function public.my_access() returns jsonb language sql stable security definer set search_path = public as $$
  select jsonb_build_object(
    'admin', is_admin(),
    'clubs', coalesce((select jsonb_agg(club_brand_json(c) || jsonb_build_object(
        'kind', c.kind, 'home_club', c.home_club,
        'role', m.role, 'teams', to_jsonb(m.teams), 'own_teams', m.own_teams,
        'seats', (club_license(c.id)).seats, 'valid_until', (club_license(c.id)).valid_until,
        'active', coalesce((club_license(c.id)).valid_until >= current_date, false),
        'used', club_used(c.id)) order by c.name)
      from club_members m join clubs c on c.id = m.club_id where m.user_id = auth.uid()), '[]'::jsonb))
$$;

-- Inbjudningar: en egen licens gäller bara tränaren själv
create or replace function public.create_invite(cid uuid, invite_label text default null) returns text
language plpgsql security definer set search_path = public as $$
declare lic licenses; t text;
begin
  if auth.uid() is null then raise exception 'Du måste vara inloggad'; end if;
  if is_solo(cid) then raise exception 'En egen licens gäller bara dig. Vill ni vara fler tränare behöver klubben en klubblicens.'; end if;
  if not (is_admin() or club_role(cid) = 'owner') then raise exception 'Bara klubbens ansvariga kan bjuda in'; end if;
  lic := club_license(cid);
  if lic.id is null or lic.valid_until < current_date then raise exception 'Klubbens licens är inte aktiv'; end if;
  if club_used(cid) >= lic.seats then raise exception 'Alla % platser är använda', lic.seats; end if;
  insert into club_invites (club_id, role, label) values (cid, 'coach', nullif(trim(invite_label), '')) returning token into t;
  return t;
end $$;

-- Lag och profil kan inte sättas om till klubb-katalog på en solo-klubb
create or replace function public.admin_set_brand(cid uuid, club_name text, catalog text, club_slug text, crest text, club_color text) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not is_admin() then raise exception 'Bara admin'; end if;
  if is_solo(cid) then raise exception 'En egen licens har ingen klubbprofil'; end if;
  update clubs set name = coalesce(nullif(trim(club_name), ''), name), catalog_name = nullif(trim(catalog), ''),
    slug = nullif(lower(trim(club_slug)), ''), crest_url = nullif(trim(crest), ''), color = nullif(trim(club_color), '') where id = cid;
end $$;

create or replace function public.admin_set_license(cid uuid, seat_count int, valid date) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not is_admin() then raise exception 'Bara admin'; end if;
  update licenses set seats = case when is_solo(cid) then 1 else seat_count end, valid_until = valid where id = (club_license(cid)).id;
end $$;

-- Admin: skapa en egen licens och få en länk att skicka till tränaren
create or replace function public.admin_create_solo(coach_label text, coach_club text, valid date) returns jsonb
language plpgsql security definer set search_path = public as $$
declare cid uuid; t text; lbl text := nullif(trim(coach_label), ''); hc text := nullif(trim(coach_club), '');
begin
  if not is_admin() then raise exception 'Bara admin'; end if;
  if lbl is null then raise exception 'Skriv tränarens namn eller e-post'; end if;
  insert into clubs (name, kind, home_club) values (left('Egen licens · ' || lbl, 120), 'solo', left(hc, 120)) returning id into cid;
  insert into licenses (club_id, seats, valid_until, note) values (cid, 1, valid, 'Egen licens');
  insert into club_invites (club_id, role, label, expires_at) values (cid, 'owner', left(lbl, 80), now() + interval '60 days') returning token into t;
  return jsonb_build_object('club_id', cid, 'token', t);
end $$;

-- Tränaren med egen licens lägger upp sitt lag (och vilken klubb hen tränar i)
create or replace function public.set_my_own_team(cid uuid, team_name text, team_group text, birth_year int, coach_club text) returns jsonb
language plpgsql security definer set search_path = public as $$
declare nm text := nullif(trim(team_name), ''); grp text := coalesce(nullif(trim(team_group), ''), 'Mixat'); hc text := nullif(trim(coach_club), ''); t jsonb;
begin
  if auth.uid() is null then raise exception 'Du måste vara inloggad'; end if;
  if not is_solo(cid) or club_role(cid) is null then raise exception 'Gäller bara egen licens'; end if;
  if nm is null or char_length(nm) > 60 then raise exception 'Skriv lagets namn (högst 60 tecken)'; end if;
  if grp not in ('Pojkar', 'Flickor', 'Mixat', 'Herr', 'Dam') then raise exception 'Okänd lagtyp'; end if;
  if birth_year is not null and (birth_year < 1950 or birth_year > extract(year from current_date)::int - 4) then raise exception 'Kontrollera födelseåret'; end if;
  if hc is not null and char_length(hc) > 120 then raise exception 'Klubbens namn är för långt'; end if;
  t := jsonb_build_object('id', 'egen-1', 'name', nm, 'g', grp, 'y', birth_year);
  update club_members set own_teams = jsonb_build_array(t), teams = array['egen-1'] where club_id = cid and user_id = auth.uid();
  update clubs set home_club = hc where id = cid;
  return t;
end $$;

-- Admin-listan visar vilka som är egna licenser
create or replace function public.admin_clubs() returns jsonb language sql stable security definer set search_path = public as $$
  select case when not is_admin() then '[]'::jsonb else coalesce((select jsonb_agg(jsonb_build_object(
    'id', c.id, 'name', c.name, 'kind', c.kind, 'home_club', c.home_club,
    'seats', (club_license(c.id)).seats, 'valid_until', (club_license(c.id)).valid_until,
    'devices', (club_license(c.id)).devices_per_user,
    'members', (select count(*) from club_members where club_id = c.id),
    'used', club_used(c.id),
    'switches30', (select count(*) from device_switches s join club_members m on m.user_id = s.user_id and m.club_id = c.id where s.at > now() - interval '30 days'),
    'owners', (select coalesce(jsonb_agg(email), '[]'::jsonb) from club_members where club_id = c.id and role = 'owner')) order by c.kind, c.name)
    from clubs c), '[]'::jsonb) end
$$;

-- Innan inloggning: inbjudan till en egen licens visas som det (inte som en klubb)
create or replace function public.invite_info(invite_token text) returns jsonb
language sql stable security definer set search_path = public as $$
  select coalesce((select club_brand_json(c) || jsonb_build_object('role', i.role, 'ok', true, 'kind', c.kind)
    from club_invites i join clubs c on c.id = i.club_id
    where i.token = invite_token and not i.revoked and i.used_by is null and i.expires_at > now()), jsonb_build_object('ok', false))
$$;

revoke execute on function public.is_solo, public.admin_create_solo, public.set_my_own_team from public, anon;
grant execute on function public.is_solo, public.admin_create_solo, public.set_my_own_team to authenticated;
