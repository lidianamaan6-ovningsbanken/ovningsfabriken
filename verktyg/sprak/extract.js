const fs=require('fs'),acorn=require('acorn'),walk=require('acorn-walk');
const R='/home/user/ovningsfabriken/';
const bank=new Set();
for(const e of JSON.parse(fs.readFileSync(R+'verktyg/film/data/bank.json'))){for(const k of ['name','orig','org','rules','phase','stage','type'])if(e[k])bank.add(e[k]);(e.points||[]).forEach(p=>bank.add(p));}
const out=new Map();
const dec=s=>s.replace(/&nbsp;/g,' ').replace(/&amp;/g,'&').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&quot;/g,'"').replace(/&#39;|&apos;/g,"'").replace(/&middot;/g,'·').replace(/&ndash;/g,'–').replace(/&mdash;/g,'—').replace(/&hellip;/g,'…').replace(/&rarr;/g,'→').replace(/&larr;/g,'←');
function isText(t){
  if(t.length<2||!/[A-Za-zÅÄÖåäö]{2}/.test(t))return false;
  if(/^[a-z0-9_.#:\-\[\]=*>+~ (),'"]+$/.test(t)&&!/[åäö]/.test(t)&&!/ [a-z]{3,} [a-z]{3,}/.test(t))return false; // klassnamn/selektorer
  if(/^(https?:|\.\/|assets\/|data:|#[0-9a-f]{3,6}$|var\(|rgba?\(|translate|scale|M\d)/.test(t))return false;
  if(/[{};]/.test(t)&&/:\s*[^ ]+;/.test(t))return false; // css
  if(/^[A-Za-z_$][\w$]*$/.test(t)&&!/[åäöÅÄÖ]/.test(t)&&!/^[A-ZÅÄÖ][a-zåäö]+$/.test(t))return false;
  return true;
}
function add(raw,file){
  const parts=raw.split(/<[^>]*>/);
  // attributvärden
  for(const m of raw.matchAll(/(?:placeholder|title|aria-label|alt|data-tip)="([^"]+)"/g))parts.push(m[1]);
  for(let p of parts){p=dec(p).replace(/\s+/g,' ').trim();if(!isText(p)||bank.has(p))continue;if(!out.has(p))out.set(p,file);}
}
for(const f of ['app/assets/app-17bb85c3132c2bc2.js','app/assets/grind.js','app/assets/konto.js','app/assets/moln.js','app/assets/utvecklare.js','app/assets/skydd.js']){
  const src=fs.readFileSync(R+f,'utf8');
  const ast=acorn.parse(src,{ecmaVersion:'latest',sourceType:'script',allowHashBang:true});
  walk.full(ast,n=>{if(n.type==='Literal'&&typeof n.value==='string')add(n.value,f);else if(n.type==='TemplateElement')add(n.value.cooked||'',f);});
}
for(const f of ['app/app.html','index.html','app/index.html','integritet.html','om-sam.html']){
  if(!fs.existsSync(R+f))continue;
  let h=fs.readFileSync(R+f,'utf8').replace(/<script[\s\S]*?<\/script>/g,s=>{try{const ast=acorn.parse(s.replace(/^<script[^>]*>|<\/script>$/g,''),{ecmaVersion:'latest'});walk.full(ast,n=>{if(n.type==='Literal'&&typeof n.value==='string')add(n.value,f);else if(n.type==='TemplateElement')add(n.value.cooked||'',f)})}catch(e){}return ''}).replace(/<style[\s\S]*?<\/style>/g,'');
  add(h,f);
}
const arr=[...out.entries()];
fs.writeFileSync('strings.json',JSON.stringify(arr,null,1));
const by={};arr.forEach(([t,f])=>by[f]=(by[f]||0)+1);
console.log(arr.length,arr.reduce((s,[t])=>s+t.length,0),by);
