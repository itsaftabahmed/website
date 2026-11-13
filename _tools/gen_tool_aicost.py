# Builds tools/ai-receptionist-cost-calculator/index.html and tools/index.html (the Free tools hub).
# Head tracking codes and page shell come from the missed call calculator; header/footer come from chrome.py.
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chrome
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U = 'https://iamaftabahmed.com/'
tpl = open(f'{ROOT}/tools/missed-call-calculator/index.html').read()
track = tpl[tpl.index('<head>') + 6:tpl.index('<title>')]
body_track = tpl[tpl.index('<body>') + 6:re.search(r'<div class="ann">|<header', tpl).start()]
icon = re.search(r'<link rel="icon"[^>]*>', tpl).group(0)
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,500..900&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap">')
person = {"@type": "Person", "@id": f"{U}#person", "name": "Aftab Ahmed", "url": f"{U}about/"}

def head(title, desc, url, og_title, img, ld, css, up):
    return f'''<!doctype html>
<html lang="en">
<head>{track}<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="Aftab Ahmed">
<meta name="theme-color" content="#0A0A0A">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Aftab Ahmed">
<meta property="og:locale" content="en_US">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{img}">
{icon}
{FONTS}
<link rel="stylesheet" href="{up}blog/blog.css">
<style>
{css}</style>
<script type="application/ld+json">
{json.dumps(ld)}
</script>
</head>
<body>{body_track}{chrome.nav(up)}
'''

# ---------------------------------------------------------------- calculator
SLUG = 'ai-receptionist-cost-calculator'
url = f'{U}tools/{SLUG}/'
TITLE = 'AI Receptionist Cost Calculator (Free) | Aftab Ahmed'
DESC = 'Free AI receptionist cost calculator: enter your monthly calls and call length to compare flat, per-minute, per-call and bundle pricing for a small business.'
FAQ = [
 ('How much does an AI receptionist cost per month?',
  'Self-serve plans commonly run from about $30 to $300 a month, and done-for-you setups usually cost a few hundred dollars a month. The real figure depends on how many minutes or calls you use, so enter your own volume in the calculator above.'),
 ('How do I calculate my AI receptionist cost?',
  'Multiply your monthly calls by your average call length to get minutes. Then price those minutes on each billing model: a flat fee, minutes times the per-minute rate, calls times the per-call rate, or a bundle price plus overage for minutes beyond the bundle. Add any monthly extras.'),
 ('Is per-minute or flat-rate pricing cheaper for an AI receptionist?',
  'It depends on volume. Per-minute billing is usually cheaper at low volume or with short calls, and a flat plan is usually cheaper once you pass a few hundred minutes a month. The calculator shows the point where they cross for your numbers.'),
 ('What hidden fees should I add to the estimate?',
  'Common extras are setup or onboarding, additional phone numbers, text messages, calendar or CRM connections, call transfers and overage rates. Ask each provider for these in writing and add the monthly ones to the extras field.'),
 ('Are the rates in the calculator real vendor prices?',
  'No. The starting rates are example values so the math is easy to follow. Replace them with the rates from the plans you are comparing.')]
ld = {"@context": "https://schema.org", "@graph": [
  {"@type": "WebApplication", "name": "AI Receptionist Cost Calculator", "url": url, "applicationCategory": "BusinessApplication", "operatingSystem": "Any",
   "isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "description": DESC, "author": person},
  {"@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": U},
    {"@type": "ListItem", "position": 2, "name": "Free tools", "item": f"{U}tools/"},
    {"@type": "ListItem", "position": 3, "name": "AI receptionist cost calculator", "item": url}]},
  {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}]}
