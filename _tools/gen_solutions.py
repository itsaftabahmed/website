# Generates problem-based solution pages (/solutions/<slug>/) in the service-page design.
# Edit SOL below, then run: python3 _tools/gen_solutions.py
import json, os, re, html, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chrome
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U = 'https://iamaftabahmed.com/'
e = lambda t: html.escape(t, quote=False)
src = open(f'{ROOT}/services/ai-automation/index.html').read()
TRACK = src[src.index('<head>') + 6:src.index('<title>')]
BODY_TRACK = src[src.index('<body>') + 6:re.search(r'<div class="ann">|<header', src).start()]
PRICE_FROM = 297   # monthly; shown on every solution page as 'Plans start from $297/month'
ICON = re.search(r'<link rel="icon"[^>]*>', src).group(0)

def phone(top, rows):
    return ('<div class="sv-phone" aria-hidden="true"><div class="sv-phone__top">' + top + '</div>'
            + ''.join(f'<div class="sv-{k}">{t}</div>' for k, t in rows) + '<div class="sv-ex">Example conversation</div></div>')

SOL = [
 dict(slug='missed-calls', name='Missed Calls', menu='Stop missed calls',
  title='Stop Missing Calls: AI Receptionist & Missed Call Text Back',
  desc='Stop losing customers to missed calls. An AI receptionist and missed call text back answer every caller in seconds and book them, day or night.',
  kicker='Solution · Missed calls',
  h1='Every missed call is a customer calling someone else',
  lead='When you can’t pick up, callers try the next business on the list. I set up an AI receptionist and an instant text back so every caller gets an answer in seconds and a booked time, even after hours.',
  visual=phone('Cool Air Heating · 7:42 pm', [('miss', 'Missed call from (512) 555-0187'), ('me', 'Hi, this is Cool Air Heating. Sorry we missed you! Is your AC or heat acting up?'), ('you', 'AC is blowing warm air'), ('me', 'I can get a tech out tomorrow at 9 am or 1 pm. Which works?'), ('you', '9 works'), ('ok', '✓ Booked · Tomorrow 9:00 am · tech assigned')]),
  intro=['Most missed calls are not lost because the business is bad. They happen because the team is on a job, with a patient, or closed for the night, and the caller won’t leave a voicemail.',
         'The fix is simple: answer every call, or reply to it within seconds, and give the caller an easy way to book. That is what this setup does.'],
  before=['Calls go to voicemail when the team is busy', 'After-hours callers book with a competitor', 'Callbacks happen hours later, if at all'],
  after=['Every call answered or texted back in seconds', 'Appointments booked straight into your calendar', 'Urgent calls passed to a person right away'],
  included=[('AI receptionist', 'Answers calls 24/7 with your approved answers, in a natural voice, using your business name.'),
            ('Missed call text back', 'Any call you can’t answer gets a friendly text within seconds, so the caller stays with you.'),
            ('Calendar booking', 'Offers real open times and books the appointment while the caller is still on the line.'),
            ('Smart handoff', 'Emergencies, complaints and sensitive calls go straight to you or your team.'),
            ('Call summaries in your CRM', 'Every call is logged with notes, so nothing gets lost between staff.'),
            ('Monthly report', 'Calls answered, appointments booked and calls handed off, in plain numbers.')],
  fit=['Home service businesses whose teams are out on jobs', 'Dental, medical and wellness practices with a busy front desk', 'Law firms, agencies and offices that close at 5 pm', 'Any business running ads that bring in phone calls'],
  steps=[('Book a call.', 'We look at your call volume, missed calls and how bookings work today.'),
         ('Get a clear plan.', 'Script, booking rules and handoffs agreed before anything is built.'),
         ('Go live.', 'Tested on real questions, connected to your number and calendar, then switched on with reporting.')],
  quote=('“Before working with Aftab, our team had to manually chase every lead. Some were contacted late and others were missed completely. He automated the follow-up while improving our campaigns at the same time. We now respond faster and our team can focus on closing instead of chasing.”', 'Ryan Cooper', 'Founder, Local Service Business'),
  mid=('See what missed calls cost you', 'Enter your call numbers and get a monthly estimate in 30 seconds.', 'tools/missed-call-calculator/', 'Open the calculator →'),
  btn2=('demo/', 'Try the live demo'), cta='Ready to stop losing callers?',
  case=('hvac', 'HVAC · Austin, Texas', 'Turning more inquiries into booked service calls', ['Inquiry from ad', 'Acknowledgment sent', 'Office callback', 'Service call booked']),
  faq=[('Will callers know they are talking to an AI?', 'They should, and the assistant says so if asked. Most callers care more about a fast, helpful answer and an easy way to book than about who picks up.'),
       ('Can I keep my existing phone number?', 'Usually, yes. Calls can be forwarded to the AI after hours, when lines are busy or after a set number of rings, so customers keep calling the number they know.'),
       ('What happens with urgent or complicated calls?', 'You decide the rules. Emergencies, complaints or anything outside the script can be transferred to you, sent as an instant alert, or booked as a priority callback.'),
       ('How much does it cost?', 'It depends on call volume and what needs connecting, such as your calendar and CRM. Most setups combine a one-time build with a monthly running cost. On a free call I’ll give you a clear quote.')],
  related=[('demo/', 'Try the AI receptionist live demo'), ('tools/ai-receptionist-cost-calculator/', 'AI receptionist cost calculator'), ('tools/missed-call-calculator/', 'Missed call cost calculator'),
           ('blog/missed-call-text-back/', 'Missed call text back: never lose a caller again'), ('blog/ai-receptionist-vs-answering-service/', 'AI receptionist vs answering service'),
           ('services/ai-automation/', 'AI automation and AI receptionists')]),

 dict(slug='lead-follow-up', name='Slow Follow-Up', menu='Fix slow follow-up',
  title='Automated Lead Follow-Up: Reply to Every Lead in Seconds',
  desc='Leads go cold in minutes. Automated follow-up replies to every form, ad lead and message in seconds, then keeps following up by text and email until they book.',
  kicker='Solution · Lead follow-up',
  h1='Leads go cold while your team is busy',
  lead='Most leads don’t say no. They just never hear back in time. I connect every lead source to one system that replies in seconds and keeps following up by text, email and call tasks until the lead books or says stop.',
  visual='<div class="sv-panel" aria-hidden="true"><div class="sv-panel__h">New leads today</div><div class="sv-lead"><b>Maria G.</b><span>Quote request · Website form</span><i class="g">Replied in 40 sec</i></div><div class="sv-lead"><b>James P.</b><span>Facebook lead form</span><i class="g">Call booked</i></div><div class="sv-lead"><b>Dana W.</b><span>Google Ads · landing page</span><i class="y">Follow-up day 3</i></div><div class="sv-lead"><b>Chris L.</b><span>Instagram DM</span><i class="y">Text sent · 1 min</i></div><div class="sv-ex">Example pipeline</div></div>',
  intro=['Leads arrive from forms, ads, DMs and calls, often while everyone is busy. By the time someone replies, the lead has already talked to a competitor or forgotten why they reached out.',
         'Automated follow-up fixes the timing. The first reply goes out in seconds, the next steps happen on schedule, and your team only steps in for real conversations.'],
  before=['Leads scattered across inboxes and apps', 'Replies hours or days later', 'Follow-up depends on who remembers'],
  after=['Every lead in one place within seconds', 'Instant reply by text and email', 'Planned follow-up until they book or opt out'],
  included=[('Instant first reply', 'A personal-sounding text and email the moment a lead arrives, with a link to book.'),
            ('One inbox for every lead', 'Website forms, Facebook and Google lead forms, DMs and missed calls land in the same CRM.'),
            ('Follow-up sequences', 'A planned series of texts, emails and call tasks over about two weeks, written in your voice.'),
            ('Stop rules', 'Any reply, booking or opt-out ends the sequence automatically, so nobody gets chased after they book.'),
            ('Alerts for your team', 'Hot leads and replies notify the right person right away.'),
            ('Pipeline you can read', 'See every lead, where it stands and which source turned into revenue.')],
  fit=['Businesses running Google or Facebook ads', 'Home services, contractors and trades sending quotes', 'Agencies, firms and offices with web and phone leads', 'Teams that lose track of leads in inboxes and spreadsheets'],
  steps=[('Book a call.', 'We map every place your leads come from and what happens to them today.'),
         ('Get a clear plan.', 'Sequence, wording and handoffs agreed before anything is built.'),
         ('Go live.', 'Every source connected, tested end to end, then switched on with reporting.')],
  quote=('“Our biggest problem wasn’t getting leads — it was following up with them fast enough. Aftab connected our ads, CRM, SMS and automated follow-up so every enquiry was contacted immediately. We stopped losing good leads simply because the team was busy.”', 'Sarah Mitchell', 'Managing Director, Healthcare Practice'),
  mid=('Want the 14-day sequence?', 'My guide shows the exact texts, emails and timing I start with.', 'blog/automated-lead-follow-up/', 'Read the guide →'),
  btn2=('blog/automated-lead-follow-up/', 'See the follow-up guide'), cta='Ready to reply to every lead in seconds?',
  case=('insurance', 'Insurance · Columbus, Ohio', 'Bringing quote inquiries into one process', ['New request', 'Assigned to agent', 'Contacted', 'Consultation booked']),
  faq=[('Will automated messages sound robotic?', 'They shouldn’t. The messages are written in your voice, mention what the lead asked about, and every reply goes to a real person on your team.'),
       ('Which lead sources can be connected?', 'Usually all of them: website forms, Facebook and Google lead forms, Instagram and Facebook messages, missed calls, and most booking tools. Anything that can send an email or a webhook can be connected.'),
       ('Is it legal to text leads automatically?', 'Generally yes, when the lead gave consent, for example on your form, and every message includes an easy way to opt out. The setup includes consent wording and opt-out handling.'),
       ('Do I need a new CRM?', 'Not necessarily. If you already use one, the follow-up is built around it. If your leads live in inboxes and spreadsheets, a simple CRM is usually part of the setup.')],
  related=[('blog/automated-lead-follow-up/', 'How to follow up with leads automatically'), ('blog/speed-to-lead/', 'Speed to lead: why the first 5 minutes decide the sale'), ('solutions/missed-calls/', 'Stop missed calls'), ('services/lead-generation/', 'Lead generation systems')]),
 dict(slug='no-shows', name='No-Shows', menu='Reduce no-shows',
  title='Reduce No-Shows with Automated Reminders & Easy Rescheduling',
  desc='Cut no-shows and late cancellations with automatic reminders, two-way confirmations, easy rescheduling by text and a waitlist that fills empty slots fast.',
  kicker='Solution · No-shows',
  h1='Empty slots cost you more than you think',
  lead='Most no-shows aren’t rude. People forget, or rescheduling feels like a hassle. I set up reminders, two-way confirmations and one-tap rescheduling, plus a waitlist that fills cancelled slots automatically.',
  visual=phone('Bright Smile Dental · Reminder', [('me', 'Hi Maria, you’re booked for Thu at 10:30 am with Dr. Lee. Reply C to confirm or R to reschedule.'), ('you', 'R'), ('me', 'No problem! Next open times: Fri 9:00 am or Mon 2:30 pm. Which works?'), ('you', 'Fri 9'), ('ok', '✓ Moved to Fri 9:00 am · Thu slot offered to waitlist')]),
  intro=['A missed appointment leaves a gap your team is still paid for, and it often delays the treatment or job that follows. Manual reminder calls take hours and still miss people.',
         'Automated reminders and easy rescheduling turn most would-be no-shows into confirmed or moved appointments, and a short-notice list fills the gaps that remain.'],
  before=['Reminder calls eat front-desk time', 'Rescheduling means calling during office hours', 'Cancelled slots stay empty'],
  after=['Reminders and confirmations sent automatically', 'Reschedule by text in a few taps', 'Cancellations offered to a waitlist right away'],
  included=[('Booking confirmations', 'Instant confirmation with an add-to-calendar link the moment someone books.'),
            ('Smart reminders', 'A short sequence before each visit, timed to how far ahead it was booked.'),
            ('Two-way confirmation', 'Reply C to confirm or R to reschedule, and your schedule updates on its own.'),
            ('Waitlist fill', 'A cancelled slot is offered to your short-notice list by text, first reply wins.'),
            ('Unconfirmed list', 'Your team gets a short call list of people who didn’t confirm, instead of calling everyone.'),
            ('No-show tracking', 'See your no-show rate each month and whether it is improving.')],
  fit=['Dental, medical and chiropractic practices', 'Med spas, salons and wellness clinics', 'Consultations for law firms, accountants and agencies', 'Service businesses with booked estimates or visits'],
  steps=[('Book a call.', 'We look at your booking tool, no-show rate and how reminders work today.'),
         ('Get a clear plan.', 'Reminder timing, wording and rescheduling rules agreed first.'),
         ('Go live.', 'Connected to your calendar or practice software, tested, then switched on.')],
  quote=('“We had different people handling our ads, website and automation, and nothing really worked together. Aftab brought everything under one strategy. Our messaging became clearer, the campaigns improved and every lead now moves through a proper follow-up process.”', 'Olivia Harris', 'Managing Director, Growing SMB'),
  mid=('See the reminder schedule that works', 'My guide covers timing, wording and what to do about repeat no-shows.', 'blog/reduce-dental-no-shows/', 'Read the guide →'),
  btn2=('blog/reduce-dental-no-shows/', 'See the reminder guide'), cta='Ready to fill your schedule?',
  case=('med-spa', 'Med spa · Scottsdale, Arizona', 'Helping inquiries become consultations', ['Consultation request', 'Acknowledgment', 'Staff follow-up', 'Consultation confirmed']),
  faq=[('Does this work with my booking or practice software?', 'Often, yes. Many scheduling and practice management tools connect directly or through automation platforms. Where they can’t, reminders can run from a connected calendar.'),
       ('How many reminders should we send?', 'Usually a confirmation at booking, a heads-up for visits booked far ahead, a two-way confirmation two days before and a short reminder on the day. More than that tends to annoy people.'),
       ('Should we charge a no-show fee?', 'A clear policy helps with repeat no-shows, but most businesses get further with reminders and easy rescheduling first. Check your contracts and local rules before charging fees.'),
       ('Can reminders include sensitive details?', 'They shouldn’t. Reminders stick to the date, time, location and how to confirm or reschedule, with no treatment or case details.')],
  related=[('blog/reduce-dental-no-shows/', 'How to reduce no-shows at a dental office'), ('blog/med-spa-no-shows/', 'How med spas can reduce consultation no-shows'), ('solutions/missed-calls/', 'Stop missed calls'), ('services/ai-automation/', 'AI automation and AI receptionists')]),
 dict(slug='ads-not-converting', name='Ads Not Converting', menu='Fix ads that don’t convert',
  title='Ads Not Converting? Fix the Offer, Page and Follow-Up',
  desc='Getting clicks but no customers? I fix the whole path from ad to booked call: the offer, the landing page, tracking and follow-up, on Google and Facebook ads.',
  kicker='Solution · Ads not converting',
  h1='Clicks don’t pay the bills. Booked customers do.',
  lead='When ads bring clicks but no customers, the problem is rarely just the targeting. I look at the whole path: the offer, the landing page, the tracking and what happens after someone fills in the form.',
  visual='<div class="sv-panel" aria-hidden="true"><div class="sv-search"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true" style="vertical-align:-2px"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg> hardwood floor installation near me</div><div class="sv-ad"><small>Sponsored · oakandgrain.example</small><b>Hardwood Floors Installed in 2 Weeks</b><p>Free in-home estimate. Licensed, insured, local team. See real projects.</p><span class="sv-call">Get my estimate</span></div><div class="sv-ok">✓ Estimate booked · text sent in 30 seconds</div><div class="sv-ex">Example ad</div></div>',
  intro=['Ads often get blamed for problems that happen after the click: a vague offer, a generic page, no tracking, or leads that wait a day for a reply.',
         'Fixing those pieces usually brings more booked customers from the same budget. Then the ads themselves can be scaled with confidence.'],
  before=['Clicks and leads, but few customers', 'Ads pointing to a general homepage', 'No idea which ads bring real revenue'],
  after=['A clear offer people want to claim', 'Landing pages built for one action', 'Calls and bookings tracked back to each ad'],
  included=[('Account and funnel audit', 'Where money is wasted: searches, audiences, pages and follow-up.'),
            ('Offer and message', 'A specific, honest offer and ad copy that speaks to buyers, not browsers.'),
            ('Landing pages', 'Fast pages for one service and one action, matched to each campaign.'),
            ('Conversion tracking', 'Calls, forms and bookings tracked in Google Ads, Meta and Analytics.'),
            ('Lead follow-up', 'Instant replies so the leads you pay for actually get contacted.'),
            ('Ongoing management', 'Testing, budget shifts and plain-English reports on cost per customer.')],
  fit=['Businesses spending on Google or Facebook ads without clear results', 'Local service businesses that need calls and bookings', 'Owners who were told “ads don’t work for us”', 'Teams with leads coming in but few turning into customers'],
  steps=[('Book a call.', 'We review your ads, pages and numbers together.'),
         ('Get a clear plan.', 'The biggest leaks first, with what to fix and in what order.'),
         ('Fix and scale.', 'Offer, pages, tracking and follow-up fixed, then budget moved to what works.')],
  quote=('“We were getting plenty of clicks but very few people were actually booking. Aftab identified that the problem was the landing page and offer, not the ads. After rebuilding the customer journey, more of our traffic started turning into real enquiries.”', 'Emma Collins', 'Marketing Director, Professional Services Firm'),
  mid=('Clicks but no calls?', 'My guide covers the 6 most common reasons and how to fix each one.', 'blog/facebook-ads-clicks-but-no-calls/', 'Read the guide →'),
  btn2=('blog/facebook-ads-clicks-but-no-calls/', 'Why ads get clicks but no calls'), cta='Ready for ads that bring customers?',
  case=('flooring', 'Flooring · Charlotte, North Carolina', 'Helping homeowners take the next step', ['Landing page', 'Project details captured', 'Estimator task', 'Estimate scheduled']),
  faq=[('Do you manage Google Ads, Facebook Ads or both?', 'Both. Many service businesses do best with Google for high-intent searches and Facebook or Instagram for offers and retargeting. The plan depends on your market and budget.'),
       ('How fast will I see results?', 'Fixes to tracking, pages and follow-up often show within weeks. Ad campaigns usually need a few weeks of data to settle before scaling.'),
       ('What budget do I need?', 'It depends on your market and goals. We work out a budget from the number of customers you want and what one customer is worth to you.'),
       ('Do you need access to my ad accounts?', 'Yes, as a partner or admin user. You keep ownership of your accounts, pages and data the whole time.')],
  related=[('blog/facebook-ads-clicks-but-no-calls/', 'Why your Facebook ads get clicks but no calls'), ('blog/facebook-ads-cost-small-business/', 'How much do Facebook ads cost?'), ('services/google-ads/', 'Google Ads management'), ('services/facebook-ads/', 'Facebook and Instagram ads')]),
 dict(slug='busywork', name='Too Much Busywork', menu='Automate busywork',
  title='Automate Busywork: Onboarding, Admin, Reviews & Reports',
  desc='Get hours back every week. I automate admin like client onboarding, data entry, review requests, invoices and reports, built around the tools you use.',
  kicker='Solution · Busywork',
  h1='Your team’s time is too valuable for copy and paste',
  lead='Copying details between apps, chasing documents, sending the same emails and building reports by hand all add up. I automate the repetitive steps so your team spends its time on customers.',
  visual='<div class="sv-panel" aria-hidden="true"><div class="sv-panel__h">Automations this week</div><div class="sv-lead"><b>New client onboarding</b><span>Welcome email, forms, folder created</span><i class="g">Done · 12</i></div><div class="sv-lead"><b>Review requests</b><span>Sent after each completed job</span><i class="g">Done · 38</i></div><div class="sv-lead"><b>Invoice reminders</b><span>Friendly nudges, then a call task</span><i class="g">Done · 9</i></div><div class="sv-lead"><b>Weekly report</b><span>Leads, bookings, revenue by source</span><i class="y">Monday 8 am</i></div><div class="sv-ex">Example dashboard</div></div>',
  intro=['Small teams lose hours each week to tasks a computer could do: moving data between apps, sending reminders, collecting documents and building the same report again.',
         'Automation handles the repeat steps reliably and the same way every time, while your team keeps control of anything that needs judgment.'],
  before=['Copying details between apps by hand', 'Chasing documents and payments by email', 'Reports built manually every week'],
  after=['Data moves between your tools automatically', 'Reminders and requests go out on schedule', 'Reports arrive ready to read'],
  included=[('Client onboarding', 'Welcome messages, forms, contracts and folders set up the moment a client signs.'),
            ('Document collection', 'Requests and reminders until every file is uploaded to your secure portal.'),
            ('Review requests', 'A request after each completed job, sent at the right time.'),
            ('Invoice and payment reminders', 'Polite reminders on schedule, with a task for your team if they don’t work.'),
            ('Data sync between apps', 'Forms, CRM, calendar, accounting and spreadsheets kept in step.'),
            ('Automatic reports', 'Leads, bookings and revenue by source delivered each week.')],
  fit=['Accounting, law and professional services firms', 'Service businesses with repeat paperwork', 'Teams using several apps that don’t talk to each other', 'Owners still doing admin at night'],
  steps=[('Book a call.', 'We list the repetitive tasks and how much time they take.'),
         ('Get a clear plan.', 'The automations that save the most time first, with clear costs.'),
         ('Go live.', 'Built around your current tools, tested, then handed over with simple instructions.')],
  quote=('“Our marketing felt disconnected. Ads were running, leads were coming in, but there was no proper journey after that. Aftab built the whole system from ad to landing page to CRM and follow-up. It made the process much easier to manage and convert.”', 'Michael Thompson', 'Director, Consulting Firm'),
  mid=('Example: onboarding on autopilot', 'See how an accounting firm can automate new client onboarding step by step.', 'blog/accounting-client-onboarding-automation/', 'Read the guide →'),
  btn2=('blog/accounting-client-onboarding-automation/', 'See an onboarding example'), cta='Ready to get hours back every week?',
  case=('accounting', 'Accounting · Manchester, United Kingdom', 'Organizing consultation and onboarding requests', ['Consultation request', 'Team member assigned', 'Client accepted', 'Onboarding checklist']),
  faq=[('Which tools can you automate?', 'Most modern business tools: CRMs, calendars, forms, email, accounting software, spreadsheets and messaging apps. Automation platforms such as Zapier, Make or n8n connect them.'),
       ('Will I need to change my software?', 'Usually not. Automations are built around the tools you already use. If a tool can’t connect, I’ll suggest the simplest alternative.'),
       ('Is my data safe?', 'Automations use the official connections of your tools, and sensitive documents stay in your secure systems. You keep ownership of every account.'),
       ('What if something breaks?', 'Automations are tested before launch and set to alert someone if a step fails, so problems get noticed and fixed quickly.')],
  related=[('blog/accounting-client-onboarding-automation/', 'How to automate client onboarding at an accounting firm'), ('solutions/lead-follow-up/', 'Fix slow follow-up'), ('services/ai-automation/', 'AI automation and AI chatbots'), ('industries/accounting/', 'Automation for accounting and CPA firms')]),
]

