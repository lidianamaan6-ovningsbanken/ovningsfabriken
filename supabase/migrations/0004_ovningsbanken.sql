-- Hela övningsbanken (1 450 övningar) flyttas in i exercises.
-- Teman = spelmoment (stage) i SvFF:s modell, grupperade per fas.

alter table public.categories add column if not exists phase text;

update public.categories set phase = 'Försvar' where slug = 'atererovring';
update public.categories set phase = 'Anfall', name = 'Avslut och mål' where slug = 'avslut';
insert into public.categories (slug, name, phase, sort_order) values
  ('speluppbyggnad',           'Speluppbyggnad',             'Anfall',            11),
  ('kontring',                 'Kontring',                   'Anfall',            13),
  ('forhindra-speluppbyggnad', 'Förhindra speluppbyggnad',   'Försvar',           21),
  ('forhindra-avslut',         'Förhindra och rädda avslut', 'Försvar',           22),
  ('omstallning-till-anfall',  'Omställning till anfall',    'Omställning',       31),
  ('omstallning-till-forsvar', 'Omställning till försvar',   'Omställning',       32),
  ('forberedelse',             'Förberedelse',               'Förberedelse',      41),
  ('skadeforebyggande',        'Skadeförebyggande',          'Skadeförebyggande', 42)
on conflict (slug) do update set name = excluded.name, phase = excluded.phase, sort_order = excluded.sort_order;
update public.categories set sort_order = 12 where slug = 'avslut';
update public.categories set sort_order = 23 where slug = 'atererovring';

alter table public.exercises
  add column if not exists old_id         text unique,
  add column if not exists phase          text,
  add column if not exists ex_type        text,
  add column if not exists level          text check (level in ('A','B','C')),
  add column if not exists organisation   text,
  add column if not exists rules          text,
  add column if not exists coaching_points text[] not null default '{}',
  add column if not exists easier         text,
  add column if not exists harder         text,
  add column if not exists game_sizes     int[] not null default '{}',   -- spelformer: 3, 5, 7, 9, 11
  add column if not exists source         text,                          -- egen, svff, extern
  add column if not exists source_url     text;

alter table public.exercises drop constraint if exists exercises_age_min_check;
alter table public.exercises add constraint exercises_age_min_check check (age_min between 3 and 21);

create or replace function public.stage_slug(stage text, phase text) returns text language sql immutable as $$
  select case stage
    when 'Speluppbyggnad' then 'speluppbyggnad'
    when 'Komma till avslut och göra mål' then 'avslut'
    when 'Kontring' then 'kontring'
    when 'Förhindra speluppbyggnad' then 'forhindra-speluppbyggnad'
    when 'Förhindra och rädda avslut' then 'forhindra-avslut'
    when 'Återerövring' then 'atererovring'
    when 'Omställning till anfall' then 'omstallning-till-anfall'
    when 'Omställning till försvar' then 'omstallning-till-forsvar'
    else case when phase = 'Skadeförebyggande' then 'skadeforebyggande' else 'forberedelse' end
  end
$$;

-- Koppla de fyra övningar som redan fanns till sina original
update public.exercises set old_id = 'b14' where slug = 'kontrapress-efter-bollforlust';
update public.exercises set old_id = 'b15' where slug = 'press-for-poang-i-tredjedelar';
update public.exercises set old_id = 't39' where slug = 'lang-passning-avlagg-avslut';
update public.exercises set old_id = 'b12' where slug = 'mottag-driv-och-avsluta';

-- Fyll på fält för alla (även de fyra ovan) från den gamla appen
with src as (
  select d.id, d.data as e from public.import_old_app d
)
insert into public.exercises (old_id, title, category_slug, phase, ex_type, level, setup, organisation, rules,
  coaching_points, easier, harder, players_min, players_max, age_min, game_sizes, source, source_url, published_at, is_public)
select e->>'id', left(e->>'name',120), public.stage_slug(e->>'stage', e->>'phase'), e->>'phase', nullif(e->>'type',''),
  nullif(e->>'level',''), nullif(e->>'orig',''),
  case when e->>'style'='svb' then null else nullif(e->>'org','') end,
  case when e->>'style'='svb' then null else nullif(e->>'rules','') end,
  coalesce(array(select jsonb_array_elements_text(e->'points')), '{}'),
  nullif(e->>'easier',''), nullif(e->>'harder',''),
  (e->>'min')::int, (e->>'max')::int, nullif(regexp_replace(e->>'ages','\D','','g'),'')::int,
  coalesce(array(select jsonb_array_elements_text(e->'sfx')::int), '{}'),
  case when e->>'style'='svb' then 'svff' when e->>'style'='mine' then 'egen' else 'extern' end,
  e->>'url', '2026-11-01', false
from src
on conflict (old_id) do update set
  phase = excluded.phase, ex_type = excluded.ex_type, level = excluded.level,
  setup = coalesce(public.exercises.setup, excluded.setup), organisation = excluded.organisation, rules = excluded.rules,
  coaching_points = excluded.coaching_points, easier = excluded.easier, harder = excluded.harder,
  players_min = excluded.players_min, players_max = excluded.players_max, age_min = excluded.age_min,
  game_sizes = excluded.game_sizes, source = excluded.source, source_url = excluded.source_url,
  published_at = coalesce(public.exercises.published_at, excluded.published_at);

-- Inloggade tränare ser alla publicerade övningar (licenskontroll läggs till i steg 2)
drop policy if exists "inloggade ser publicerade övningar" on public.exercises;
create policy "inloggade ser publicerade övningar" on public.exercises
  for select to authenticated using (published_at is not null and published_at <= now());

create index if not exists exercises_category_idx on public.exercises (category_slug);
create index if not exists exercises_title_trgm on public.exercises using gin (to_tsvector('swedish', title || ' ' || coalesce(setup,'')));