CSS = '''.ac{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:22px;margin:8px 0 34px}
.ac__in,.ac__out{background:var(--surface);border:1px solid var(--line);border-radius:22px;padding:26px}
.ac__f{margin-bottom:20px}.ac__f label{display:flex;justify-content:space-between;gap:12px;font-size:15px;color:var(--soft);margin-bottom:10px}.ac__f label b{color:#fff;white-space:nowrap}
.ac select,.ac input[type=number]{width:100%;padding:12px 14px;border-radius:12px;background:#0d0d0d;color:#fff;border:1px solid #333;font:inherit;font-size:15px}
.ac input[type=number]:focus,.ac select:focus{outline:none;border-color:var(--red)}
.ac input[type=range]{-webkit-appearance:none;appearance:none;width:100%;height:6px;border-radius:9px;background:linear-gradient(90deg,var(--red) var(--p,40%),#333 var(--p,40%));outline:none}
.ac input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:22px;height:22px;border-radius:50%;background:#fff;border:4px solid var(--red);cursor:grab}
.ac input[type=range]::-moz-range-thumb{width:14px;height:14px;border-radius:50%;background:#fff;border:4px solid var(--red);cursor:grab}
.ac__note{color:var(--muted);font-size:13px;margin-top:6px}
.ac__rates{border-top:1px solid var(--line);margin-top:6px;padding-top:18px}.ac__rates>b{display:block;font-size:15px;margin-bottom:4px}
.ac__g{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:12px}.ac__g label{display:block;font-size:13px;color:var(--muted);margin-bottom:6px}
.ac__out{display:flex;flex-direction:column;gap:14px;position:sticky;top:90px;align-self:start}
.ac__k{color:var(--red-text);font-weight:800;letter-spacing:.14em;font-size:12px;text-transform:uppercase}
.ac__big{font-family:var(--display);font-stretch:115%;font-weight:900;font-size:clamp(38px,4.6vw,52px);color:#ff2a33;letter-spacing:-.03em;line-height:1.05}
.ac__big small{display:block;font-family:'Plus Jakarta Sans',sans-serif;font-stretch:100%;font-size:15px;font-weight:600;color:var(--muted);letter-spacing:0;margin-top:6px}
.ac__rows div{display:flex;justify-content:space-between;gap:12px;padding:10px 12px;border-top:1px solid var(--line);font-size:15px;color:var(--soft)}
.ac__rows b{color:#fff}.ac__rows .best{background:rgba(74,222,128,.08);border:1px solid rgba(74,222,128,.3);border-radius:12px}.ac__rows .best b{color:#4ade80}
.ac__rows .best span::after{content:"Lowest";margin-left:8px;font-size:11px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#4ade80}
.ac__for{color:var(--muted);font-size:13px;line-height:1.5}
.ac__busy{background:rgba(224,17,25,.08);border:1px solid rgba(224,17,25,.35);border-radius:16px;padding:14px 16px;font-size:14.5px;color:var(--soft)}.ac__busy b{color:#fff}
.ac__btns{display:flex;flex-wrap:wrap;gap:10px}.ac__btns .btn{padding:12px 18px;font-size:14.5px}
.ac__ghost{background:none!important;border:1px solid #3a3a3a!important;box-shadow:none!important;color:#fff;cursor:pointer;font-family:inherit;font-weight:700;border-radius:999px}
.ac__lead{margin-top:2px;padding-top:16px;border-top:1px solid var(--line)}
article table{width:100%;border-collapse:collapse;margin:18px 0;font-size:15.5px}article th,article td{text-align:left;padding:11px 12px;border-bottom:1px solid var(--line)}article th{color:var(--muted);font-size:12.5px;letter-spacing:.08em;text-transform:uppercase}
.tw{overflow-x:auto}
@media (max-width:760px){.ac{grid-template-columns:1fr}.ac__out{position:static}}
'''
num = lambda i, lab, v, step, mn='0': f'<div><label for="{i}">{lab}</label><input type="number" id="{i}" value="{v}" min="{mn}" step="{step}" inputmode="decimal"></div>'
faq_html = ''.join(f'  <h3>{q}</h3>\n  <p>{a}</p>\n' for q, a in FAQ)
page = head(TITLE, DESC, url, 'AI receptionist cost calculator: compare 4 pricing models', f'{U}images/og/{SLUG}.png', ld, CSS, '../../') + f'''
<section class="hero"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="../../">Home</a><span>/</span><a href="../">Free tools</a><span>/</span>AI receptionist cost calculator</nav>
  <div class="kicker">Free tool · For US small businesses</div>
  <h1>AI receptionist cost calculator</h1>
  <p class="lead">What will an AI receptionist cost your business each month? Enter your calls and average call length, and this free calculator prices them on the four ways AI receptionists are billed, so you can see which plan type is cheapest for you.</p>
</div></section>

<article>
  <div class="ac" id="ac">
    <div class="ac__in">
      <div class="ac__f"><label for="acInd">Your industry</label>
        <select id="acInd">
          <option value="home">HVAC, plumbing &amp; home services</option>
          <option value="dental">Dental practice</option>
          <option value="law">Law firm</option>
          <option value="medspa">Med spa</option>
          <option value="realestate">Real estate</option>
          <option value="insurance">Insurance agency</option>
          <option value="other">Other service business</option>
        </select>
        <div class="ac__note">Sets example call numbers. Replace them with your own.</div></div>
      <div class="ac__f"><label for="acCalls">Calls per month <b id="acCallsV"></b></label><input type="range" id="acCalls" min="20" max="2000" step="10"></div>
      <div class="ac__f"><label for="acMins">Average call length <b id="acMinsV"></b></label><input type="range" id="acMins" min="0.5" max="8" step="0.5"></div>
      <div class="ac__f"><label for="acShare">Share of calls the AI answers <b id="acShareV"></b></label><input type="range" id="acShare" min="10" max="100" step="5"><div class="ac__note">100% for every call. Lower it for after-hours or overflow only.</div></div>
      <div class="ac__f"><label for="acBusy">Your busiest month is higher by <b id="acBusyV"></b></label><input type="range" id="acBusy" min="0" max="100" step="5"></div>
      <div class="ac__rates"><b>Plan rates to compare</b><div class="ac__note">Example values, not vendor prices. Type in the rates from the plans you are considering.</div>
        <div class="ac__g">
          {num('acFlat', 'Flat plan ($ a month)', 150, 1)}
          {num('acPm', 'Per-minute rate ($)', 0.40, 0.01)}
          {num('acPc', 'Per-call rate ($)', 1.50, 0.05)}
          {num('acBp', 'Bundle price ($ a month)', 99, 1)}
          {num('acBm', 'Minutes in the bundle', 200, 10)}
          {num('acBo', 'Overage rate ($ a minute)', 0.50, 0.01)}
          {num('acExtra', 'Monthly extras ($): numbers, texts, add-ons', 0, 1)}
          {num('acSetup', 'One-time setup fee ($)', 0, 10)}
        </div></div>
    </div>
    <div class="ac__out" aria-live="polite">
      <div class="ac__k">Lowest estimated cost</div>
      <div class="ac__big"><span id="acBest">$0</span><small id="acBestL">per month</small></div>
      <div class="ac__rows">
        <div id="acR0"><span>Flat monthly</span><b></b></div>
        <div id="acR1"><span>Per minute</span><b></b></div>
        <div id="acR2"><span>Per call</span><b></b></div>
        <div id="acR3"><span>Bundle + overage</span><b></b></div>
      </div>
      <div class="ac__for" id="acFor"></div>
      <div class="ac__busy" id="acBusyOut"></div>
      <div class="ac__btns"><a class="btn" href="../../#book" id="acBook">Get a real quote on a free call →</a><button type="button" class="btn ac__ghost" id="acCopy">Copy link to this result</button></div>
      <form class="lead ac__lead" data-lead="tool-{SLUG}" data-ok="Thanks! I’ll email your result and a short plan within one business day.">
        <b style="color:#fff;font-size:15px">Email me this result and a plan</b>
        <input name="name" placeholder="First name" autocomplete="given-name" aria-label="First name">
        <input type="email" name="email" required placeholder="Email address" autocomplete="email" aria-label="Email address">
        <input name="website" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
        <button class="btn ac__ghost" type="submit">Send me a plan</button>
        <p class="lead__msg" aria-live="polite"></p>
      </form>
      <a href="../../demo/" style="color:var(--red-text);font-weight:700;font-size:14.5px">Or try the AI receptionist demo →</a>
    </div>
  </div>

  <h2 id="how">How do you calculate AI receptionist cost?</h2>
  <p>Start with minutes: <strong>calls per month × average call length × the share of calls the AI answers</strong>. Then price those minutes on each of the four billing models:</p>
  <ul>
    <li><strong>Flat monthly:</strong> the plan price, whatever the volume (many flat plans have a fair-use limit, so check it).</li>
    <li><strong>Per minute:</strong> minutes × the per-minute rate.</li>
    <li><strong>Per call:</strong> answered calls × the per-call rate.</li>
    <li><strong>Bundle plus overage:</strong> the bundle price, plus (minutes beyond the bundle × the overage rate).</li>
  </ul>
  <p>Add monthly extras to each. A worked example with hypothetical rates: 300 calls at 2 minutes is 600 minutes. A $150 flat plan costs $150. At $0.40 a minute it costs $240. At $1.50 a call it costs $450. A $99 bundle with 200 minutes and $0.50 overage costs $99 + (400 × $0.50) = $299. The plan with the lowest advertised price is not the cheapest one here.</p>

  <h2 id="scenarios">What does an AI receptionist cost at different call volumes?</h2>
  <p>The same example rates, at three volumes with 2-minute calls. These are illustrations of the math, not quotes:</p>
  <div class="tw"><table>
    <tr><th>Calls a month</th><th>Flat $150</th><th>$0.40 a minute</th><th>$1.50 a call</th><th>$99 bundle</th><th>Lowest</th></tr>
    <tr><td>60 (quiet)</td><td>$150</td><td>$48</td><td>$90</td><td>$99</td><td>Per minute</td></tr>
    <tr><td>300 (steady)</td><td>$150</td><td>$240</td><td>$450</td><td>$299</td><td>Flat</td></tr>
    <tr><td>1,000 (busy)</td><td>$150</td><td>$800</td><td>$1,500</td><td>$999</td><td>Flat</td></tr>
  </table></div>
  <p>Low volume favors paying per minute. Once the phone is busy, a flat plan usually wins, which is why you should always price your busiest month before you choose. For typical market ranges and the extras to ask about, read <a href="../../blog/ai-receptionist-cost/">how much an AI receptionist costs</a>.</p>

  <h2 id="industry">How does the cost change by industry?</h2>
  <p>Call length and call timing matter more than the industry name, but they follow patterns:</p>
  <ul>
    <li><strong>Home services:</strong> short, urgent calls, many after hours. Per-minute bills stay low per call but spike in peak season. See <a href="../../industries/home-services/">automation for home service businesses</a>.</li>
    <li><strong>Dental and medical:</strong> steady daytime volume with scheduling questions. If the assistant handles patient information, the vendor needs to sign a business associate agreement; <a href="https://www.hhs.gov/hipaa/for-professionals/covered-entities/sample-business-associate-agreement-provisions/index.html" rel="noopener">HHS explains what that covers</a>. See <a href="../../industries/dental/">automation for dental practices</a>.</li>
    <li><strong>Law firms:</strong> fewer but longer intake calls, so per-minute and per-call plans behave very differently. See <a href="../../industries/law/">automation for law firms</a>.</li>
    <li><strong>Med spas:</strong> booking and pricing questions, often in the evening. See <a href="../../industries/med-spa/">automation for med spas</a>.</li>
  </ul>

  <h2 id="worth">Is an AI receptionist worth the cost?</h2>
  <p>Compare the monthly figure above with what unanswered calls cost you now. The <a href="../missed-call-calculator/">missed call cost calculator</a> estimates that side. For scale, the U.S. Bureau of Labor Statistics lists the <a href="https://www.bls.gov/ooh/office-and-administrative-support/receptionists.htm" rel="noopener">median pay for receptionists</a> at $18.27 an hour as of May 2025, before taxes and benefits. An AI receptionist does a narrower job than a person, so most businesses use it for overflow and after-hours calls. My guide to <a href="../../blog/ai-receptionist-vs-answering-service/">AI receptionist vs answering service</a> covers the trade-offs, and <a href="../../solutions/missed-calls/">the missed calls solution</a> shows how I set it up, including the calendar connection and follow-up, through my <a href="../../services/ai-automation/">AI automation service</a>.</p>

  <h2 id="faq">FAQ</h2>
{faq_html}
  <div class="sources"><b>Sources and further reading</b><ul>
    <li><a href="https://www.bls.gov/ooh/office-and-administrative-support/receptionists.htm" rel="noopener">U.S. Bureau of Labor Statistics: Receptionists, Occupational Outlook Handbook</a></li>
    <li><a href="https://www.hhs.gov/hipaa/for-professionals/covered-entities/sample-business-associate-agreement-provisions/index.html" rel="noopener">HHS: Business associate contracts</a></li>
  </ul></div>

  <div class="related"><b>Related tools and guides</b><ul>
    <li><a href="../missed-call-calculator/">Missed call cost calculator</a></li>
    <li><a href="../../demo/">Try the AI receptionist live demo</a></li>
    <li><a href="../../blog/ai-receptionist-cost/">How much does an AI receptionist cost? Pricing explained</a></li>
    <li><a href="../../blog/ai-receptionist-small-business/">AI receptionists: answering calls and booking appointments 24/7</a></li>
    <li><a href="../">All free tools</a></li>
  </ul></div>

  <div class="cta">
    <h2>Want a real number for your business?</h2>
    <p>Book a free 30-minute call. Bring last month's call count and I'll show you what an AI receptionist would cost and what it would save.</p>
    <a class="btn" href="../../#book">Book a free call →</a>
  </div>
</article>

{chrome.footer('../../')}
<script>
(function(){{
  // Example call numbers per industry (not statistics): calls a month, average minutes
  var P={{home:[300,2],dental:[450,2.5],law:[160,4],medspa:[220,2.5],realestate:[140,3],insurance:[200,3],other:[250,2]}};
  var $=function(i){{return document.getElementById(i)}},R=['acCalls','acMins','acShare','acBusy'],N=['acFlat','acPm','acPc','acBp','acBm','acBo','acExtra','acSetup'];
  var KEY={{acCalls:'calls',acMins:'mins',acShare:'share',acBusy:'busy',acFlat:'flat',acPm:'pm',acPc:'pc',acBp:'bp',acBm:'bm',acBo:'bo',acExtra:'extra',acSetup:'setup'}};
  var money=function(n){{return '$'+Math.round(n).toLocaleString('en-US')}},v=function(i){{var x=parseFloat($(i).value);return isFinite(x)&&x>=0?x:0}},used=false;
  var NAMES=['a flat monthly plan','per-minute billing','per-call billing','a bundle with overage'];
  function costs(calls,mins){{var m=calls*mins;return [v('acFlat'),m*v('acPm'),calls*v('acPc'),v('acBp')+Math.max(0,m-v('acBm'))*v('acBo')].map(function(c){{return c+v('acExtra')}})}}
  function low(a){{var k=0;a.forEach(function(c,i){{if(c<a[k])k=i}});return k}}
  function update(){{
    R.forEach(function(i){{var r=$(i);r.style.setProperty('--p',(r.value-r.min)/(r.max-r.min)*100+'%')}});
    var calls=v('acCalls')*v('acShare')/100,mins=v('acMins'),busy=1+v('acBusy')/100;
    $('acCallsV').textContent=v('acCalls').toLocaleString('en-US');$('acMinsV').textContent=mins+' min';$('acShareV').textContent=v('acShare')+'%';$('acBusyV').textContent=v('acBusy')+'%';
    var c=costs(calls,mins),k=low(c),cb=costs(calls*busy,mins),kb=low(cb);
    c.forEach(function(x,i){{var row=$('acR'+i);row.querySelector('b').textContent=money(x)+' / mo';row.classList.toggle('best',i===k)}});
    $('acBest').textContent=money(c[k]);$('acBestL').textContent='per month on '+NAMES[k]+(calls?' · about $'+(c[k]/calls).toFixed(2)+' a call':'');
    $('acFor').textContent=Math.round(calls).toLocaleString('en-US')+' answered calls × '+mins+' min = '+Math.round(calls*mins).toLocaleString('en-US')+' minutes a month. First year on the lowest option: '+money(c[k]*12+v('acSetup'))+(v('acSetup')?' including setup':'')+'.';
    $('acBusyOut').innerHTML=v('acBusy')?('In your busiest month ('+Math.round(calls*busy).toLocaleString('en-US')+' calls) the lowest option is <b>'+NAMES[kb]+'</b> at <b>'+money(cb[kb])+'</b>.'+(kb!==k?' That is a different plan type than a normal month, so check both.':'')):'Set a busiest-month increase above to see whether the cheapest plan type changes.';
  }}
  function touch(){{if(!used){{used=true;(window.dataLayer=window.dataLayer||[]).push({{event:'tool_used',tool:'{SLUG}'}})}}update()}}
  function link(){{var q=R.concat(N).map(function(i){{return KEY[i]+'='+encodeURIComponent($(i).value)}}).join('&');return location.origin+location.pathname+'?'+q}}
  $('acInd').addEventListener('change',function(e){{var p=P[e.target.value];$('acCalls').value=p[0];$('acMins').value=p[1];touch()}});
  R.concat(N).forEach(function(i){{$(i).addEventListener('input',touch)}});
  $('acCopy').addEventListener('click',function(){{var b=this,u=link(),done=function(){{b.textContent='Link copied';setTimeout(function(){{b.textContent='Copy link to this result'}},1800)}};
    (window.dataLayer=window.dataLayer||[]).push({{event:'tool_result_shared',tool:'{SLUG}'}});
    if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(u).then(done,function(){{prompt('Copy this link',u)}});else prompt('Copy this link',u)}});
  $('acBook').addEventListener('click',function(){{(window.dataLayer=window.dataLayer||[]).push({{event:'calculator_cta',tool:'{SLUG}',lowest:$('acBest').textContent}})}});
  var lf=document.querySelector('.ac__lead');if(lf)lf.leadExtra=function(){{return 'Industry: '+$('acInd').selectedOptions[0].text+'; calls/mo '+$('acCalls').value+'; avg min '+$('acMins').value+'; AI share '+$('acShare').value+'%; busy +'+$('acBusy').value+'%; lowest '+$('acBest').textContent+' '+$('acBestL').textContent+'; rates flat '+$('acFlat').value+', /min '+$('acPm').value+', /call '+$('acPc').value+', bundle '+$('acBp').value+'/'+$('acBm').value+'min/'+$('acBo').value}};
  // defaults, then any values shared in the link (?calls=300&mins=2 ...)
  $('acCalls').value=300;$('acMins').value=2;$('acShare').value=100;$('acBusy').value=30;
  var q=new URLSearchParams(location.search);Object.keys(KEY).forEach(function(i){{var x=parseFloat(q.get(KEY[i]));if(isFinite(x)&&x>=0)$(i).value=x}});
  update();
}})();
</script>
<script src="../../blog/lead.js" defer></script>
</body>
</html>
'''
os.makedirs(f'{ROOT}/tools/{SLUG}', exist_ok=True)
open(f'{ROOT}/tools/{SLUG}/index.html', 'w').write(page)

