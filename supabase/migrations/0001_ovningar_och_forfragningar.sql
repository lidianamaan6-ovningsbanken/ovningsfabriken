-- Övningsfabriken: första versionen av databasen.
-- Två delar: övningsbanken och förfrågningar från kontaktformuläret.

-- ===== Kategorier =====
create table public.categories (
  slug        text primary key,
  name        text not null,
  sort_order  int  not null default 0
);

-- ===== Övningar =====
create table public.exercises (
  id            uuid primary key default gen_random_uuid(),
  slug          text not null unique check (slug ~ '^[a-z0-9-]+$'),
  title         text not null check (char_length(title) between 3 and 120),
  category_slug text not null references public.categories(slug),
  summary       text check (char_length(summary) <= 400),
  description   text,
  setup         text,                         -- t.ex. "5 mot 2 i 8 × 8 m"
  players_min   int  check (players_min > 0),
  players_max   int  check (players_max >= players_min),
  age_min       int  check (age_min between 5 and 21),
  video_path    text,                         -- sökväg till videon
  poster_path   text,                         -- stillbild som visas innan videon spelas
  is_public     boolean not null default false, -- syns på startsidan utan inloggning
  published_at  timestamptz,                  -- null = utkast
  created_at    timestamptz not null default now(),
  updated_at    timestamptz not null default now()
);
create index exercises_published_idx on public.exercises (published_at desc) where published_at is not null;

create function public.touch_updated_at() returns trigger language plpgsql as $$
begin new.updated_at = now(); return new; end $$;
create trigger exercises_touch before update on public.exercises
  for each row execute function public.touch_updated_at();

-- ===== Förfrågningar från kontaktformuläret =====
create table public.leads (
  id            uuid primary key default gen_random_uuid(),
  created_at    timestamptz not null default now(),
  name          text not null check (char_length(name) between 1 and 120),
  club          text check (char_length(club) <= 160),
  email         text not null check (char_length(email) <= 254 and email ~* '^[^@\s]+@[^@\s]+\.[^@\s]+$'),
  coaches_count int  check (coaches_count between 1 and 500),
  interest      text not null check (interest in ('Tränarlicens','Klubblicens 5–6 tränare','Klubblicens 7 tränare','Licens för hela klubben','Annat')),
  message       text check (char_length(message) <= 2000),
  consent       boolean not null check (consent = true),
  status        text not null default 'ny' check (status in ('ny','kontaktad','kund','avslutad'))
);

-- ===== Säkerhet (Row Level Security) =====
alter table public.categories enable row level security;
alter table public.exercises  enable row level security;
alter table public.leads      enable row level security;

-- Alla får läsa kategorier.
create policy "kategorier är publika" on public.categories
  for select to anon, authenticated using (true);

-- Besökare utan inloggning ser bara publicerade övningar som är märkta som publika.
create policy "publika övningar syns för alla" on public.exercises
  for select to anon, authenticated
  using (is_public and published_at is not null and published_at <= now());

-- Besökare får skicka in en förfrågan, men aldrig läsa, ändra eller ta bort några.
create policy "vem som helst kan skicka förfrågan" on public.leads
  for insert to anon, authenticated
  with check (status = 'ny');

-- Rättigheter på tabellnivå (RLS-reglerna ovan begränsar sedan raderna).
revoke all on public.categories, public.exercises, public.leads from anon, authenticated;
grant select on public.categories, public.exercises to anon, authenticated;
grant insert (name, club, email, coaches_count, interest, message, consent) on public.leads to anon, authenticated;
