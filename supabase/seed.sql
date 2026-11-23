-- Startdata: kategorier och de övningar som har video i dag.
insert into public.categories (slug, name, sort_order) values
  ('atererovring', 'Återerövring', 10),
  ('avslut',       'Avslut och mål', 20)
on conflict (slug) do nothing;

insert into public.exercises (slug, title, category_slug, summary, setup, players_min, players_max, age_min, video_path, poster_path, is_public, published_at) values
  ('kontrapress-efter-bollforlust', 'Kontrapress efter bollförlust', 'atererovring',
   'Blått håller bollen i 5 mot 2. Tappar de den gäller det att reagera direkt: närmaste pressar, nästa stänger passningsvägen.',
   '5 mot 2 i 8 × 8 m', 7, null, null, 'video/kontrapress.mp4', 'video/kontrapress.jpg', true, '2026-11-18'),
  ('press-for-poang-i-tredjedelar', 'Press för poäng i tredjedelar', 'atererovring',
   'Planen delas i tre zoner. En bollvinst högt upp ger 3 poäng, i mitten 2 och i egen tredjedel 1. Laget lär sig pressa tidigt.',
   'Tre zoner, poäng per zon', null, null, null, 'video/press-tredjedelar.mp4', 'video/press-tredjedelar.jpg', true, '2026-11-16'),
  ('lang-passning-avlagg-avslut', 'Lång passning, avlägg och avslut', 'avslut',
   'Lång passning, avlägg, diagonal löpning och avslut. Stationerna roterar efter varje aktion så att alla får många avslut.',
   'Stationer runt straffområdet', null, null, null, 'video/avslut-bayern.mp4', 'video/avslut-bayern.jpg', true, '2026-11-14'),
  ('mottag-driv-och-avsluta', 'Mottag, driv och avsluta i tre stationer', 'avslut',
   'Mottagaren börjar med ryggen mot mål, vänder, driver och avslutar.',
   'Tre stationer', 4, 15, 9, null, null, false, null)
on conflict (slug) do nothing;
