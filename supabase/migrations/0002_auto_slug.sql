-- Slug skapas automatiskt från titeln om fältet lämnas tomt.
-- "Mottag, driv och avsluta" -> "mottag-driv-och-avsluta". Å/Ä blir a, Ö blir o.
create or replace function public.make_slug(t text) returns text language sql immutable as $$
  select trim(both '-' from regexp_replace(
           translate(lower(t), 'åäöéèüàáíóú', 'aaoeeuaaiou'),
           '[^a-z0-9]+', '-', 'g'))
$$;

create or replace function public.exercises_fill_slug() returns trigger language plpgsql as $$
declare base text; candidate text; n int := 1;
begin
  if new.slug is null or btrim(new.slug) = '' then
    base := public.make_slug(new.title);
  else
    base := public.make_slug(new.slug);   -- rätta även en egenskriven slug
  end if;
  candidate := base;
  while exists (select 1 from public.exercises where slug = candidate and id <> new.id) loop
    n := n + 1; candidate := base || '-' || n;
  end loop;
  new.slug := candidate;
  return new;
end $$;

create trigger exercises_fill_slug before insert or update of slug, title on public.exercises
  for each row execute function public.exercises_fill_slug();

alter table public.exercises alter column slug drop not null;
