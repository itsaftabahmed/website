# Builds tools/no-show-cost-calculator/index.html. Shell, head and CSS come from gen_tool_aicost.py
# (importing it also rebuilds the AI receptionist calculator and the tools hub).
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chrome
import gen_tool_aicost as A
U, ROOT = A.U, A.ROOT
SLUG = 'no-show-cost-calculator'
url = f'{U}tools/{SLUG}/'
TITLE = 'No-Show Cost Calculator (Free) | Aftab Ahmed'
DESC = 'Free no-show cost calculator: see what missed appointments cost your practice or service business each month and year, and what cutting no-shows is worth.'
FAQ = [
 ('How do you calculate the cost of no-shows?',
  'Multiply your booked appointments per month by your no-show rate to get missed appointments, then multiply by the average value of a visit. Subtract the share of no-shows that rebook and still come in later, because that revenue is delayed rather than lost. Multiply by 12 for the yearly cost.'),
 ('How do you calculate a no-show rate?',
  'Divide the number of no-shows by the number of booked appointments in the same period and multiply by 100. Count every booked appointment, not only completed ones, and count late cancellations separately if you can refill those slots.'),
 ('What is a good no-show rate?',
  'There is no single benchmark, because no-show rates vary widely by industry, booking lead time and patient or customer type. The useful target is your own rate going down month after month; track it monthly and compare it after you add reminders, confirmations or deposits.'),
 ('How can a business reduce no-shows?',
  'The most practical steps are a confirmation at booking, reminders by text before the visit, a two-way reply so people can confirm or reschedule in one tap, a waitlist to refill empty slots, and deposits for long or high-value appointments where that fits your business.'),
 ('Are the numbers in the calculator real statistics?',
  'No. The starting values are examples so the math is easy to follow. Replace them with your own appointment count, no-show rate and visit value from your scheduling software.')]
ld = {"@context": "https://schema.org", "@graph": [
  {"@type": "WebApplication", "name": "No-Show Cost Calculator", "url": url, "applicationCategory": "BusinessApplication", "operatingSystem": "Any",
   "isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "description": DESC, "author": A.person},
  {"@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": U},
    {"@type": "ListItem", "position": 2, "name": "Free tools", "item": f"{U}tools/"},
    {"@type": "ListItem", "position": 3, "name": "No-show cost calculator", "item": url}]},
  {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}]}
