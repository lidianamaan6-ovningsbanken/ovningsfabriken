/* Övningsfabriken – språkval
 * Appen skrivs på svenska. När ett annat språk är valt översätts allt som visas på skärmen
 * (texter, knappar, platshållare, hjälptexter) med en ordlista per språk i assets/sprak/.
 * Ordlistan matchar hela texter, texter med siffror (”12 övningar” → ”12 exercises”)
 * och datum ord för ord. Det tränaren själv skriver (namn, anteckningar) lämnas orört.
 * Valt språk sparas på enheten. Byte av språk laddar om sidan.
 */
(function () {
  'use strict';
  /* Versionsnummer för ordlistorna – skrivs av verktyg/sprak/bygg_sprak.py */
  const V = {"en":"866fc46f","bank-en":"a5f2f0a9","ar":"568566e2","bank-ar":"3f62950a","de":"e5ed8d81","bank-de":"b75e1277","es":"29366827","bank-es":"fb53a736","fi":"d496d187","bank-fi":"4a06f66f","fr":"842557c7","bank-fr":"578a7a94"};
  const LANGS = [
    ['sv', 'Svenska'], ['en', 'English'], ['ar', 'العربية', 1], ['fa', 'فارسی', 1], ['fi', 'Suomi'], ['es', 'Español'],
    ['de', 'Deutsch'], ['fr', 'Français'], ['pl', 'Polski'], ['tr', 'Türkçe'], ['uk', 'Українська'], ['ru', 'Русский'], ['pt', 'Português'], ['it', 'Italiano']
  ].filter(l => l[0] === 'sv' || V[l[0]]);
  const KEY = 'of-sprak';
  const base = (document.currentScript && document.currentScript.src) ? new URL('sprak/', document.currentScript.src).href : 'assets/sprak/';
  let lang = 'sv';
  try {
    const q = new URLSearchParams(location.search).get('lang');
    lang = (q || localStorage.getItem(KEY) || 'sv').toLowerCase();
    if (q) localStorage.setItem(KEY, lang);
  } catch (e) { }
  if (!LANGS.some(l => l[0] === lang)) lang = 'sv';
  const info = LANGS.find(l => l[0] === lang);
  const root = document.documentElement;
  const api = window.OF_SPRAK = { lang, langs: LANGS, missing: new Set(), t: s => s, open, set, label: () => info[1] };

  /* Väljaren: knappar med data-sprak-open öppnar den, var de än står */
  document.addEventListener('click', e => { const b = e.target.closest && e.target.closest('[data-sprak-open]'); if (b) { e.preventDefault(); open(); } });
  function set(code) { try { localStorage.setItem(KEY, code); } catch (e) { } const u = new URL(location.href); u.searchParams.delete('lang'); location.replace(u.toString()); }
  function open() {
    let w = document.getElementById('of-sprak-val'); if (w) w.remove();
    w = document.createElement('div'); w.id = 'of-sprak-val'; w.setAttribute('translate', 'no');
    w.innerHTML = '<div class="of-sp-card" role="dialog" aria-modal="true" aria-labelledby="of-sp-h"><h2 id="of-sp-h">Språk · Language</h2><div class="of-sp-list">'
      + LANGS.map(([c, n, r]) => '<button type="button" data-sp="' + c + '"' + (c === lang ? ' aria-current="true"' : '') + (r ? ' dir="rtl"' : '') + ' lang="' + c + '">' + n + '</button>').join('')
      + '</div><p class="of-sp-note">' + (lang === 'sv' ? 'Andra språk än svenska är maskinöversatta och kan innehålla fel.' : 'Machine translated · Maskinöversatt') + '</p><button type="button" class="of-sp-close" data-sp-x>✕</button></div>';
    w.addEventListener('click', e => {
      const b = e.target.closest('[data-sp]'); if (b) { if (b.dataset.sp !== lang) set(b.dataset.sp); else w.remove(); return; }
      if (e.target === w || e.target.closest('[data-sp-x]')) w.remove();
    });
    document.addEventListener('keydown', function esc(e) { if (e.key === 'Escape') { w.remove(); document.removeEventListener('keydown', esc); } });
    document.body.appendChild(w);
    (w.querySelector('[aria-current]') || w.querySelector('button')).focus();
  }
  const css = document.createElement('style');
  css.textContent = '#of-sprak-val{position:fixed;inset:0;z-index:10000;background:rgba(10,20,15,.55);display:flex;align-items:center;justify-content:center;padding:16px;font-family:"DM Sans",system-ui,sans-serif}'
    + '.of-sp-card{position:relative;background:#f4f1ea;color:#13241b;border-radius:18px;padding:22px 20px 16px;width:min(420px,100%);max-height:90vh;overflow:auto;box-shadow:0 20px 60px rgba(0,0,0,.35)}'
    + '.of-sp-card h2{margin:0 0 14px;font-size:20px}.of-sp-list{display:grid;grid-template-columns:1fr 1fr;gap:8px}'
    + '.of-sp-list button{font:inherit;font-size:16px;padding:12px;border-radius:12px;border:1px solid #d8d2c4;background:#fff;color:inherit;cursor:pointer;text-align:start}'
    + '.of-sp-list button[aria-current]{background:#1f6143;color:#fff;border-color:#1f6143}.of-sp-list button:focus-visible{outline:3px solid #c9a227;outline-offset:2px}'
    + '.of-sp-note{font-size:13px;color:#5b6b62;margin:12px 0 0}.of-sp-close{position:absolute;top:10px;inset-inline-end:10px;border:0;background:none;font-size:18px;cursor:pointer;color:inherit;padding:6px 10px}'
    + 'html.of-sp-wait body{visibility:hidden}';
  (document.head || root).appendChild(css);
  const kod = () => document.querySelectorAll('[data-sprak-kod]').forEach(e => { e.textContent = lang.toUpperCase(); });
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', kod); else kod();
  if (lang === 'sv') return;

  /* ---------- Översättning ---------- */
  root.lang = lang; if (info[2]) root.dir = 'rtl';
  root.classList.add('of-sp-wait', 'of-sp-' + lang);
  const waitT = setTimeout(() => root.classList.remove('of-sp-wait'), 4000);
  let D = null, N = new Map(), W = {}, P = [];
  const NUM = /\d+(?:[.,:]\d+)*/g;
  const ORIG = new WeakMap(), OUT = new WeakMap(), AORIG = new WeakMap();
  const ATTRS = ['placeholder', 'title', 'aria-label', 'alt'];
  const SKIP = /^(SCRIPT|STYLE|TEXTAREA|NOSCRIPT|CODE|PRE)$/;

  function lookup(core, depth = 0) {
    let r = D[core]; if (r != null) return r;
    if (/\d/.test(core)) {
      const nums = core.match(NUM), k = core.replace(NUM, '#');
      const t = N.get(k); if (t != null) { let i = 0; return /\{\d+\}/.test(t) ? t.replace(/\{(\d+)\}/g, (_, j) => nums[j - 1] ?? '') : t.replace(/#/g, () => nums[i++] ?? ''); }
    }
    if (depth < 2) for (const [re, t, lit] of P) {
      if (!core.includes(lit)) continue;
      const m = core.match(re); if (!m) continue;
      return t.replace(/\{(\d)\}/g, (_, i) => { const g = m[+i] ?? ''; const x = g && /[A-Za-zÅÄÖåäö]/.test(g) ? lookup(g.trim(), depth + 1) : null; return x ?? g; });
    }
    // Etikett med kolon (”Speldjup:”)
    if (depth < 2 && /:$/.test(core) && core.length > 2) { const r = lookup(core.slice(0, -1), depth + 1); if (r != null) return r + ':'; }
    // Sammansatta rader (”Alla typer · 16–19 år · Halv plan”): del för del
    if (depth < 2 && core.includes(' · ')) {
      let any = false; const o = core.split(' · ').map(x => { const r = lookup(x, depth + 1); if (r != null) any = true; return r ?? x; });
      if (any) return o.join(' · ');
    }
    // Datum och korta ordföljder: översätt ord för ord om varje ord är känt
    const toks = core.split(/(\s+|[.,·–—\-/:()])/);
    if (toks.length < 16) {
      let ok = true, any = false;
      const o = toks.map(x => { if (!x || /^(\s+|[.,·–—\-/:()]|\d+)$/.test(x)) return x; const lw = x.toLowerCase(); const w = W[x] ?? W[lw]; if (w == null) { ok = false; return x; } any = true; return x === x.toUpperCase() && x !== lw ? w.toUpperCase() : (x[0] !== lw[0] ? w[0].toUpperCase() + w.slice(1) : w); });
      if (ok && any) return o.join('');
    }
    return null;
  }
  function tr(s) {
    if (!s || !/[A-Za-zÅÄÖåäöÉé]/.test(s)) return null;
    const m = s.match(/^(\s*)([\s\S]*?)(\s*)$/); const core = m[2].replace(/\s+/g, ' ');
    const r = lookup(core);
    if (r == null) { if (core.length < 400) api.missing.add(core); return null; }
    return m[1] + r + m[3];
  }
  api.t = s => tr(s) ?? s;
  const skip = el => { for (let e = el; e; e = e.parentElement) { if (SKIP.test(e.tagName) || e.isContentEditable || e.getAttribute('translate') === 'no' || e.classList.contains('notranslate')) return true; if (e === document.body) break; } return false; };
  let retry = false;
  function doText(n) {
    const cur = n.nodeValue; if (OUT.get(n) === cur && !(retry && ORIG.get(n) === cur)) return;
    if (!n.parentElement || skip(n.parentElement)) return;
    ORIG.set(n, cur); const t = tr(cur);
    if (t != null && t !== cur) { OUT.set(n, t); n.nodeValue = t; } else OUT.set(n, cur);
  }
  function doAttrs(el) {
    let o = AORIG.get(el);
    for (const a of ATTRS) {
      const v = el.getAttribute(a); if (v == null) continue;
      if (o && o[a] && o[a][1] === v) continue;
      const t = tr(v); if (!o) { o = {}; AORIG.set(el, o); }
      o[a] = [v, t ?? v]; if (t != null && t !== v) el.setAttribute(a, t);
    }
    if (el.tagName === 'INPUT' && /^(button|submit|reset)$/i.test(el.type) && el.value) { const t = tr(el.value); if (t != null && t !== el.value) el.value = t; }
  }
  function walk(node) {
    if (node.nodeType === 3) { doText(node); return; }
    if (node.nodeType !== 1 || SKIP.test(node.tagName)) return;
    if (node.getAttribute('translate') === 'no') return;
    doAttrs(node);
    const it = document.createTreeWalker(node, NodeFilter.SHOW_ELEMENT | NodeFilter.SHOW_TEXT, { acceptNode: n => n.nodeType === 1 && (SKIP.test(n.tagName) || n.getAttribute('translate') === 'no' || n.classList.contains('notranslate')) ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT });
    let n; while ((n = it.nextNode())) { if (n.nodeType === 3) doText(n); else doAttrs(n); }
  }
  function titleFix() { const t = tr(document.title); if (t && t !== document.title) document.title = t; }
  const mo = new MutationObserver(muts => {
    for (const m of muts) {
      if (m.type === 'characterData') doText(m.target);
      else if (m.type === 'attributes') { if (m.target.nodeType === 1 && !skip(m.target)) doAttrs(m.target); }
      else for (const n of m.addedNodes) { if (n.nodeType === 3 ? true : !skip(n.parentElement || n)) walk(n); }
    }
  });

  function build(d) {
    D = Object.assign(Object.create(null), d.t || {});
    for (const [k, v] of Object.entries(d.n || {})) N.set(k, v);
    for (const [k, v] of Object.entries(D)) if (/\d/.test(k)) { const kk = k.replace(NUM, '#'); if (!N.has(kk) && (k.match(NUM) || []).length === (v.match(NUM) || []).length && !/\d/.test(v.replace(NUM, '#').replace(/#/g, ''))) N.set(kk, v.replace(NUM, '#')); }
    W = Object.assign(Object.create(null), d.w || {});
    P = (d.p || []).map(([k, v]) => { const parts = k.split('{}'); return [new RegExp('^' + parts.map(x => x.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('(.+?)') + '$'), v, parts.reduce((a, b) => b.length > a.length ? b : a, '')]; })
      .sort((a, b) => b[2].length - a[2].length);
  }
  function start(d) {
    build(d);
    const go = () => {
      walk(document.body); titleFix();
      mo.observe(root, { subtree: true, childList: true, characterData: true, attributes: true, attributeFilter: ATTRS });
      clearTimeout(waitT); root.classList.remove('of-sp-wait');
    };
    if (document.body) go(); else document.addEventListener('DOMContentLoaded', go);
  }
  /* Övningsbankens texter: separat fil som läses in efter inloggningen (se skydd.js) */
  api.addBank = d => { if (!D) return; Object.assign(D, d.t || {}); api.missing.clear(); if (document.body) { retry = true; try { walk(document.body); } finally { retry = false; } } };
  const get = n => fetch(base + n + '.json?v=' + (V[n] || ''), { cache: 'force-cache' }).then(r => { if (!r.ok) throw new Error(r.status); return r.json(); });
  const ui = get(lang);
  ui.then(start).catch(() => { root.classList.remove('of-sp-wait'); });
  /* Övningsbankens texter behövs bara i appen – hämtas parallellt och läggs till när de kommer */
  if (document.querySelector('meta[name="of-app"]') && V['bank-' + lang]) Promise.all([ui, get('bank-' + lang)]).then(([, b]) => api.addBank(b)).catch(() => { });
})();
