-- Klubbens profil (märke, färg, kortnamn) och vilka lag varje tränare har.
-- Märke och färg får visas innan inloggning (startbild och inbjudan) – de är inte hemliga.

alter table public.clubs
  add column if not exists slug text unique check (slug ~ '^[a-z0-9-]{2,30}$'),
  add column if not exists crest_url text,
  add column if not exists color text check (color ~ '^#[0-9a-fA-F]{6}$'),
  add column if not exists catalog_name text;   -- klubbens namn i lagkatalogen (lagkatalog.js)

alter table public.club_members
  add column if not exists teams text[] not null default '{}';

create or replace function public.club_brand_json(c clubs) returns jsonb language sql stable as $$
  select jsonb_build_object('id', c.id, 'name', c.name, 'slug', c.slug, 'crest', c.crest_url, 'color', c.color, 'catalog', c.catalog_name)
$$;

-- Innan inloggning: vilken klubb gäller inbjudan? (koden är lång och slumpad, så den går inte att gissa)
create or replace function public.invite_info(invite_token text) returns jsonb
language sql stable security definer set search_path = public as $$
  select coalesce((select club_brand_json(c) || jsonb_build_object('role', i.role, 'ok', true)
    from club_invites i join clubs c on c.id = i.club_id
    where i.token = invite_token and not i.revoked and i.used_by is null and i.expires_at > now()), jsonb_build_object('ok', false))
$$;

-- Innan inloggning: klubbens profil via kortnamn (för adresser som ?klubb=jfa)
create or replace function public.club_brand(club_slug text) returns jsonb
language sql stable security definer set search_path = public as $$
  select coalesce((select club_brand_json(c) from clubs c where c.slug = lower(club_slug)), 'null'::jsonb)
$$;

create or replace function public.my_access() returns jsonb language sql stable security definer set search_path = public as $$
  select jsonb_build_object(
    'admin', is_admin(),
    'clubs', coalesce((select jsonb_agg(club_brand_json(c) || jsonb_build_object(
        'role', m.role, 'teams', to_jsonb(m.teams),
        'seats', (club_license(c.id)).seats, 'valid_until', (club_license(c.id)).valid_until,
        'active', coalesce((club_license(c.id)).valid_until >= current_date, false),
        'used', club_used(c.id)) order by c.name)
      from club_members m join clubs c on c.id = m.club_id where m.user_id = auth.uid()), '[]'::jsonb))
$$;

create or replace function public.set_my_teams(cid uuid, team_ids text[]) returns void
language plpgsql security definer set search_path = public as $$
begin
  if club_role(cid) is null then raise exception 'Du är inte med i klubben'; end if;
  if coalesce(array_length(team_ids, 1), 0) > 8 then raise exception 'Högst 8 lag'; end if;
  update club_members set teams = coalesce(team_ids, '{}') where club_id = cid and user_id = auth.uid();
end $$;

create or replace function public.set_member_teams(cid uuid, member uuid, team_ids text[]) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not (is_admin() or club_role(cid) = 'owner') then raise exception 'Bara klubbens ansvariga kan ändra lag'; end if;
  if coalesce(array_length(team_ids, 1), 0) > 8 then raise exception 'Högst 8 lag'; end if;
  update club_members set teams = coalesce(team_ids, '{}') where club_id = cid and user_id = member;
end $$;

create or replace function public.admin_set_brand(cid uuid, club_name text, catalog text, club_slug text, crest text, club_color text) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not is_admin() then raise exception 'Bara admin'; end if;
  update clubs set name = coalesce(nullif(trim(club_name), ''), name), catalog_name = nullif(trim(catalog), ''),
    slug = nullif(lower(trim(club_slug)), ''), crest_url = nullif(trim(crest), ''), color = nullif(trim(club_color), '') where id = cid;
end $$;

revoke execute on function public.invite_info, public.club_brand from public;
grant execute on function public.invite_info, public.club_brand to anon, authenticated;
revoke execute on function public.set_my_teams, public.set_member_teams, public.admin_set_brand from anon, public;
grant execute on function public.set_my_teams, public.set_member_teams, public.admin_set_brand to authenticated;

-- Sams klubb blir Järfälla FA med JFA:s märke och färg
update public.clubs set name = 'Järfälla FA', catalog_name = 'Järfälla FA', slug = 'jfa',
  crest_url = 'assets/club-crests/jfa-stor.png', color = '#007a00'
where name = 'Övningsfabriken';