CSS = A.CSS
rng = lambda i, lab, mn, mx, st, note='': f'<div class="ac__f"><label for="{i}">{lab} <b id="{i}V"></b></label><input type="range" id="{i}" min="{mn}" max="{mx}" step="{st}">{note}</div>'
faq_html = ''.join(f'  <h3>{q}</h3>\n  <p>{a}</p>\n' for q, a in FAQ)
page = A.head(TITLE, DESC, url, 'No-show cost calculator: what missed appointments cost you', f'{U}images/og/{SLUG}.png', ld, CSS, '../../') + f'''
<section class="hero"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="../../">Home</a><span>/</span><a href="../">Free tools</a><span>/</span>No-show cost calculator</nav>
  <div class="kicker">Free tool · For US practices and service businesses</div>
  <h1>No-show cost calculator</h1>
  <p class="lead">What do missed appointments cost your business? Enter your weekly appointments, your no-show rate and what a visit is worth, and this free no-show cost calculator shows the monthly and yearly loss, plus what you win back by cutting no-shows.</p>
</div></section>

<article>
  <div class="ac" id="ac">
    <div class="ac__in">
      <div class="ac__f"><label for="nsInd">Your industry</label>
        <select id="nsInd">
          <option value="dental">Dental practice</option>
          <option value="medical">Medical or chiropractic clinic</option>
          <option value="medspa">Med spa or salon</option>
          <option value="home">HVAC, plumbing &amp; home services</option>
          <option value="consult">Law, accounting or insurance consultations</option>
          <option value="other">Other appointment-based business</option>
        </select>
        <div class="ac__note">Sets example values. Replace them with your own.</div></div>
      {rng('nsAppts', 'Booked appointments per week', 5, 500, 5)}
      {rng('nsRate', 'No-show rate today', 0, 40, 1, '<div class="ac__note">No-shows ÷ booked appointments. Your scheduling software usually shows this.</div>')}
      {rng('nsTarget', 'No-show rate after reminders', 0, 40, 1, '<div class="ac__note">A goal to test, not a promise. Set it to what you think reminders and confirmations could reach.</div>')}
      <div class="ac__rates"><b>Your numbers</b><div class="ac__note">Example values. Use your own averages.</div>
        <div class="ac__g">
          {A.num('nsVal', 'Average value of a visit ($)', 200, 10)}
          {A.num('nsRebook', 'No-shows that rebook and come later (%)', 30, 5)}
        </div></div>
    </div>
    <div class="ac__out" aria-live="polite">
      <div class="ac__k">No-shows cost you</div>
      <div class="ac__big"><span id="nsYear">$0</span><small id="nsYearL">per year</small></div>
      <div class="ac__rows">
        <div><span>Missed appointments a month</span><b id="nsMissed"></b></div>
        <div><span>Revenue lost a month</span><b id="nsMonth"></b></div>
        <div class="best"><span>Won back a month at your target</span><b id="nsSave"></b></div>
        <div><span>Won back a year</span><b id="nsSaveY"></b></div>
      </div>
      <div class="ac__for" id="nsFor"></div>
      <div class="ac__btns"><a class="btn" href="../../#book" id="nsBook">Cut my no-shows on a free call →</a><button type="button" class="btn ac__ghost" id="nsCopy">Copy link to this result</button></div>
      <form class="lead ac__lead" data-lead="tool-{SLUG}" data-ok="Thanks! I’ll email your result and a short plan within one business day.">
        <b style="color:#fff;font-size:15px">Email me this result and a plan</b>
        <input name="name" placeholder="First name" autocomplete="given-name" aria-label="First name">
        <input type="email" name="email" required placeholder="Email address" autocomplete="email" aria-label="Email address">
        <input name="website" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
        <button class="btn ac__ghost" type="submit">Send me a plan</button>
        <p class="lead__msg" aria-live="polite"></p>
      </form>
      <a href="../../solutions/no-shows/" style="color:var(--red-text);font-weight:700;font-size:14.5px">See how automated reminders work →</a>
    </div>
  </div>

  <h2 id="how">How do you calculate the cost of no-shows?</h2>
  <p>The cost of no-shows is the number of missed appointments times what each visit is worth, minus the visits that still happen later because the person rebooked:</p>
  <p><strong>Monthly cost = appointments per week × 4.33 × no-show rate × average visit value × (1 − share that rebooks)</strong>. Multiply by 12 for the yearly cost.</p>
  <p>A worked example with hypothetical numbers: 100 appointments a week, a 12% no-show rate, a $200 average visit and 30% of no-shows rebooking later. That is about 52 missed appointments a month and 100 × 4.33 × 0.12 × $200 × 0.70 ≈ $7,270 lost a month, or about $87,300 a year. Cutting the rate from 12% to 6% would win back about half of that. These are example numbers; use your own.</p>

  <h2 id="scenarios">What do no-shows cost at different sizes?</h2>
  <p>Example scenarios with a 10% no-show rate and 30% of no-shows rebooking later. They illustrate the math; they are not benchmarks:</p>
  <div class="tw"><table>
    <tr><th>Business</th><th>Appointments a week</th><th>Visit value</th><th>Lost a month</th><th>Lost a year</th></tr>
    <tr><td>Small clinic</td><td>40</td><td>$150</td><td>$1,819</td><td>$21,823</td></tr>
    <tr><td>Busy dental practice</td><td>120</td><td>$250</td><td>$9,093</td><td>$109,116</td></tr>
    <tr><td>Med spa</td><td>60</td><td>$300</td><td>$5,456</td><td>$65,470</td></tr>
    <tr><td>Home service company</td><td>30</td><td>$400</td><td>$3,637</td><td>$43,646</td></tr>
  </table></div>
  <p>Higher-value appointments make each no-show expensive even at low volume, which is why med spas, dental practices and contractors with in-home estimates feel no-shows most.</p>

  <h2 id="rate">How do you find your no-show rate?</h2>
  <p>Take the last 4 weeks in your scheduling or practice software. Count booked appointments and count no-shows (people who neither came nor cancelled). Divide no-shows by booked appointments and multiply by 100. Track late cancellations separately: you may refill those slots, while a no-show slot is usually lost. Check the rate by weekday, appointment type and how far ahead the visit was booked, because visits booked weeks in advance are often the ones people forget.</p>

  <h2 id="reduce">How can you reduce no-shows?</h2>
  <ul>
    <li><strong>Confirm at booking:</strong> a text with the date, time, address and how to reschedule.</li>
    <li><strong>Remind before the visit:</strong> one reminder a day or two ahead, and one on the day for early appointments.</li>
    <li><strong>Make it two-way:</strong> let people reply to confirm or reschedule, so a "can't make it" becomes a rebooking instead of an empty slot.</li>
    <li><strong>Keep a waitlist:</strong> offer freed-up slots to people who want an earlier time.</li>
    <li><strong>Use deposits where they fit:</strong> for long or high-value appointments such as med spa treatments.</li>
  </ul>
  <p>Practices should keep reminders free of sensitive details: date, time, location and how to confirm. The <a href="https://www.hhs.gov/hipaa/for-professionals/index.html" rel="noopener">HHS HIPAA guidance for professionals</a> covers what counts as protected health information. Automated texts need the person's consent and an easy way to opt out.</p>

  <h2 id="industry">How do no-shows differ by industry?</h2>
  <ul>
    <li><strong>Dental practices:</strong> hygiene visits booked months ahead are easy to forget. See <a href="../../blog/reduce-dental-no-shows/">how to reduce no-shows at a dental office</a> and <a href="../../industries/dental/">automation for dental practices</a>.</li>
    <li><strong>Med spas:</strong> high-value consultations make deposits and confirmations worth it. See <a href="../../blog/med-spa-no-shows/">how med spas can reduce consultation no-shows</a>.</li>
    <li><strong>Home services:</strong> a missed in-home estimate wastes a technician's drive as well as the slot. See <a href="../../industries/home-services/">automation for home service businesses</a>.</li>
    <li><strong>Chiropractic and physical therapy:</strong> missed follow-up visits break a treatment plan. See <a href="../../industries/chiropractic/">automation for chiropractors</a>.</li>
  </ul>
  <p>The <a href="../../solutions/no-shows/">no-shows solution</a> shows how I set up confirmations, reminders and rebooking, and the <a href="../../pricing/">pricing page</a> shows what it costs. If leads also wait too long before they book at all, try the <a href="../speed-to-lead-calculator/">speed to lead calculator</a>.</p>

  <h2 id="faq">FAQ</h2>
{faq_html}
  <div class="sources"><b>Sources and further reading</b><ul>
    <li><a href="https://www.hhs.gov/hipaa/for-professionals/index.html" rel="noopener">U.S. Department of Health and Human Services: HIPAA for professionals</a></li>
  </ul></div>

  <div class="related"><b>Related tools and guides</b><ul>
    <li><a href="../speed-to-lead-calculator/">Speed to lead calculator</a></li>
    <li><a href="../missed-call-calculator/">Missed call cost calculator</a></li>
    <li><a href="../../blog/reduce-dental-no-shows/">How to reduce no-shows at a dental office</a></li>
    <li><a href="../../blog/med-spa-no-shows/">How med spas can reduce consultation no-shows</a></li>
    <li><a href="../../solutions/no-shows/">Reduce no-shows with automated reminders</a></li>
    <li><a href="../">All free tools</a></li>
  </ul></div>

  <div class="cta">
    <h2>Want fewer empty slots?</h2>
    <p>Book a free 30-minute call. Bring last month's appointment numbers and I'll show you where reminders and rebooking would save the most.</p>
    <a class="btn" href="../../#book">Book a free call →</a>
  </div>
</article>

{chrome.footer('../../')}
<script>
(function(){{
  // Example values per industry (not statistics): appointments a week, no-show %, visit value
  var P={{dental:[100,12,200],medical:[120,12,150],medspa:[60,10,300],home:[30,8,400],consult:[25,10,250],other:[60,10,150]}};
  var $=function(i){{return document.getElementById(i)}},R=['nsAppts','nsRate','nsTarget'],N=['nsVal','nsRebook'];
  var KEY={{nsAppts:'appts',nsRate:'rate',nsTarget:'target',nsVal:'value',nsRebook:'rebook'}};
  var money=function(n){{return '$'+Math.round(n).toLocaleString('en-US')}},v=function(i){{var x=parseFloat($(i).value);return isFinite(x)&&x>=0?x:0}},used=false;
  function update(){{
    R.forEach(function(i){{var r=$(i);r.style.setProperty('--p',(r.value-r.min)/(r.max-r.min)*100+'%')}});
    var A=v('nsAppts')*4.33,r=Math.min(v('nsRate'),100)/100,t=Math.min(v('nsTarget'),100)/100,val=v('nsVal'),keep=1-Math.min(v('nsRebook'),100)/100;
    $('nsApptsV').textContent=v('nsAppts').toLocaleString('en-US');$('nsRateV').textContent=Math.round(r*100)+'%';$('nsTargetV').textContent=Math.round(t*100)+'%';
    var missed=A*r,month=missed*val*keep,save=Math.max(0,(r-t))*A*val*keep;
    $('nsYear').textContent=money(month*12);$('nsYearL').textContent='per year · '+money(month)+' a month';
    $('nsMissed').textContent=Math.round(missed).toLocaleString('en-US');$('nsMonth').textContent=money(month);$('nsSave').textContent=money(save);$('nsSaveY').textContent=money(save*12);
    $('nsFor').textContent=v('nsAppts')+' a week × 4.33 × '+Math.round(r*100)+'% no-shows × '+money(val)+' × '+Math.round(keep*100)+'% not rebooked = '+money(month)+' a month.'+(t>=r?' Set the target below your current rate to see what you win back.':'');
  }}
  function touch(){{if(!used){{used=true;(window.dataLayer=window.dataLayer||[]).push({{event:'tool_used',tool:'{SLUG}'}})}}update()}}
  function link(){{var q=R.concat(N).map(function(i){{return KEY[i]+'='+encodeURIComponent($(i).value)}}).join('&');return location.origin+location.pathname+'?'+q}}
  $('nsInd').addEventListener('change',function(e){{var p=P[e.target.value];$('nsAppts').value=p[0];$('nsRate').value=p[1];$('nsTarget').value=Math.max(0,Math.round(p[1]/2));$('nsVal').value=p[2];touch()}});
  R.concat(N).forEach(function(i){{$(i).addEventListener('input',touch)}});
  $('nsCopy').addEventListener('click',function(){{var b=this,u=link(),done=function(){{b.textContent='Link copied';setTimeout(function(){{b.textContent='Copy link to this result'}},1800)}};
    (window.dataLayer=window.dataLayer||[]).push({{event:'tool_result_shared',tool:'{SLUG}'}});
    if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(u).then(done,function(){{prompt('Copy this link',u)}});else prompt('Copy this link',u)}});
  $('nsBook').addEventListener('click',function(){{(window.dataLayer=window.dataLayer||[]).push({{event:'calculator_cta',tool:'{SLUG}',yearly:$('nsYear').textContent}})}});
  var lf=document.querySelector('.ac__lead');if(lf)lf.leadExtra=function(){{return 'Industry: '+$('nsInd').selectedOptions[0].text+'; appts/wk '+$('nsAppts').value+'; no-show '+$('nsRate').value+'%; target '+$('nsTarget').value+'%; visit $'+$('nsVal').value+'; rebook '+$('nsRebook').value+'%; yearly loss '+$('nsYear').textContent+'; won back/yr '+$('nsSaveY').textContent}};
  // defaults, then any values shared in the link (?appts=100&rate=12 ...)
  $('nsAppts').value=100;$('nsRate').value=12;$('nsTarget').value=6;
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
