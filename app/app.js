// Övningsfabriken – appen (steg 1: inloggning, skal och övningsbank)
// Backend: Supabase (Postgres + inloggning). Ingen byggprocess, vanliga ES-moduler.

const SUPABASE_URL = 'https://fwgvfmkdmrpmgririxpt.supabase.co';
const SUPABASE_KEY = 'sb_publishable_Gi3qXYCia2WPxGIXcT8spQ_0ck6NMiT'; // publik nyckel, skyddas av RLS

const sb = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY, {
  auth: { flowType: 'implicit', persistSession: true, detectSessionInUrl: true, autoRefreshToken: true },
});

const root = document.getElementById('root');
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const nf = new Intl.NumberFormat('sv-SE');
let session = null;
let categories = [];

/* ---------- ikoner ---------- */
const ICON = {
  idag: '<svg viewBox="0 0 24 24"><path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/></svg>',
  planering: '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>',
  ovningsbank: '<svg viewBox="0 0 24 24"><rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/></svg>',
  match: '<svg viewBox="0 0 24 24"><rect x="2" y="5" width="20" height="14" rx="1"/><path d="M12 5v14M2 9h3v6H2M22 9h-3v6h3"/><circle cx="12" cy="12" r="2"/></svg>',
  verktyg: '<svg viewBox="0 0 24 24"><circle cx="5" cy="12" r="1.5"/><circle cx="12" cy="12" r="1.5"/><circle cx="19" cy="12" r="1.5"/></svg>',
};
const NAV = [['idag', 'Idag'], ['planering', 'Planering'], ['ovningsbank', 'Övningsbank'], ['match', 'Match'], ['verktyg', 'Verktyg']];
const PHASES = ['Anfall', 'Försvar', 'Omställning', 'Förberedelse', 'Skadeförebyggande'];
const PHASE_COLOR = { 'Anfall': 'var(--anfall)', 'Försvar': 'var(--forsvar)', 'Omställning': 'var(--omst)', 'Förberedelse': 'var(--forb)', 'Skadeförebyggande': 'var(--skad)' };

/* ---------- router ---------- */
function parseHash() {
  const h = location.hash.replace(/^#\/?/, '');
  const [path, query = ''] = h.split('?');
  const parts = path.split('/').filter(Boolean);
  return { page: parts[0] || 'idag', id: parts[1], params: new URLSearchParams(query) };
}
window.addEventListener('hashchange', () => { if (session) renderApp(); });

/* ---------- inloggning ---------- */
function renderLogin(msg = '') {
  document.title = 'Logga in · Övningsfabriken';
  root.innerHTML = `
  <div class="login">
    <section class="side">
      <a class="brand" href="../"><img src="../ovningsfabriken-mark.svg" alt="" width="22" height="28">Övningsfabriken</a>
      <div><h1>Passet klart innan du kliver ut på planen.</h1>
      <p>Logga in med din e-postadress. Du får en länk i mejlet, och när du trycker på den är du inne.</p></div>
    </section>
    <section class="form">
      <form id="lf" novalidate>
        <h2>Logga in</h2>
        <label class="field">E-post<input class="input" type="email" name="email" autocomplete="email" required placeholder="namn@klubb.se"></label>
        <p class="err" id="lerr" role="alert">${esc(msg)}</p>
        <button class="btn" type="submit" id="lbtn">Skicka inloggningslänk</button>
        <div class="sent" id="sent" hidden></div>
        <p class="small muted">Har du ingen licens än? <a href="../#kontakt">Kontakta oss</a>.</p>
      </form>
    </section>
  </div>`;
  const f = document.getElementById('lf');
  f.addEventListener('submit', async e => {
    e.preventDefault();
    const email = f.email.value.trim();
    const err = document.getElementById('lerr');
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) { err.textContent = 'Skriv en giltig e-postadress.'; f.email.focus(); return; }
    const b = document.getElementById('lbtn'); b.disabled = true; b.textContent = 'Skickar …'; err.textContent = '';
    const { error } = await sb.auth.signInWithOtp({ email, options: { emailRedirectTo: location.origin + location.pathname } });
    b.disabled = false; b.textContent = 'Skicka inloggningslänk';
    if (error) {
      err.textContent = /rate|limit|many/i.test(error.message)
        ? 'För många försök just nu. Vänta en stund och försök igen.'
        : 'Det gick inte att skicka länken. Försök igen om en stund.';
      return;
    }
    const s = document.getElementById('sent');
    s.innerHTML = `<b>Kolla din e-post.</b><br>Vi har skickat en inloggningslänk till ${esc(email)}. Mejlet kan komma på engelska och heter ”Your sign-in link”. Titta i skräpposten om det inte syns.`;
    s.hidden = false;
  });
}