# ---------------------------------------------------------------- tools hub
# Newest first. Add a tuple here when a new tool launches, then rerun this script.
TOOLS = [
 (f'{SLUG}/', 'Calculator · New', 'AI receptionist cost calculator', 'Enter your calls and call length to compare flat, per-minute, per-call and bundle pricing.', 'Open the calculator →'),
 ('missed-call-calculator/', 'Calculator', 'Missed call cost calculator', 'See how much revenue unanswered calls cost you each month, and what a fast reply could win back.', 'Open the calculator →'),
 ('../demo/', 'Live demo', 'AI receptionist demo', 'Chat with an example AI receptionist for a dental office, HVAC company, law firm and more.', 'Try the demo →')]
hub_url = f'{U}tools/'
HT = 'Free Tools for Service Businesses | Aftab Ahmed'
HD = 'Free tools for small service businesses: AI receptionist cost calculator, missed call cost calculator and a live AI receptionist demo. No sign-up needed.'
hub_ld = {"@context": "https://schema.org", "@graph": [
  {"@type": "CollectionPage", "name": "Free tools for service businesses", "url": hub_url, "description": HD, "author": person},
  {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": U}, {"@type": "ListItem", "position": 2, "name": "Free tools", "item": hub_url}]},
  {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": t[2], "url": hub_url + t[0] if not t[0].startswith('..') else U + t[0][3:]} for i, t in enumerate(TOOLS)]}]}
cards = ''.join(f'''  <a class="card" href="{h}">
    <div class="kicker">{k}</div>
    <h2>{n}</h2>
    <p>{d}</p>
    <span>{c}</span>
  </a>
''' for h, k, n, d, c in TOOLS)
hub = head(HT, HD, hub_url, 'Free tools for service businesses', f'{U}images/og/{SLUG}.png', hub_ld, '.cards{padding-bottom:20px}\n', '../') + f'''
<section class="hero"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="../">Home</a><span>/</span>Free tools</nav>
  <div class="kicker">Free tools</div>
  <h1>Free tools for service businesses</h1>
  <p class="lead">Calculators and demos that show what missed calls, slow replies and busywork cost, and what fixing them is worth. Free to use, no sign-up. A new tool is added every week.</p>
</div></section>

<main class="wrap"><div class="cards">
{cards}</div>
<div class="cta" style="margin-top:30px">
  <h2>Want the numbers looked at for you?</h2>
  <p>Book a free 30-minute call and bring your results. I'll show you what would make the biggest difference first.</p>
  <a class="btn" href="../#book">Book a free call →</a>
</div>
</main>

{chrome.footer('../')}
</body>
</html>
'''
open(f'{ROOT}/tools/index.html', 'w').write(hub)
print('built', SLUG, 'and tools hub', len(TITLE), len(DESC), len(HT), len(HD))
