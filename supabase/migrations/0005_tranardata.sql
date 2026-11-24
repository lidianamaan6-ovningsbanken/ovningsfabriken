-- Tränarens egna data: pass, matcher, favoriter och inställningar.
-- En rad per sak, så att två enheter kan ändra olika pass utan att skriva över varandra.
-- Säkerhet: varje inloggad tränare ser och ändrar bara sina egna rader (RLS).

create table if not exists public.coach_items (
  user_id    uuid not null default auth.uid() references auth.users(id) on delete cascade,
  kind       text not null check (kind in ('sess', 'match', 'mxteam', 'mxform', 'saved', 'settings')),
  item_id    text not null check (char_length(item_id) between 1 and 200),
  data       jsonb not null default '{}'::jsonb,
  deleted    boolean not null default false,
  updated_at timestamptz not null default now(),
  primary key (user_id, kind, item_id),
  constraint coach_items_size check (pg_column_size(data) < 400000)
);

create index if not exists coach_items_user_updated on public.coach_items (user_id, updated_at);

create or replace function public.coach_items_touch() returns trigger language plpgsql as $$
begin
  new.updated_at := now();
  return new;
end $$;

drop trigger if exists coach_items_touch on public.coach_items;
create trigger coach_items_touch before insert or update on public.coach_items
  for each row execute function public.coach_items_touch();

alter table public.coach_items enable row level security;

drop policy if exists "egna rader: läsa" on public.coach_items;
drop policy if exists "egna rader: skapa" on public.coach_items;
drop policy if exists "egna rader: ändra" on public.coach_items;
drop policy if exists "egna rader: ta bort" on public.coach_items;
create policy "egna rader: läsa"    on public.coach_items for select to authenticated using (user_id = auth.uid());
create policy "egna rader: skapa"   on public.coach_items for insert to authenticated with check (user_id = auth.uid());
create policy "egna rader: ändra"   on public.coach_items for update to authenticated using (user_id = auth.uid()) with check (user_id = auth.uid());
create policy "egna rader: ta bort" on public.coach_items for delete to authenticated using (user_id = auth.uid());

revoke all on public.coach_items from anon;
grant select, insert, update, delete on public.coach_items to authenticated;
