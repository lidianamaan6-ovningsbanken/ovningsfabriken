/* Övningsfabriken – service worker
 * Gör appen snabb och användbar utan nät:
 *  - Sidan (app.html): nätet först, sparad kopia om nätet saknas.
 *  - Versionerade filer (?v=…), typsnitt och bilder: från enheten direkt, uppdateras i bakgrunden.
 *  - Appens stora kod hanteras av skydd.js (egen cache), filmer och inloggning (Supabase) går alltid direkt till nätet.
 */
const SKAL = 'of-skal-v1';
const START = ['./app.html', './workspace.css?v=38', './grind.css?v=7', './assets/vendor/supabase.js?v=2', './lagkatalog.js', './stockholm-p2009.js'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(SKAL).then(c => c.addAll(START).catch(() => { })).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k.startsWith('of-skal-') && k !== SKAL).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});

const MEDIA = /\.(png|jpe?g|webp|svg|gif|woff2?|ico)$/i;
const CODE = /\.(js|css|json|webmanifest)$/i;
const JSPDF = /cdnjs\.cloudflare\.com\/ajax\/libs\/(jspdf|pdf\.js)\//;

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (JSPDF.test(req.url)) { e.respondWith(cacheFirst(req)); return; }              // PDF-biblioteken (jsPDF, PDF.js): hämtas en gång
  if (url.origin !== location.origin) return;                                        // Supabase m.m.: alltid nätet
  if (/\/assets\/app-[0-9a-f]+\.js$/.test(url.pathname)) return;                     // appens kod: skydd.js sköter den
  if (/\.(mp4|webm|mov)$/i.test(url.pathname)) return;                               // filmer: webbläsarens egen hantering (spolning)
  if (req.mode === 'navigate') { e.respondWith(networkFirst(req)); return; }
  if (MEDIA.test(url.pathname) || (CODE.test(url.pathname) && url.search.includes('v='))) { e.respondWith(cacheFirst(req)); return; }
  if (CODE.test(url.pathname)) { e.respondWith(staleWhileRevalidate(req)); return; }
});

async function cacheFirst(req) {
  const c = await caches.open(SKAL); const hit = await c.match(req);
  if (hit) return hit;
  const res = await fetch(req); if (res.ok || res.type === 'opaque') c.put(req, res.clone()).catch(() => { });
  return res;
}
async function staleWhileRevalidate(req) {
  const c = await caches.open(SKAL); const hit = await c.match(req);
  const net = fetch(req).then(res => { if (res.ok) c.put(req, res.clone()).catch(() => { }); return res; }).catch(() => hit);
  return hit || net;
}
async function networkFirst(req) {
  const c = await caches.open(SKAL);
  try {
    const res = await fetch(req);
    if (res.ok) c.put(new URL(req.url).pathname.endsWith('/') ? './app.html' : req, res.clone()).catch(() => { });
    return res;
  } catch (e) {
    return (await c.match(req, { ignoreSearch: true })) || (await c.match('./app.html')) || Response.error();
  }
}
