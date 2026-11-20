# Builds tools/speed-to-lead-calculator/index.html. Shell, head and CSS come from gen_tool_aicost.py
# (importing it also rebuilds the AI receptionist calculator and the tools hub).
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chrome
import gen_tool_aicost as A
U, ROOT = A.U, A.ROOT
SLUG = 'speed-to-lead-calculator'
url = f'{U}tools/{SLUG}/'
TITLE = 'Speed to Lead Calculator (Free) | Aftab Ahmed'
DESC = 'Free speed to lead calculator: see how many of your leads wait too long for a reply and what answering within 5 minutes could be worth to your business.'
HBR = 'https://hbr.org/2011/03/the-short-life-of-online-sales-leads'
FAQ = [
 ('What is speed to lead?',
  'Speed to lead is the time between a new lead reaching out (a form, call, text or ad inquiry) and your first real reply. The shorter it is, the more of those people you reach while they are still interested.'),
 ('How do you calculate lead response time?',
  'For each lead, subtract the time the inquiry came in from the time of your first reply. Add those times and divide by the number of leads for the average. Also look at the median and at the share of leads answered within 5 minutes, because a few very slow replies can hide behind a decent average.'),
 ('What is a good lead response time for a small business?',
  'Within 5 minutes is a common target, and the closer to instant the better. An automatic text that goes out in seconds, followed by a call from a person, is the most practical way for a small team to hit it every time, including evenings and weekends.'),
 ('How much revenue does slow lead response cost?',
  'Use the calculator above: it multiplies the leads you could move into the fast group by the difference between your close rate on fast and slow leads, then by your average job value. Use your own close rates from your CRM or a month of records, not a statistic from someone else.'),
 ('Are the numbers in the calculator real statistics?',
  'No. The starting values are examples so the math is easy to follow. Replace them with your own lead count, close rates and job value to get a number that means something for your business.')]
ld = {"@context": "https://schema.org", "@graph": [
  {"@type": "WebApplication", "name": "Speed to Lead Calculator", "url": url, "applicationCategory": "BusinessApplication", "operatingSystem": "Any",
   "isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "description": DESC, "author": A.person},
  {"@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": U},
    {"@type": "ListItem", "position": 2, "name": "Free tools", "item": f"{U}tools/"},
    {"@type": "ListItem", "position": 3, "name": "Speed to lead calculator", "item": url}]},
  {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}]}
