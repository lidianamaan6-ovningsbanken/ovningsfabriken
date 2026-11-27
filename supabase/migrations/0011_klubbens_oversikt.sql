-- Klubbens översikt för ansvariga och admin: hur aktiva tränarna är och om de följer
-- spelarutbildningsplanen. Bara SIFFROR per tränare – aldrig innehållet i pass, matcher eller anteckningar.

-- 1) Aktiva dagar: en rad per tränare och dag när appen öppnas
create table if not exists public.app_opens (
  user_id uuid not null references auth.users(id) on delete cascade default auth.uid(),
  day date not null default current_date,
  primary key (user_id, day)
);
alter table public.app_opens enable row level security;
revoke all on public.app_opens from anon, authenticated;

create or replace function public.log_open() returns void
language sql security definer set search_path = public as $$
  insert into app_opens (user_id, day) select auth.uid(), current_date where auth.uid() is not null
  on conflict do nothing;
$$;
revoke all on function public.log_open() from public, anon;
grant execute on function public.log_open() to authenticated;

-- 2) Översikten: en rad per tränare i klubben
create or replace function public.club_usage(cid uuid) returns jsonb
language plpgsql stable security definer set search_path = public as $$
begin
  if auth.uid() is null or not (is_admin() or club_role(cid) = 'owner') then raise exception 'Bara klubbens ansvariga kan se översikten'; end if;
  return coalesce((
    select jsonb_agg(row_to_json(x) order by x.active_30 desc, x.email) from (
      select m.user_id, u.email, m.role, m.joined_at,
        (select count(*) from app_opens o where o.user_id = m.user_id and o.day > current_date - 30) as active_30,
        (select count(*) from app_opens o where o.user_id = m.user_id) as active_total,
        (select max(d.last_seen) from user_devices d where d.user_id = m.user_id) as last_seen,
        (select count(*) from coach_items c where c.user_id = m.user_id and c.kind = 'sess' and not c.deleted and not coalesce((c.data->>'removed')::boolean, false)) as pass_total,
        (select count(*) from coach_items c where c.user_id = m.user_id and c.kind = 'sess' and not c.deleted and not coalesce((c.data->>'removed')::boolean, false) and c.updated_at > now() - interval '30 days') as pass_30,
        (select count(*) from coach_items c where c.user_id = m.user_id and c.kind = 'sess' and not c.deleted and (c.data ? 'completedAt' or c.data->'refl'->>'done' = 'true')) as pass_done,
        (select count(*) from coach_items c where c.user_id = m.user_id and c.kind = 'sess' and not c.deleted and coalesce(c.data->>'periodId', '') <> '') as pass_season,
        (select count(*) from coach_items c where c.user_id = m.user_id and c.kind = 'match' and not c.deleted and not coalesce((c.data->>'removed')::boolean, false)) as matches,
        (select count(*) from coach_items c where c.user_id = m.user_id and c.kind = 'saved' and not c.deleted and c.data->>'own' = 'true' and not coalesce((c.data->>'removed')::boolean, false)) as own_exercises,
        (select coalesce(jsonb_array_length(c.data->'season'->'periods'), 0) from coach_items c where c.user_id = m.user_id and c.kind = 'settings' limit 1) as season_periods,
        (select count(*) from coach_items c, jsonb_array_elements(case when jsonb_typeof(c.data->'season'->'periods') = 'array' then c.data->'season'->'periods' else '[]'::jsonb end) p where c.user_id = m.user_id and c.kind = 'settings' and p ? 'lp') as lp_periods,
        (select coalesce(jsonb_array_length(c.data->'idea'->'principles'), 0) from coach_items c where c.user_id = m.user_id and c.kind = 'settings' limit 1) as idea_principles
      from club_members m join auth.users u on u.id = m.user_id
      where m.club_id = cid
    ) x), '[]'::jsonb);
end $$;
revoke all on function public.club_usage(uuid) from public, anon;
grant execute on function public.club_usage(uuid) to authenticated;
