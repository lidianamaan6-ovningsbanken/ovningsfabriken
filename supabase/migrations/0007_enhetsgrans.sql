-- Enhetsgräns: ett konto får vara aktivt på högst N enheter (standard 2, t.ex. mobil + dator).
-- Stoppar att en tränare delar sitt lösenord med kollegor utanför licensen.
-- Loggar in man på en ny enhet när gränsen är nådd måste en annan enhet loggas ut.
-- Alla sådana byten loggas så att admin kan se konton som byter misstänkt ofta.

alter table public.licenses add column if not exists devices_per_user int not null default 2 check (devices_per_user between 1 and 10);

create table if not exists public.user_devices (
  user_id uuid not null references auth.users(id) on delete cascade,
  device_id text not null check (char_length(device_id) between 8 and 80),
  label text,
  first_seen timestamptz not null default now(),
  last_seen timestamptz not null default now(),
  primary key (user_id, device_id)
);
create table if not exists public.device_switches (
  id bigint generated always as identity primary key,
  user_id uuid not null references auth.users(id) on delete cascade,
  at timestamptz not null default now()
);
create index if not exists device_switches_user on public.device_switches (user_id, at);

alter table public.user_devices enable row level security;
alter table public.device_switches enable row level security;
drop policy if exists "enheter: egna" on public.user_devices;
create policy "enheter: egna" on public.user_devices for select to authenticated using (user_id = auth.uid());
revoke all on public.user_devices, public.device_switches from anon;
revoke insert, update, delete on public.user_devices, public.device_switches from authenticated;
grant select on public.user_devices to authenticated;

-- Högsta tillåtna antal enheter för den inloggade (bästa licensen bland klubbarna; admin 10)
create or replace function public.device_limit() returns int language sql stable security definer set search_path = public as $$
  select case when is_admin() then 10 else coalesce((
    select max((club_license(m.club_id)).devices_per_user) from club_members m where m.user_id = auth.uid()), 2) end
$$;

create or replace function public.register_device(dev text, dev_label text default null) returns jsonb
language plpgsql security definer set search_path = public as $$
declare lim int; n int;
begin
  if auth.uid() is null then raise exception 'Du måste vara inloggad'; end if;
  -- enheter som inte använts på 60 dagar räknas inte
  delete from user_devices where user_id = auth.uid() and last_seen < now() - interval '60 days';
  if exists (select 1 from user_devices where user_id = auth.uid() and device_id = dev) then
    update user_devices set last_seen = now(), label = coalesce(dev_label, label) where user_id = auth.uid() and device_id = dev;
    return jsonb_build_object('ok', true);
  end if;
  lim := device_limit();
  select count(*) into n from user_devices where user_id = auth.uid();
  if n < lim then
    insert into user_devices (user_id, device_id, label) values (auth.uid(), dev, dev_label);
    return jsonb_build_object('ok', true);
  end if;
  return jsonb_build_object('ok', false, 'limit', lim, 'devices',
    (select jsonb_agg(jsonb_build_object('id', device_id, 'label', label, 'last_seen', last_seen) order by last_seen) from user_devices where user_id = auth.uid()));
end $$;

-- Byt ut en enhet mot den här (loggar ut den andra)
create or replace function public.replace_device(dev text, dev_label text, remove_dev text) returns jsonb
language plpgsql security definer set search_path = public as $$
declare recent int;
begin
  if auth.uid() is null then raise exception 'Du måste vara inloggad'; end if;
  select count(*) into recent from device_switches where user_id = auth.uid() and at > now() - interval '24 hours';
  if recent >= 6 then raise exception 'För många enhetsbyten idag. Försök igen i morgon eller kontakta Övningsfabriken.'; end if;
  delete from user_devices where user_id = auth.uid() and device_id = remove_dev;
  insert into device_switches (user_id) values (auth.uid());
  return register_device(dev, dev_label);
end $$;

create or replace function public.forget_device(dev text) returns void
language sql security definer set search_path = public as $$
  delete from user_devices where user_id = auth.uid() and device_id = dev
$$;

-- Admin ser enhetsbyten per klubb (misstänkt delning)
create or replace function public.admin_clubs() returns jsonb language sql stable security definer set search_path = public as $$
  select case when not is_admin() then '[]'::jsonb else coalesce((select jsonb_agg(jsonb_build_object(
    'id', c.id, 'name', c.name, 'seats', (club_license(c.id)).seats, 'valid_until', (club_license(c.id)).valid_until,
    'devices', (club_license(c.id)).devices_per_user,
    'members', (select count(*) from club_members where club_id = c.id),
    'used', club_used(c.id),
    'switches30', (select count(*) from device_switches s join club_members m on m.user_id = s.user_id and m.club_id = c.id where s.at > now() - interval '30 days'),
    'owners', (select coalesce(jsonb_agg(email), '[]'::jsonb) from club_members where club_id = c.id and role = 'owner')) order by c.name)
    from clubs c), '[]'::jsonb) end
$$;

revoke execute on function public.device_limit, public.register_device, public.replace_device, public.forget_device from anon, public;
grant execute on function public.device_limit, public.register_device, public.replace_device, public.forget_device to authenticated;

create or replace function public.admin_set_devices(cid uuid, n int) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not is_admin() then raise exception 'Bara admin'; end if;
  update licenses set devices_per_user = n where id = (club_license(cid)).id;
end $$;
revoke execute on function public.admin_set_devices from anon, public;
grant execute on function public.admin_set_devices to authenticated;