CSS = A.CSS + '.ac__bar{height:12px;border-radius:9px;background:#2a2a2a;overflow:hidden;display:flex;margin:4px 0 2px}.ac__bar i{display:block;background:#4ade80}.ac__bar em{display:block;background:var(--red)}\n.ac__legend{display:flex;justify-content:space-between;gap:10px;font-size:13px;color:var(--muted)}\n'
rng = lambda i, lab, mn, mx, st, note='': f'<div class="ac__f"><label for="{i}">{lab} <b id="{i}V"></b></label><input type="range" id="{i}" min="{mn}" max="{mx}" step="{st}">{note}</div>'
faq_html = ''.join(f'  <h3>{q}</h3>\n  <p>{a}</p>\n' for q, a in FAQ)
page = A.head(TITLE, DESC, url, 'Speed to lead calculator: what slow replies cost you', f'{U}images/og/{SLUG}.png', ld, CSS, '../../') + f'''
<section class="hero"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="../../">Home</a><span>/</span><a href="../">Free tools</a><span>/</span>Speed to lead calculator</nav>
  <div class="kicker">Free tool · For US small businesses</div>
  <h1>Speed to lead calculator</h1>
  <p class="lead">How many of your leads wait too long for a reply, and what is that costing you? Enter your monthly leads, how fast you reply today and your close rates, and this free speed to lead calculator shows the extra customers and revenue from answering within 5 minutes.</p>
</div></section>

<article>
  <div class="ac" id="ac">
    <div class="ac__in">
      <div class="ac__f"><label for="slInd">Your industry</label>
        <select id="slInd">
          <option value="home">HVAC, plumbing &amp; home services</option>
          <option value="dental">Dental practice</option>
          <option value="law">Law firm</option>
          <option value="medspa">Med spa</option>
          <option value="realestate">Real estate</option>
          <option value="insurance">Insurance agency</option>
          <option value="other">Other service business</option>
        </select>
        <div class="ac__note">Sets example lead and job values. Replace them with your own.</div></div>
      {rng('slLeads', 'New leads per month', 5, 1000, 5)}
      <div class="ac__f"><label for="slNow">Your typical reply time today</label>
        <select id="slNow">
          <option value="" selected>Choose one to set an example</option>
          <option value="85">Under 5 minutes, almost always</option>
          <option value="35">5 to 30 minutes</option>
          <option value="15">30 minutes to 2 hours</option>
          <option value="5">Later the same day</option>
          <option value="2">Next day or later</option>
        </select>
        <div class="ac__note">Sets a rough example for the slider below. Use your real share if you know it.</div></div>
      {rng('slFast', 'Leads you reply to within 5 minutes now', 0, 100, 1)}
      {rng('slTarget', 'Leads replied to within 5 minutes after fixing it', 0, 100, 1, '<div class="ac__note">An automatic text in seconds plus a call from a person usually gets this above 90%.</div>')}
      <div class="ac__rates"><b>Your close rates and job value</b><div class="ac__note">Example values. Check a month of your own leads: how many fast replies and slow replies became customers?</div>
        <div class="ac__g">
          {A.num('slCf', 'Close rate, replied within 5 min (%)', 30, 1)}
          {A.num('slCs', 'Close rate, replied later (%)', 15, 1)}
          {A.num('slVal', 'Average job or customer value ($)', 1200, 50)}
        </div></div>
    </div>
    <div class="ac__out" aria-live="polite">
      <div class="ac__k">Extra revenue from faster replies</div>
      <div class="ac__big"><span id="slRev">$0</span><small id="slRevL">per month</small></div>
      <div>
        <div class="ac__bar" aria-hidden="true"><i id="slBarF"></i><em id="slBarS"></em></div>
        <div class="ac__legend"><span id="slLegF"></span><span id="slLegS"></span></div>
      </div>
      <div class="ac__rows">
        <div><span>Leads waiting over 5 minutes now</span><b id="slWait"></b></div>
        <div><span>Customers a month now</span><b id="slNowC"></b></div>
        <div class="best"><span>Customers a month after</span><b id="slAfterC"></b></div>
        <div><span>Extra revenue a year</span><b id="slYear"></b></div>
      </div>
      <div class="ac__for" id="slFor"></div>
      <div class="ac__btns"><a class="btn" href="../../#book" id="slBook">Fix my reply time on a free call →</a><button type="button" class="btn ac__ghost" id="slCopy">Copy link to this result</button></div>
      <form class="lead ac__lead" data-lead="tool-{SLUG}" data-ok="Thanks! I’ll email your result and a short plan within one business day.">
        <b style="color:#fff;font-size:15px">Email me this result and a plan</b>
        <input name="name" placeholder="First name" autocomplete="given-name" aria-label="First name">
        <input type="email" name="email" required placeholder="Email address" autocomplete="email" aria-label="Email address">
        <input name="website" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
        <button class="btn ac__ghost" type="submit">Send me a plan</button>
        <p class="lead__msg" aria-live="polite"></p>
      </form>
      <a href="../../demo/" style="color:var(--red-text);font-weight:700;font-size:14.5px">See an instant reply in the AI receptionist demo →</a>
    </div>
  </div>

  <h2 id="how">How do you calculate what speed to lead is worth?</h2>
  <p>Split your leads into two groups: the ones you reply to within 5 minutes and the ones who wait longer. Each group has its own close rate. The value of replying faster is the number of leads you move from the slow group to the fast group, times the difference in close rate, times what a customer is worth:</p>
  <p><strong>Extra customers = leads per month × (target fast share − current fast share) × (fast close rate − slow close rate)</strong>, and extra revenue = extra customers × average job value.</p>
  <p>A worked example with hypothetical numbers: 100 leads a month, 20% answered within 5 minutes today, a 30% close rate on fast replies and 15% on slow ones, and a $1,200 average job. Moving to 90% fast replies gives 100 × 0.70 × 0.15 = 10.5 extra customers a month, or about $12,600 in extra revenue a month. Your own close rates decide the answer, so measure them before you trust the number.</p>

  <h2 id="scenarios">What is faster lead response worth at different sizes?</h2>
  <p>Example scenarios using a 30% fast close rate, a 15% slow close rate, a $1,000 job value and a 90% target. These illustrate the math; they are not benchmarks:</p>
  <div class="tw"><table>
    <tr><th>Business</th><th>Leads a month</th><th>Fast today</th><th>Extra customers</th><th>Extra revenue a month</th></tr>
    <tr><td>Small, slow replies</td><td>30</td><td>20%</td><td>3.15</td><td>$3,150</td></tr>
    <tr><td>Steady, slow replies</td><td>100</td><td>20%</td><td>10.5</td><td>$10,500</td></tr>
    <tr><td>Steady, already fairly fast</td><td>100</td><td>60%</td><td>4.5</td><td>$4,500</td></tr>
    <tr><td>Busy, slow replies</td><td>300</td><td>20%</td><td>31.5</td><td>$31,500</td></tr>
  </table></div>
  <p>The gain is largest when you have many leads and few of them get a fast reply. If you already answer most leads quickly, the next step is usually better follow-up for the ones who don't answer, which my guide to <a href="../../blog/automated-lead-follow-up/">automated lead follow-up</a> covers.</p>

  <h2 id="measure">How do you measure your lead response time?</h2>
  <p>Take the last 20 to 30 leads. For each one, note when the inquiry arrived and when someone first replied, and subtract. Then count how many were answered within 5 minutes; that share goes in the calculator. Look at evenings and weekends separately, because that is where most small businesses lose speed. Research on online leads, such as the <a href="{HBR}" rel="noopener">Harvard Business Review study on the short life of online sales leads</a>, found that many companies take hours or longer to reply, which is why the share answered within minutes matters more than the average.</p>

  <h2 id="good">What is a good speed to lead?</h2>
  <ul>
    <li><strong>Under 1 minute:</strong> possible with an automatic text or AI reply. This is the realistic goal for every lead, at any hour.</li>
    <li><strong>Under 5 minutes:</strong> a strong result for a person replying by hand during business hours.</li>
    <li><strong>30 minutes or more:</strong> many leads have already contacted someone else or lost interest.</li>
    <li><strong>Next day:</strong> you are mostly reaching people who already booked elsewhere.</li>
  </ul>
  <p>My guide on <a href="../../blog/speed-to-lead/">why the first 5 minutes decide the sale</a> explains the reasons and what the first message should say. Any automated texts or calls need the customer's consent, and the FCC has confirmed that <a href="https://www.fcc.gov/document/fcc-makes-ai-generated-voices-robocalls-illegal" rel="noopener">AI-generated voices in robocalls fall under existing calling rules</a>.</p>

  <h2 id="industry">How does speed to lead differ by industry?</h2>
  <ul>
    <li><strong>Home services:</strong> urgent jobs go to whoever answers first, often after hours. See <a href="../../industries/home-services/">automation for home service businesses</a>.</li>
    <li><strong>Dental and med spas:</strong> new patients often inquire in the evening and book wherever replies first. See <a href="../../industries/dental/">dental practices</a> and <a href="../../industries/med-spa/">med spas</a>.</li>
    <li><strong>Law firms:</strong> people with a legal problem often contact several firms at once, so the first callback has a real advantage. See <a href="../../industries/law/">law firms</a>.</li>
    <li><strong>Real estate and insurance:</strong> online leads from portals and quote forms go to several agents, so seconds matter. See <a href="../../industries/real-estate/">real estate</a> and <a href="../../industries/insurance/">insurance agencies</a>.</li>
  </ul>
  <p>If your phone is where leads wait longest, the <a href="../missed-call-calculator/">missed call cost calculator</a> estimates that side. The <a href="../../solutions/lead-follow-up/">slow follow-up solution</a> shows how I set up instant replies and follow-up as one system.</p>

  <h2 id="faq">FAQ</h2>
{faq_html}
  <div class="sources"><b>Sources and further reading</b><ul>
    <li><a href="{HBR}" rel="noopener">Harvard Business Review: The Short Life of Online Sales Leads (Oldroyd, McElheran and Elkington, 2011)</a></li>
    <li><a href="https://www.fcc.gov/document/fcc-makes-ai-generated-voices-robocalls-illegal" rel="noopener">FCC: AI-generated voices in robocalls</a></li>
  </ul></div>

  <div class="related"><b>Related tools and guides</b><ul>
    <li><a href="../missed-call-calculator/">Missed call cost calculator</a></li>
    <li><a href="../ai-receptionist-cost-calculator/">AI receptionist cost calculator</a></li>
    <li><a href="../../blog/speed-to-lead/">Speed to lead: why the first 5 minutes decide the sale</a></li>
    <li><a href="../../blog/automated-lead-follow-up/">How to follow up with leads automatically</a></li>
    <li><a href="../../services/lead-generation/">Lead generation systems</a></li>
    <li><a href="../">All free tools</a></li>
  </ul></div>

  <div class="cta">
    <h2>Want every lead answered in seconds?</h2>
    <p>Book a free 30-minute call. Bring your numbers and I'll show you how to reply to every lead instantly, day and night.</p>
    <a class="btn" href="../../#book">Book a free call →</a>
  </div>
</article>

{chrome.footer('../../')}
<script>
(function(){{
  // Example values per industry (not statistics): leads a month, average job value
  var P={{home:[80,1200],dental:[60,1500],law:[40,4000],medspa:[70,600],realestate:[50,6000],insurance:[60,900],other:[60,1000]}};
  var $=function(i){{return document.getElementById(i)}},R=['slLeads','slFast','slTarget'],N=['slCf','slCs','slVal'];
  var KEY={{slLeads:'leads',slFast:'fast',slTarget:'target',slCf:'cf',slCs:'cs',slVal:'value'}};
  var money=function(n){{return '$'+Math.round(n).toLocaleString('en-US')}},v=function(i){{var x=parseFloat($(i).value);return isFinite(x)&&x>=0?x:0}},used=false;
  var one=function(n){{return (Math.round(n*10)/10).toLocaleString('en-US')}};
  function update(){{
    R.forEach(function(i){{var r=$(i);r.style.setProperty('--p',(r.value-r.min)/(r.max-r.min)*100+'%')}});
    var L=v('slLeads'),f=Math.min(v('slFast'),100)/100,t=Math.min(v('slTarget'),100)/100,cf=v('slCf')/100,cs=v('slCs')/100,val=v('slVal');
    $('slLeadsV').textContent=L.toLocaleString('en-US');$('slFastV').textContent=Math.round(f*100)+'%';$('slTargetV').textContent=Math.round(t*100)+'%';
    var now=L*(f*cf+(1-f)*cs),after=L*(t*cf+(1-t)*cs),extra=after-now,rev=extra*val;
    $('slRev').textContent=(rev<0?'−':'')+money(Math.abs(rev));$('slRevL').textContent='per month · '+one(extra)+' extra customers';
    $('slBarF').style.width=f*100+'%';$('slBarS').style.width=(1-f)*100+'%';
    $('slLegF').textContent=Math.round(L*f).toLocaleString('en-US')+' replied within 5 min';$('slLegS').textContent=Math.round(L*(1-f)).toLocaleString('en-US')+' waited longer';
    $('slWait').textContent=Math.round(L*(1-f)).toLocaleString('en-US')+' a month';$('slNowC').textContent=one(now);$('slAfterC').textContent=one(after);$('slYear').textContent=(rev<0?'−':'')+money(Math.abs(rev)*12);
    $('slFor').textContent=L.toLocaleString('en-US')+' leads × ('+Math.round(t*100)+'% − '+Math.round(f*100)+'%) × ('+Math.round(cf*100)+'% − '+Math.round(cs*100)+'%) = '+one(extra)+' extra customers × '+money(val)+' = '+money(rev)+' a month.'+(t<=f?' Set the target above your current share to see the gain.':'');
  }}
  function touch(){{if(!used){{used=true;(window.dataLayer=window.dataLayer||[]).push({{event:'tool_used',tool:'{SLUG}'}})}}update()}}
  function link(){{var q=R.concat(N).map(function(i){{return KEY[i]+'='+encodeURIComponent($(i).value)}}).join('&');return location.origin+location.pathname+'?'+q}}
  $('slInd').addEventListener('change',function(e){{var p=P[e.target.value];$('slLeads').value=p[0];$('slVal').value=p[1];touch()}});
  $('slNow').addEventListener('change',function(e){{if(e.target.value){{$('slFast').value=e.target.value;touch()}}}});
  R.concat(N).forEach(function(i){{$(i).addEventListener('input',touch)}});
  $('slCopy').addEventListener('click',function(){{var b=this,u=link(),done=function(){{b.textContent='Link copied';setTimeout(function(){{b.textContent='Copy link to this result'}},1800)}};
    (window.dataLayer=window.dataLayer||[]).push({{event:'tool_result_shared',tool:'{SLUG}'}});
    if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(u).then(done,function(){{prompt('Copy this link',u)}});else prompt('Copy this link',u)}});
  $('slBook').addEventListener('click',function(){{(window.dataLayer=window.dataLayer||[]).push({{event:'calculator_cta',tool:'{SLUG}',extra:$('slRev').textContent}})}});
  var lf=document.querySelector('.ac__lead');if(lf)lf.leadExtra=function(){{return 'Industry: '+$('slInd').selectedOptions[0].text+'; leads/mo '+$('slLeads').value+'; reply today: '+$('slNow').selectedOptions[0].text+'; fast now '+$('slFast').value+'%; target '+$('slTarget').value+'%; close fast '+$('slCf').value+'%, slow '+$('slCs').value+'%; job value $'+$('slVal').value+'; extra '+$('slRev').textContent+' '+$('slRevL').textContent}};
  // defaults, then any values shared in the link (?leads=100&fast=20 ...)
  $('slLeads').value=100;$('slFast').value=20;$('slTarget').value=90;
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
print('built', SLUG, len(TITLE), len(DESC))