COST_Q = 'How much does it cost?'
COST_A = f'Plans start from ${PRICE_FROM} per month. The final price depends on what needs to be built and connected, such as your calendar, CRM and phone system. On a free 30-minute call you get a clear quote before anything starts.'
def faq(x):
    return [(q, a) for q, a in x['faq'] if q != COST_Q] + [(COST_Q, COST_A)]

def page(x):
    url = f'{U}solutions/{x["slug"]}/'; up = '../../'
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Service", "name": x['title'].split(':')[0], "serviceType": x['name'], "url": url, "description": x['desc'],
         "provider": {"@type": "Person", "@id": f"{U}#person", "name": "Aftab Ahmed", "url": f"{U}about/"}, "areaServed": {"@type": "Country", "name": "United States"},
         "offers": {"@type": "Offer", "priceSpecification": {"@type": "UnitPriceSpecification", "minPrice": PRICE_FROM, "priceCurrency": "USD", "unitText": "month"}}},
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": U},
         {"@type": "ListItem", "position": 2, "name": "Solutions", "item": url}, {"@type": "ListItem", "position": 3, "name": x['name'], "item": url}]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq(x)]}]}
    li = lambda xs: ''.join(f'<li>{e(t)}</li>' for t in xs)
    q, who, role = x['quote']; cid, ck, ct, flow = x['case']
    fl = '<i aria-hidden="true">→</i>'.join(f'<span>{e(s)}</span>' for s in flow)
    return f'''<!doctype html>
<html lang="en">
<head>{TRACK}<title>{e(x['title'])}</title>
<meta name="description" content="{html.escape(x['desc'])}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="Aftab Ahmed">
<meta name="theme-color" content="#0A0A0A">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Aftab Ahmed">
<meta property="og:locale" content="en_US">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{html.escape(x['title'])}">
<meta property="og:description" content="{html.escape(x['desc'])}">
<meta property="og:image" content="{U}images/aftab-cutout.webp">
<meta name="twitter:card" content="summary_large_image">
{ICON}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,500..900&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{up}blog/blog.css">
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False)}
</script>
</head>
<body>{BODY_TRACK}{chrome.nav(up)}

<section class="hero hero--svc"><div class="wrap"><div class="sv-copy">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="{up}">Home</a><span>/</span>Solutions<span>/</span>{e(x['name'])}</nav>
  <div class="kicker">{e(x['kicker'])}</div>
  <h1>{e(x['h1'])}</h1>
  <p class="lead">{e(x['lead'])}</p>
  <p class="sv-price">Plans start from <b>${PRICE_FROM}/month</b> · Free 30-minute call, no obligation</p>
  <a class="btn" href="{up}#book">Book a free 30-minute call →</a> <a class="btn" href="{up}{x['btn2'][0]}" style="background:none;border:1px solid #3a3a3a;box-shadow:none;margin-left:6px">{e(x['btn2'][1])}</a>
</div>
{x['visual']}</div></section>

<article class="svc">
{''.join(f'  <p>{e(p)}</p>' + chr(10) for p in x['intro'])}  <div class="sv-ba"><div class="sv-card"><b>Today</b><ul>{li(x['before'])}</ul></div><div class="sv-arrow" aria-hidden="true">→</div><div class="sv-card sv-card--good"><b>After we set it up</b><ul>{li(x['after'])}</ul></div></div>

  <h2 id="included">What's included</h2>
  <div class="svc-grid">{''.join(f'<div><b>{e(t)}</b><p>{e(d)}</p></div>' for t, d in x['included'])}</div>

  <div class="midcta"><div><b>{e(x['mid'][0])}</b><p>{e(x['mid'][1])}</p></div><a class="btn" href="{up}{x['mid'][2]}">{e(x['mid'][3])}</a></div>

  <h2 id="fit">Who this is for</h2>
  <ul class="check">{li(x['fit'])}</ul>

  <h2 id="process">How it works</h2>
  <ol class="steps">{''.join(f'<li><strong>{e(a)}</strong> {e(b)}</li>' for a, b in x['steps'])}</ol>

  <h2 id="proof">What clients say</h2>
  <div class="sv-proof"><figure class="sv-card"><blockquote>{e(q)}</blockquote><figcaption><b>{e(who)}</b><small>{e(role)}</small></figcaption></figure><div class="sv-card"><div class="kicker">Case study · {e(ck)}</div><h3>{e(ct)}</h3><div class="pflow">{fl}</div><p><a href="{up}case-studies/#{cid}">Read the case study →</a></p></div></div>

  <h2 id="faq">FAQ</h2>
{''.join(f'  <h3>{e(q)}</h3>' + chr(10) + f'  <p>{e(a)}</p>' + chr(10) for q, a in faq(x))}
  <div class="related"><b>Related</b><ul>{''.join(f'<li><a href="{up}{h}">{e(t)}</a></li>' for h, t in x['related'])}</ul></div>

  <div class="cta">
    <h2>{e(x['cta'])}</h2>
    <p>Book a free 30-minute call. I’ll look at your calls and show you exactly how this would work for your business.</p>
    <a class="btn" href="{up}#book">Book a free call →</a>
  </div>
</article>

<div class="sv-bar"><a class="btn" href="{up}#book">Book a free call →</a></div>
{chrome.footer(up)}
</body>
</html>
'''

if __name__ == '__main__':
    for x in SOL:
        os.makedirs(f'{ROOT}/solutions/{x["slug"]}', exist_ok=True)
        open(f'{ROOT}/solutions/{x["slug"]}/index.html', 'w').write(page(x))
        print('ok', x['slug'], len(x['title']), len(x['desc']))
