-- Antal publicerade övningar per tema, för startsidan.
-- Räknar ALLA publicerade övningar (även de som bara syns i appen),
-- men lämnar bara ut siffror, aldrig själva övningarna.
create or replace function public.exercise_stats()
returns table (slug text, name text, count bigint)
language sql stable security definer set search_path = public as $$
  select c.slug, c.name, count(e.id)
  from public.categories c
  left join public.exercises e
    on e.category_slug = c.slug
   and e.published_at is not null
   and e.published_at <= now()
  group by c.slug, c.name, c.sort_order
  order by count(e.id) desc, c.sort_order
$$;
revoke all on function public.exercise_stats() from public;
grant execute on function public.exercise_stats() to anon, authenticated;