/* ---------- appens skal ---------- */
function renderApp() {
  const { page } = parseHash();
  const email = session?.user?.email || '';
  if (!root.querySelector('.shell')) {
    root.innerHTML = `
    <div class="shell">
      <nav class="sidebar" aria-label="Appens meny">
        <a class="brand" href="#/idag"><img src="../ovningsfabriken-mark.svg" alt="" width="22" height="28">Övningsfabriken</a>
        <div class="nav">${NAV.map(([k, t]) => `<a href="#/${k}" data-k="${k}">${ICON[k]}<span>${t}</span></a>`).join('')}</div>
        <div class="me"><span>Inloggad som</span><b>${esc(email)}</b><button type="button" data-logout>Logga ut</button></div>
      </nav>
      <div>
        <div class="topbar"><a class="brand" href="#/idag"><img src="../ovningsfabriken-mark.svg" alt="" width="20" height="25">Övningsfabriken</a><button type="button" data-logout>Logga ut</button></div>
        <main class="view" id="view" tabindex="-1"></main>
      </div>
    </div>`;
    root.querySelectorAll('[data-logout]').forEach(b => b.addEventListener('click', () => sb.auth.signOut()));
  }
  const navKey = page === 'ovning' ? 'ovningsbank' : page;
  root.querySelectorAll('.nav a').forEach(a => { if (a.dataset.k === navKey) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current'); });
  const view = document.getElementById('view');
  const pages = { idag: viewIdag, ovningsbank: viewBank, ovning: viewExercise, planering: viewSoon, match: viewSoon, verktyg: viewSoon };
  (pages[page] || viewIdag)(view, parseHash());
  window.scrollTo(0, 0);
}

/* ---------- Idag ---------- */
function viewIdag(v) {
  document.title = 'Idag · Övningsfabriken';
  const d = new Date().toLocaleDateString('sv-SE', { weekday: 'long', day: 'numeric', month: 'long' });
  v.innerHTML = `
    <div class="pagehead"><div><p style="margin:0;font-weight:600;text-transform:capitalize">${esc(d)}</p><h1>Idag</h1></div></div>
    <div class="grid2">
      <a class="card" href="#/ovningsbank" style="text-decoration:none">
        <h2 style="font-size:24px">Övningsbanken</h2>
        <p class="muted" style="margin-top:6px">Sök bland alla övningar och filtrera på spelskede, ålder och antal spelare.</p>
        <p style="margin-top:14px;font-weight:700;color:var(--green)">Öppna övningsbanken →</p>
      </a>
      <div class="empty" style="text-align:left">
        <h2>Träningspass</h2>
        <p>Att skapa och köra träningspass kommer i nästa steg av den nya appen.</p>
      </div>
    </div>`;
}

/* ---------- sidor som byggs i senare steg ---------- */
function viewSoon(v, { page }) {
  const names = { planering: ['Planering', 'Pass, läroplan, säsong, spelidé och lagets utveckling.'], match: ['Match', 'Matchförberedelse, matchdag och efter matchen.'], verktyg: ['Verktyg', 'Rita egen övning, sparade övningar och progressioner.'] };
  const [t, d] = names[page];
  document.title = `${t} · Övningsfabriken`;
  v.innerHTML = `<div class="pagehead"><div><h1>${t}</h1><p>${d}</p></div></div>
    <div class="empty"><h2>Byggs just nu</h2><p>Den här delen flyttas över till den nya appen i ett kommande steg.</p></div>`;
}

/* ---------- Övningsbanken ---------- */
const PAGE = 30;
function exMeta(e) {
  const pl = e.players_min && e.players_max ? (e.players_min === e.players_max ? `${e.players_min} spelare` : `${e.players_min}–${e.players_max} spelare`) : e.players_min ? `${e.players_min}+ spelare` : '';
  return [pl, e.age_min ? `${e.age_min}+ år` : '', e.level ? `Nivå ${e.level}` : ''].filter(Boolean);
}
function exCard(e) {
  const cat = categories.find(c => c.slug === e.category_slug);
  const color = PHASE_COLOR[e.phase] || 'var(--green2)';
  return `<a class="ex" href="#/ovning/${esc(e.slug)}" style="--c:${color}">
    <span class="bar"></span>
    <span class="body">
      <span class="stage">${esc(cat?.name || e.phase || '')}</span>
      <h3>${esc(e.title)}</h3>
      <span class="meta">${exMeta(e).map(esc).join('<span aria-hidden="true">·</span>')}
        ${e.video_path ? '<span class="tag vid">Video</span>' : ''}${e.source === 'svff' ? '<span class="tag svff">SvFF</span>' : ''}${e.source === 'egen' ? '<span class="tag">Egen</span>' : ''}</span>
    </span></a>`;
}
function bankQuery(p) {
  let q = sb.from('exercises').select('slug,title,phase,category_slug,players_min,players_max,age_min,level,source,video_path', { count: 'exact' });
  const text = (p.get('q') || '').replace(/[,()%*\\]/g, ' ').trim();
  if (text) q = q.or(`title.ilike.%${text}%,setup.ilike.%${text}%,ex_type.ilike.%${text}%`);
  if (p.get('fas')) q = q.eq('phase', p.get('fas'));
  if (p.get('moment')) q = q.eq('category_slug', p.get('moment'));
  if (p.get('spelform')) q = q.contains('game_sizes', [Number(p.get('spelform'))]);
  if (p.get('alder')) q = q.lte('age_min', Number(p.get('alder')));
  if (p.get('spelare')) { const n = Number(p.get('spelare')); q = q.lte('players_min', n).gte('players_max', n); }
  if (p.get('kalla')) q = q.eq('source', p.get('kalla'));
  return q.order('source', { ascending: true }).order('title', { ascending: true });
}
function viewBank(v, { params }) {
  document.title = 'Övningsbank · Övningsfabriken';
  const p = params;
  const opt = (val, label, cur) => `<option value="${esc(val)}"${String(cur || '') === String(val) ? ' selected' : ''}>${esc(label)}</option>`;
  const fas = p.get('fas') || '';
  const moments = categories.filter(c => !fas || c.phase === fas);
  v.innerHTML = `
    <div class="pagehead"><div><h1>Övningsbank</h1><p>Hitta en övning för det ni ska träna.</p></div></div>
    <form id="bf" class="card" role="search">
      <div class="search">
        <label class="field"><span class="sr" style="position:absolute;left:-9999px">Sök övning</span>
          <input class="input" type="search" name="q" value="${esc(p.get('q') || '')}" placeholder="Sök, till exempel rondo, speluppbyggnad eller avslut" autocomplete="off"></label>
        <button class="btn" type="submit">Sök</button>
      </div>
      <details class="fwrap" id="fwrap"><summary>Filter${(() => { const n = ["fas","moment","spelform","alder","spelare","kalla"].filter(k => p.get(k)).length; return n ? ` (${n} valda)` : ""; })()}</summary>
      <div class="filters">
        <label class="field">Fas<select class="input" name="fas">${opt('', 'Alla faser', fas)}${PHASES.map(x => opt(x, x, fas)).join('')}</select></label>
        <label class="field">Moment<select class="input" name="moment">${opt('', 'Alla moment', p.get('moment'))}${moments.map(c => opt(c.slug, c.name, p.get('moment'))).join('')}</select></label>
        <label class="field">Spelform<select class="input" name="spelform">${opt('', 'Alla', p.get('spelform'))}${[3, 5, 7, 9, 11].map(n => opt(n, `${n} mot ${n}`, p.get('spelform'))).join('')}</select></label>
        <label class="field">Spelarnas ålder<select class="input" name="alder">${opt('', 'Alla åldrar', p.get('alder'))}${[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16].map(n => opt(n, `${n} år`, p.get('alder'))).join('')}</select></label>
        <label class="field">Antal spelare<input class="input" name="spelare" inputmode="numeric" pattern="[0-9]*" maxlength="2" value="${esc(p.get('spelare') || '')}" placeholder="t.ex. 12"></label>
        <label class="field">Källa<select class="input" name="kalla">${opt('', 'Alla', p.get('kalla'))}${opt('egen', 'Egna övningar', p.get('kalla'))}${opt('extern', 'Från andra källor', p.get('kalla'))}${opt('svff', 'SvFF:s övningsbank', p.get('kalla'))}</select></label>
      </div></details>
    </form>
    <div class="resbar"><span id="count" aria-live="polite">Söker …</span><button type="button" id="clear"${[...p.keys()].length ? '' : ' hidden'}>Rensa sökning och filter</button></div>
    <div class="exlist" id="list">${'<div class="skel"></div>'.repeat(6)}</div>
    <div class="more"><button class="btn ghost" type="button" id="more" hidden>Visa fler</button></div>`;

  const f = document.getElementById('bf');
  const fw = document.getElementById('fwrap');
  fw.open = matchMedia('(min-width: 601px)').matches || ['fas','moment','spelform','alder','spelare','kalla'].some(k => p.get(k));
  const go = () => {
    const np = new URLSearchParams();
    for (const [k, val] of new FormData(f)) if (String(val).trim()) np.set(k, String(val).trim());
    if (np.get('fas') && np.get('moment') && categories.find(c => c.slug === np.get('moment'))?.phase !== np.get('fas')) np.delete('moment');
    location.hash = '#/ovningsbank' + (np.toString() ? '?' + np : '');
  };
  f.addEventListener('submit', e => { e.preventDefault(); go(); });
  f.querySelectorAll('select').forEach(s => s.addEventListener('change', go));
  f.spelare.addEventListener('change', go);
  document.getElementById('clear').onclick = () => { location.hash = '#/ovningsbank'; };

  let offset = 0;
  const list = document.getElementById('list');
  const more = document.getElementById('more');
  async function load(first) {
    more.disabled = true;
    const { data, count, error } = await bankQuery(p).range(offset, offset + PAGE - 1);
    if (error) { list.innerHTML = `<div class="empty"><h2>Något gick fel</h2><p>Övningarna kunde inte hämtas. Försök igen om en stund.</p></div>`; document.getElementById('count').textContent = ''; return; }
    document.getElementById('count').textContent = `${nf.format(count)} övningar`;
    if (first) list.innerHTML = '';
    if (first && !data.length) list.innerHTML = `<div class="empty" style="grid-column:1/-1"><h2>Inga övningar matchar</h2><p>Prova att ta bort ett filter eller söka på ett annat ord.</p></div>`;
    list.insertAdjacentHTML('beforeend', data.map(exCard).join(''));
    offset += data.length;
    more.hidden = offset >= count; more.disabled = false;
  }
  more.onclick = () => load(false);
  load(true);
}

/* ---------- en övning ---------- */
async function viewExercise(v, { id }) {
  v.innerHTML = `<a class="back" href="javascript:history.back()">← Tillbaka till övningsbanken</a><div class="skel" style="height:240px"></div>`;
  const { data: e, error } = await sb.from('exercises').select('*').eq('slug', id).maybeSingle();
  if (error || !e) { v.innerHTML = `<a class="back" href="#/ovningsbank">← Övningsbanken</a><div class="empty"><h2>Övningen hittades inte</h2></div>`; return; }
  document.title = `${e.title} · Övningsfabriken`;
  const cat = categories.find(c => c.slug === e.category_slug);
  const color = PHASE_COLOR[e.phase] || 'var(--green2)';
  const fact = (label, val) => val ? `<span class="fact"><small>${label}</small>${esc(val)}</span>` : '';
  const players = e.players_min && e.players_max ? (e.players_min === e.players_max ? `${e.players_min}` : `${e.players_min}–${e.players_max}`) : e.players_min ? `${e.players_min}+` : '';
  const vid = e.video_path ? (e.video_path.startsWith('http') ? e.video_path : '../' + e.video_path) : '';
  const poster = e.poster_path ? (e.poster_path.startsWith('http') ? e.poster_path : '../' + e.poster_path) : '';
  const sec = (t, html) => html ? `<section class="sec card"><h2>${t}</h2>${html}</section>` : '';
  v.innerHTML = `
    <a class="back" href="javascript:history.back()">← Tillbaka till övningsbanken</a>
    <header class="exhead" style="--c:${color}">
      <span class="stage">${esc(e.phase || '')}${cat ? ' · ' + esc(cat.name) : ''}</span>
      <h1>${esc(e.title)}</h1>
      <div class="facts">${fact('Spelare', players)}${fact('Ålder', e.age_min ? e.age_min + '+ år' : '')}${fact('Nivå', e.level)}${fact('Typ', e.ex_type)}${fact('Spelform', e.game_sizes?.length ? e.game_sizes.map(n => n + ' mot ' + n).join(', ') : '')}</div>
    </header>
    <div class="exbody">
      <div>
        ${sec('Upplägg', e.setup ? `<p>${esc(e.setup)}</p>` : '')}
        ${sec('Organisation', e.organisation ? `<p>${esc(e.organisation)}</p>` : '')}
        ${sec('Regler', e.rules ? `<p>${esc(e.rules)}</p>` : '')}
        ${sec('Coachningspunkter', e.coaching_points?.length ? `<ul>${e.coaching_points.map(x => `<li>${esc(x)}</li>`).join('')}</ul>` : '')}
        ${sec('Gör den lättare', e.easier ? `<p>${esc(e.easier)}</p>` : '')}
        ${sec('Gör den svårare', e.harder ? `<p>${esc(e.harder)}</p>` : '')}
        ${e.source === 'svff' && e.source_url ? `<section class="sec card"><h2>Hela övningen hos SvFF</h2><p class="muted">Upplägg, anvisningar och bild finns i Svensk Fotbolls övningsbank.</p><p style="margin-top:12px"><a class="btn ghost" href="${esc(e.source_url)}" target="_blank" rel="noopener">Öppna hos SvFF ↗</a></p></section>` : ''}
      </div>
      <div>${vid ? `<video class="exvideo" src="${esc(vid)}" poster="${esc(poster)}" controls playsinline muted loop preload="metadata"></video>` : ''}</div>
    </div>`;
}

/* ---------- start ---------- */
async function start() {
  const { data } = await sb.auth.getSession();
  session = data.session;
  sb.auth.onAuthStateChange((_evt, s) => {
    const was = !!session; session = s;
    if (!!s !== was || !s) boot();
  });
  boot();
}
async function boot() {
  if (!session) { renderLogin(); return; }
  if (!categories.length) {
    const { data } = await sb.from('categories').select('slug,name,phase,sort_order').order('sort_order');
    categories = data || [];
  }
  if (location.hash.includes('access_token')) history.replaceState(null, '', location.pathname + '#/idag');
  root.innerHTML = '';
  renderApp();
}
start();
