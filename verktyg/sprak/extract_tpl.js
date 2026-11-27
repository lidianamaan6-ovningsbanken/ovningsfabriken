const fs=require('fs'),acorn=require('acorn'),walk=require('acorn-walk');
const R='/home/user/ovningsfabriken/';
const out=new Map();
const dec=s=>s.replace(/&nbsp;/g,' ').replace(/&amp;/g,'&').replace(/&middot;/g,'·').replace(/&ndash;/g,'–').replace(/&hellip;/g,'…').replace(/&quot;/g,'"').replace(/&#39;/g,"'");
function flat(n,acc){ if(n.type==='BinaryExpression'&&n.operator==='+'){flat(n.left,acc);flat(n.right,acc);} else if(n.type==='Literal'&&typeof n.value==='string')acc.push(n.value); else if(n.type==='TemplateLiteral'){n.quasis.forEach((q,i)=>{acc.push(q.value.cooked||'');if(i<n.expressions.length)acc.push('\u0001')})} else acc.push('\u0001'); return acc;}
function handle(parts,file){
  const s=parts.join(''); if(!s.includes('\u0001'))return;
  // ta bort taggar men behåll uttryck som står i attribut utanför
  const noTags=s.replace(/<[^>]*>/g,'\u0002');
  for(let seg of noTags.split('\u0002')){
    seg=dec(seg).replace(/\s+/g,' ').trim();
    if(!seg.includes('\u0001'))continue;
    const lit=seg.replace(/\u0001/g,'');
    if(!/[a-zåäöA-ZÅÄÖ]{3}/.test(lit))continue;
    if(/^[\u0001\s]*$/.test(seg))continue;
    if(/[{};=]|=>|\(\)|^\.|^#/.test(lit)&&/[{};=]/.test(lit))continue;
    if(/^[a-z0-9_\-\u0001 .:#]+$/.test(seg)&&!/ [a-zåäö]{3,} /.test(seg))continue; // klassnamn
    const t=seg.replace(/\u0001+/g,'{}').replace(/\{\}\s*\{\}/g,'{}');
    if(t==='{}'||t.length>300)continue;
    if(!out.has(t))out.set(t,file);
  }
}
const seen=new WeakSet();
for(const f of ['app/assets/app-17bb85c3132c2bc2.js','app/assets/grind.js','app/assets/konto.js','app/assets/moln.js','app/assets/utvecklare.js']){
  const ast=acorn.parse(fs.readFileSync(R+f,'utf8'),{ecmaVersion:'latest'});
  walk.full(ast,n=>{
    if((n.type==='BinaryExpression'&&n.operator==='+')||n.type==='TemplateLiteral'){
      if(seen.has(n))return; 
      const acc=flat(n,[]); handle(acc,f);
    }
  });
}
const arr=[...out.keys()];
fs.writeFileSync('templates.json',JSON.stringify(arr,null,0));
console.log(arr.length);
console.log(arr.filter((_,i)=>i%25==0).slice(0,60).join('\n'));
