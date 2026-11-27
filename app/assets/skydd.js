/* Övningsfabriken – skyddat innehåll
 * 1) Appens kod (med övningsbanken) laddas först när inloggningsgrinden släpper in tränaren.
 *    Den hämtas från Supabase-lagringen 'skyddat' via en tillfällig länk och sparas på enheten per version.
 * 2) Filmer och förhandsbilder pekas ut med data-skydd-* och får tillfälliga länkar (1 timme).
 * RESERV = true: så länge filerna också ligger öppet på GitHub används de om något saknas i lagringen.
 * När kodförrådet blivit privat och filerna tagits bort sätts RESERV till false.
 */
(function () {
  'use strict';
  const RESERV = true;
  const BUCKET = 'skyddat';
  const M = () => window.OF_MOLN;
  const meta = document.querySelector('meta[name="of-app"]')?.content || '';
  const [appFile, appVer] = meta.split('?v=');
  const stats = { app: 'väntar', appKalla: '', media: 0, mediaLagring: 0, mediaReserv: 0, fel: [] };

  /* ---------- Appens kod ---------- */
  let appPromise = null;
  function inject(src) {
    return new Promise((resolve, reject) => {
      const s = document.createElement('script'); s.src = src; s.onload = resolve; s.onerror = () => reject(new Error('Kunde inte köra appen'));
      document.body.appendChild(s);
    });
  }
  const valid = t => typeof t === 'string' && t.length > 100000 && t.includes('startWorkspace');
  async function fromCache() {
    try {
      const c = await caches.open('of-skydd'); const r = await c.match('/of-app/' + appVer);
      if (r) { const t = await r.text(); if (valid(t)) return t; await c.delete('/of-app/' + appVer); }
    } catch (e) { }
    return null;
  }
  async function toCache(text) {
    try {
      const c = await caches.open('of-skydd');
      for (const k of await c.keys()) if (k.url.includes('/of-app/')) await c.delete(k);
      await c.put('/of-app/' + appVer, new Response(text, { headers: { 'Content-Type': 'text/javascript' } }));
    } catch (e) { }
  }
  /* Version som saknas i lagringen kommer vi ihåg, så att vi inte frågar i onödan vid varje start */
  const NOSTORE = 'of-skydd-saknas';
  const lsGet = k => { try { return localStorage.getItem(k); } catch (e) { return null; } };
  const lsSet = (k, v) => { try { localStorage.setItem(k, v); } catch (e) { } };
  async function fromStorage() {
    if (lsGet(NOSTORE) === appVer) return null;
    try { await M()?.ready; } catch (e) { }
    if (!M()?.sb) return null;
    try {
      const { data, error } = await M().sb.storage.from(BUCKET).createSignedUrl('app/' + appVer + '.js', 120);
      if (error) throw error;
      const r = await fetch(data.signedUrl); if (!r.ok) throw new Error('HTTP ' + r.status);
      const t = await r.text(); if (!valid(t)) throw new Error('Ogiltig appkod i lagringen');
      return t;
    } catch (e) {
      stats.fel.unshift('App från lagring: ' + (e.message || e));
      if (/not.?found|404|Object not found/i.test(e.message || '')) lsSet(NOSTORE, appVer);
      return null;
    }
  }
  async function fromReserve() {
    try { const r = await fetch('./assets/' + appFile + '?v=' + appVer, { cache: 'no-cache' }); if (!r.ok) return null; const t = await r.text(); return valid(t) ? t : null; }
    catch (e) { return null; }
  }
  async function loadApp() {
    if (appPromise) return appPromise;
    appPromise = (async () => {
      // 1) Enheten: appens kod sparad sedan förra gången – ingen nätverkstrafik alls
      let text = await fromCache(); let kalla = 'enheten';
      // 2) Lagringen, 3) den öppna reservkopian. Det som hämtas sparas på enheten till nästa start.
      if (!text) { text = await fromStorage(); kalla = 'lagringen'; }
      if (!text && RESERV) { text = await fromReserve(); kalla = 'öppen reserv'; }
      if (text) {
        if (kalla !== 'enheten') toCache(text);
        const url = URL.createObjectURL(new Blob([text], { type: 'text/javascript' }));
        await inject(url); stats.app = 'laddad'; stats.appKalla = kalla; return;
      }
      if (RESERV) { await inject('./assets/' + appFile + '?v=' + appVer); stats.app = 'laddad'; stats.appKalla = 'öppen reserv'; return; }
      stats.app = 'fel'; throw new Error('Appen kunde inte laddas');
    })();
    appPromise.then(() => { scan(); window.OF_GRIND?.appReady(); }).catch(e => {
      const app = document.getElementById('app');
      if (app) app.innerHTML = '<p role="alert" style="padding:24px">Appen kunde inte laddas. Kontrollera nätet och ladda om sidan.</p>';
    });
    return appPromise;
  }
  /* Börja hämta appens kod direkt om enheten redan har tillgång – inloggningskontrollen sker parallellt */
  function prefetch() { if (!appPromise) fromCache().then(t => { if (!t && RESERV && lsGet(NOSTORE) === appVer) fromReserve().then(x => x && toCache(x)); }); }

  /* ---------- Filmer och bilder ---------- */
  /* Tillfälliga länkar och vilka filer som saknas i lagringen sparas på enheten,
     så att bilder och filmer visas direkt utan en fråga till servern vid varje sidbyte och start. */
  const MKEY = 'of-skydd-media.v2';   // v2: lagringen fylldes 27 nov – gamla ”saknas”-minnen gäller inte längre
  try { localStorage.removeItem('of-skydd-media'); } catch (e) { }
  const urls = new Map(); // namn -> { url, exp }
  const missing = new Set();
  let storeEmpty = false;   // lagringen har inga mediafiler än (reservläge): använd reserven direkt
  try {
    const o = JSON.parse(localStorage.getItem(MKEY) || 'null');
    if (o && Date.now() - o.at < 12 * 3600e3) {
      (o.missing || []).forEach(n => missing.add(n)); storeEmpty = !!o.empty;
      Object.entries(o.urls || {}).forEach(([n, v]) => { if (v.exp > Date.now() + 60e3) urls.set(n, v); });
    }
  } catch (e) { }
  let saveT = null;
  function saveMedia() {
    clearTimeout(saveT); saveT = setTimeout(() => {
      const u = {}; [...urls.entries()].slice(-400).forEach(([n, v]) => { if (v.exp > Date.now()) u[n] = v; });
      try { localStorage.setItem(MKEY, JSON.stringify({ at: Date.now(), empty: storeEmpty, missing: [...missing].slice(-2000), urls: u })); } catch (e) { }
    }, 500);
  }
  let checkedThisSession = false;
  let queue = new Set(), timer = null;
  const ATTRS = [['data-skydd-poster', 'poster'], ['data-skydd-src', 'src'], ['data-skydd-href', 'href']];
  const SEL = ATTRS.map(([a]) => '[' + a + ']').join(',');
  function apply(el) {
    for (const [a, prop] of ATTRS) {
      const n = el.getAttribute(a); if (!n) continue;
      const hit = urls.get(n);
      let url = hit && hit.exp > Date.now() ? hit.url : null;
      if (!url && RESERV && (missing.has(n) || storeEmpty)) { url = 'assets/' + n; if (storeEmpty && !missing.has(n) && !checkedThisSession) queue.add(n); }
      if (!url) { queue.add(n); continue; }
      if (el.getAttribute(prop) !== url) {
        el.setAttribute(prop, url);
        if (el.tagName === 'SOURCE' && el.parentElement?.tagName === 'VIDEO') { const v = el.parentElement; if (!v.dataset.skyddLoaded) { v.dataset.skyddLoaded = '1'; v.load(); } }
      }
    }
  }
  function scan(root) {
    (root || document).querySelectorAll(SEL).forEach(apply);
    if (queue.size) { clearTimeout(timer); timer = setTimeout(fetchUrls, 10); }
  }
  async function fetchUrls() {
    let names = [...queue]; queue = new Set(); if (!names.length || !M()?.sb || !M().state.user) return;
    if (storeEmpty) { if (checkedThisSession) return; checkedThisSession = true; names = names.slice(0, 20); }   // en stickprovskoll per besök
    let hits = 0;
    for (let i = 0; i < names.length; i += 100) {
      const part = names.slice(i, i + 100);
      try {
        const { data, error } = await M().sb.storage.from(BUCKET).createSignedUrls(part.map(n => 'media/' + n), 3600);
        if (error) throw error;
        data.forEach((d, k) => {
          const n = part[k];
          if (d.signedUrl) { urls.set(n, { url: d.signedUrl, exp: Date.now() + 3300e3 }); stats.mediaLagring++; hits++; }
          else { missing.add(n); stats.mediaReserv++; }
        });
      } catch (e) { part.forEach(n => missing.add(n)); stats.fel.unshift('Medialänkar: ' + (e.message || e)); }
    }
    stats.media = urls.size + missing.size;
    storeEmpty = RESERV && hits === 0 && names.length >= 3 ? true : (hits > 0 ? false : storeEmpty);
    saveMedia();
    document.querySelectorAll(SEL).forEach(el => { for (const [a] of ATTRS) { const n = el.getAttribute(a); if (n && names.includes(n)) { apply(el); break; } } });
  }
  new MutationObserver(muts => {
    for (const m of muts) for (const node of m.addedNodes) {
      if (node.nodeType !== 1) continue;
      if (node.matches?.(SEL)) apply(node);
      if (node.querySelector?.(SEL)) node.querySelectorAll(SEL).forEach(apply);
    }
    if (queue.size) { clearTimeout(timer); timer = setTimeout(fetchUrls, 10); }
  }).observe(document.documentElement, { childList: true, subtree: true });

  window.OF_SKYDD = { loadApp, scan, stats, RESERV, appFile, appVer, BUCKET, prefetch };
  try { if (JSON.parse(localStorage.getItem('of-tillgang') || 'null')?.ok) prefetch(); } catch (e) { }
})();
