# Generates /industries/ (hub + one page per industry) and /privacy/.
# Edit the I list below, then run: python3 _tools/gen_industries.py
import json, os, html, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U = 'https://iamaftabahmed.com/'
src = open(f'{ROOT}/services/ai-automation/index.html').read()
TRACK_HEAD = src[src.index('<head>') + 6:src.index('<title>')].strip('\n')   # GA4, GTM, Pixel, Clarity, conversion events
TRACK_BODY = src[src.index('<body>') + 6:src.index('<header')].strip('\n')  # GTM noscript
ICON = re.search(r'<link rel="icon" href="([^"]+)"', src).group(1)
e = lambda t: html.escape(t, quote=False)

SV = {'ai': ('AI automation & AI chatbots', 'services/ai-automation/'),
      'ga': ('Google Ads management', 'services/google-ads/'),
      'fb': ('Facebook & Instagram ads', 'services/facebook-ads/'),
      'lg': ('lead generation systems', 'services/lead-generation/')}
# Blog posts that industry pages can link to in their Related box (key -> (title, path)).
POSTS = {'hvacmissed': ('Missed calls are costing your HVAC business jobs', 'blog/hvac-missed-calls/'),
         'fbcalls': ('Why your Facebook ads get clicks but no calls (and how to fix it)', 'blog/facebook-ads-clicks-but-no-calls/'),
         'dentalnoshows': ('How to reduce no-shows at a dental office', 'blog/reduce-dental-no-shows/'),
         'refollowup': ('Real estate lead follow-up scripts for text and email', 'blog/real-estate-follow-up-scripts/'),
         'fbcost': ('How much do Facebook ads cost for a small business in the US?', 'blog/facebook-ads-cost-small-business/')}

I = [
 dict(slug='dental', name='Dental & Medical Practices', short='Dental & medical', forname='dental & medical practices', biz='practice',
  title='AI Receptionist & Lead Generation for Dental Practices',
  desc='Never miss a new-patient call again. AI receptionist, instant text-back, appointment reminders and local ads for US dental and medical practices.',
  h1='Never miss a new-patient call again',
  lead='For dental and medical practices: an AI receptionist that answers and books around the clock, reminders that cut no-shows, and local ads that bring in the patients you actually want.',
  card='AI receptionist, missed-call text back, reminders and local ads that fill the schedule.',
  takeaways=['Most practices don\'t have a patient-demand problem; they lose new patients to missed calls, slow replies and after-hours enquiries.',
             'An AI receptionist can answer common questions and offer real appointment times 24/7, and hand anything clinical to your team.',
             'Automated confirmations and reminders help keep the schedule full without front-desk phone time.',
             'Local Google and Meta ads work best when every lead gets an instant reply and a booking link.'],
  pains_h='Where do dental and medical practices lose new patients?',
  pains_a='Usually between the first call and the first appointment. Patients who can\'t get through, or wait too long for a reply, simply call the next practice on the list.',
  pains=[('Calls missed during treatment','The front desk is checking someone in, the phone rings out, and that caller books somewhere else.'),
         ('Enquiries after hours','Many people look for a dentist in the evening or at the weekend, when nobody is there to answer.'),
         ('No-shows and late cancellations','Empty chairs cost money, and chasing confirmations by phone eats up front-desk time.'),
         ('Ads that bring clicks, not patients','Campaigns send traffic to a generic homepage and nobody can tell which spend produced bookings.')],
  fix_h='How does AI automation help a dental practice?',
  fix_a='It handles the repetitive first steps (answering, qualifying, booking and reminding) so your team can focus on the patients in the chair.',
  fixes=[('AI receptionist (chat & phone)','Answers common questions about services, insurance accepted, hours and location in your practice\'s tone, and offers real open slots.','ai'),
         ('Missed-call text back','If a call isn\'t answered, the caller gets a friendly text within seconds with a link to book.','ai'),
         ('Reminders & confirmations','Automatic text and email reminders, easy confirm or reschedule, and a waitlist to fill gaps.','ai'),
         ('Recall & reactivation','Gentle messages to patients who are due for a cleaning or haven\'t been back in a while.','lg'),
         ('Local search ads','Google Ads for high-intent searches such as "emergency dentist near me" or "dental implants" plus a matching landing page.','ga'),
         ('Review requests','A short text after each visit asking happy patients for a Google review.','ai')],
  journey=['A potential patient searches "dentist near me" at 9pm and taps your ad or listing.',
           'Your AI receptionist answers their questions about the treatment, insurance and opening hours.',
           'They pick an open slot from your real calendar and get an instant confirmation.',
           'Reminders go out automatically before the visit, with an easy way to reschedule.',
           'After the visit, they get a thank-you and a review request.'],
  fit=['General, cosmetic and family dental practices','Orthodontists, oral surgeons and specialty clinics','Medical, chiropractic, physio and wellness clinics','Practices with a busy front desk and more calls than hands'],
  faq=[('Is an AI receptionist HIPAA compliant?','It can be set up with HIPAA-conscious tools, and it is configured to handle scheduling and general questions rather than collect clinical details. Which platforms fit depends on your current software and your own compliance requirements, so we confirm this together before anything goes live.'),
       ('Will patients know they\'re talking to AI?','The assistant is open about being a virtual assistant, and it\'s set up to be warm, clear and quick. Patients who want a person, or have a clinical question, are handed to your team with the full conversation attached.'),
       ('Does it work with my practice management software?','Often, yes, either directly or through your online booking system. If a direct connection isn\'t possible, the assistant can capture the request and alert your front desk to confirm the time.')],
  rel=['ai','ga','dentalnoshows','fbcalls']),
 dict(slug='real-estate', name='Real Estate & Property', short='Real estate & property', forname='real estate & property', biz='business',
  title='Real Estate Lead Follow-Up & AI Automation for Agents',
  desc='Reply to every buyer and seller lead in seconds. AI follow-up, lead qualification, showing booking and ads for US real estate agents and property teams.',
  h1='Reply to every buyer lead in seconds, not hours',
  lead='For real estate agents, teams and property managers: instant replies to every portal, ad and website lead, qualification while you\'re at showings, and follow-up that keeps going for months.',
  card='Instant lead replies, qualification, showing booking and long-term nurture.',
  takeaways=['In real estate, the agent who replies first often wins the conversation, and most leads arrive while you\'re busy with clients.',
             'AI follow-up can reply to new leads within seconds, ask about budget, area and timeline, and book a call or showing.',
             'Most buyers and sellers aren\'t ready today, so automated nurture over weeks and months matters as much as the first reply.',
             'All your lead sources (portals, ads, website, open houses) should land in one CRM with a clear next step.'],
  pains_h='Why do real estate agents lose so many leads?',
  pains_a='Mostly because of speed and follow-up. Leads come in at all hours from many sources, and the ones that aren\'t ready to move this week are often forgotten.',
  pains=[('Slow first response','A lead comes in while you\'re at a showing or a closing, and by the time you call back they\'ve spoken to another agent.'),
         ('Leads scattered everywhere','Portal leads, Facebook leads, website forms and open-house sign-ins all live in different places.'),
         ('"Just looking" leads go cold','Most people are months away from moving, and manual follow-up stops after a call or two.'),
         ('Time spent on tire-kickers','Hours go into calls with people who aren\'t qualified, pre-approved or serious yet.')],
  fix_h='How does AI follow-up work for real estate agents?',
  fix_a='Every new lead gets an instant, personal reply, a few qualifying questions and an easy way to book, and then stays on a follow-up plan until they\'re ready.',
  fixes=[('Instant lead response','New leads from portals, ads and your website get a text and email within seconds, in your voice.','ai'),
         ('AI qualification','Asks about buying or selling, area, budget, timeline and financing, and flags hot leads to you right away.','ai'),
         ('Showing & call booking','Offers times from your calendar for a call, valuation or showing, with confirmations and reminders.','ai'),
         ('Long-term nurture','Helpful, low-pressure check-ins and new listing alerts for leads who aren\'t ready yet.','lg'),
         ('One CRM for every source','Every lead in one place with its source, status and next step, so nothing slips through.','lg'),
         ('Listing & seller ads','Facebook, Instagram and Google campaigns for listings, home valuations and open houses.','fb')],
  journey=['Someone fills in a home-valuation form from your Facebook ad on a Sunday evening.',
           'Within seconds they get a personal text from your assistant thanking them and asking a couple of quick questions.',
           'They answer: selling in 3 to 6 months, already found their next area. You get an alert marking it a hot lead.',
           'They book a call slot from your calendar right in the conversation.',
           'If they\'re not ready yet, they get useful updates over the coming months instead of being forgotten.'],
  fit=['Solo agents and real estate teams buying portal or ad leads','Brokerages that want consistent follow-up across agents','Property managers handling rental and maintenance enquiries','Investors and developers marketing new projects'],
  faq=[('Can the AI reply to Zillow and Realtor.com leads?','In most cases, yes. Portal leads usually arrive by email or through your CRM, and the automation can pick them up and reply by text and email within seconds. The exact setup depends on which portals and CRM you use.'),
       ('Will leads know they\'re talking to an assistant?','The assistant is set up to be clear that it\'s helping on your behalf and to sound natural and friendly. As soon as a lead wants to talk to you or is clearly serious, it hands over with the full conversation attached.'),
       ('Does this replace my CRM?','Not necessarily. If you already use a real estate CRM, the automation is built around it. If your leads are scattered across inboxes and spreadsheets, setting up a simple CRM is usually part of the first step.')],
  rel=['ai','lg','refollowup','fbcost']),
 dict(slug='accounting', name='Accounting & CPA Firms', short='Accounting & CPA', forname='accounting & CPA firms', biz='firm',
  title='AI Automation & Client Onboarding for CPA Firms',
  desc='Win more clients without the admin pile-up. AI enquiry handling, automated onboarding, document chasing and lead generation for US accounting and CPA firms.',
  h1='Win more clients without the admin pile-up',
  lead='For accounting, bookkeeping and CPA firms: an assistant that handles routine enquiries, onboarding that runs itself, automatic document reminders, and a steady flow of the right new clients.',
  card='Enquiry handling, automated onboarding, document chasing and steady new clients.',
  takeaways=['Accounting firms lose most of their time to repetitive admin: the same questions, onboarding steps and document chasing every season.',
             'An AI assistant can answer routine questions, qualify new enquiries and book consultations, and hand complex questions to your team.',
             'Automated onboarding and document reminders cut back-and-forth emails, especially during tax season.',
             'Targeted ads and landing pages help you attract the type of client you want, not just more enquiries.'],
  pains_h='What slows accounting and CPA firms down the most?',
  pains_a='Repetitive admin. Answering the same questions, onboarding new clients by hand and chasing missing documents take time away from billable work, and peak season makes it worse.',
  pains=[('The same questions, every day','"What do you charge?", "Do you handle my type of return?", "What documents do I need?" asked again and again.'),
         ('Manual onboarding','Engagement letters, intake forms and welcome emails sent one by one, so new clients wait.'),
         ('Chasing documents','Hours spent emailing clients for missing receipts, statements and signatures.'),
         ('Unpredictable new clients','Growth relies on referrals, and enquiries spike in tax season and dry up after.')],
  fix_h='How can an accounting firm use AI automation?',
  fix_a='By automating the steps that repeat for every client (enquiries, intake, reminders and follow-up) while your team keeps control of anything that needs professional judgment.',
  fixes=[('AI enquiry assistant','Answers routine questions about services, process and fees on your website, and qualifies new enquiries.','ai'),
         ('Consultation booking','Qualified prospects book a discovery call straight into your calendar, with reminders.','ai'),
         ('Automated onboarding','Engagement letter, intake form and welcome sequence go out automatically once a client says yes.','ai'),
         ('Document reminders','Friendly automatic reminders until every document is in, with a clear checklist for the client.','ai'),
         ('Year-round lead generation','Google Ads and landing pages for the services you want more of, such as bookkeeping, small-business tax or advisory.','ga'),
         ('Client reactivation','Timely messages to past clients before tax season and for year-round services.','lg')],
  journey=['A small-business owner searches for "bookkeeping for small business" and lands on your page.',
           'Your assistant answers their questions and asks about their business type, size and needs.',
           'They book a consultation, and you get a summary of the enquiry before the call.',
           'Once they sign up, onboarding starts automatically: engagement letter, intake form and welcome email.',
           'Document reminders go out on a schedule until everything is in, without anyone chasing by hand.'],
  fit=['CPA firms and tax practices with seasonal workload peaks','Bookkeeping and payroll firms onboarding clients regularly','Advisory and fractional CFO practices that want better-fit clients','Small firms where partners still do the admin themselves'],
  faq=[('Is it safe to use AI with client financial information?','The assistant is set up to handle enquiries, scheduling and reminders, not to collect sensitive financial data in chat. Documents still go through your secure client portal, and the tools are chosen to fit your firm\'s security and confidentiality requirements.'),
       ('Will the AI give tax advice to clients?','No. It answers routine questions about your services and process and hands anything that needs professional judgment to your team. That keeps advice where it belongs and saves your staff time on the basics.'),
       ('Does it work with the software we already use?','Usually, yes. Automation is built around your existing tools, such as your CRM or practice management system, client portal, e-signature and calendar, rather than forcing you to switch.')],
  rel=['ai','ga','lg']),
 dict(slug='home-services', name='Home Services', short='Home services', forname='home service businesses', biz='business', who='customer',
  title='Lead Follow-Up & AI Automation for Home Service Businesses',
  desc='Answer every call, even from the job site. Missed-call text back, quote follow-up, booking and local ads for US HVAC, plumbing, roofing and more.',
  h1='Answer every call, even when you\'re on a job',
  lead='For HVAC, plumbing, roofing, electrical, cleaning and landscaping businesses: instant replies to every call and form, quote follow-up that doesn\'t rely on memory, and local ads that bring in real jobs.',
  card='Missed-call text back, quote follow-up, job booking and local ads.',
  takeaways=['Home service businesses lose most leads to missed calls while the team is on a job, and to quotes that never get followed up.',
             'Missed-call text back starts a conversation within seconds, so the customer doesn\'t call the next company on the list.',
             'Automated quote follow-up and booking reminders win more of the jobs you already quoted.',
             'Google Ads and Local Services Ads work best for urgent, high-intent searches, as long as every lead gets an instant reply.'],
  pains_h='Why do home service businesses miss so many jobs?',
  pains_a='Because the people who answer the phone are usually up a ladder or under a sink. Urgent customers call the first company that picks up.',
  pains=[('Missed calls on the job','You can\'t answer while you\'re working, and an urgent customer won\'t wait for a call back.'),
         ('Quotes that go quiet','Estimates get sent and then forgotten, even though many customers just needed a nudge.'),
         ('Busy and quiet seasons','Work floods in during peak season and dries up after, with no plan to fill the gaps.'),
         ('Paying for leads that go nowhere','Lead sites and ads bring enquiries, but slow replies mean competitors win them.')],
  fix_h='How does automation help a home service business?',
  fix_a='It replies to every call and form in seconds, books jobs and follows up on quotes automatically, so you win more work without spending evenings on the phone.',
  fixes=[('Missed-call text back','Every missed call gets a text within seconds asking what they need and offering to book.','ai'),
         ('AI booking assistant','Answers common questions on your website and social pages, collects job details and photos, and books a visit.','ai'),
         ('Quote follow-up','Friendly automatic follow-ups after every estimate until the customer says yes or no.','lg'),
         ('Reminders & on-my-way texts','Appointment reminders and arrival updates that cut no-shows and missed visits.','ai'),
         ('Local search ads','Google Ads and Local Services Ads for urgent searches like "AC repair near me" or "emergency plumber".','ga'),
         ('Reviews & repeat work','Review requests after each job and seasonal reminders for maintenance and tune-ups.','lg')],
  journey=['A homeowner\'s AC stops working on a Saturday and they call you while you\'re on another job.',
           'They instantly get a text: sorry we missed you, what\'s going on and where are you located?',
           'They reply with the problem and a photo, and pick a visit time from the link.',
           'They get a reminder before the visit and an on-my-way text on the day.',
           'After the job, they get a thank-you, a review request and later a maintenance reminder.'],
  fit=['HVAC, plumbing and electrical contractors','Roofing, remodeling and home improvement companies','Cleaning, pest control and landscaping businesses','Owner-operators who are on the tools most of the day'],
  faq=[('Does missed-call text back work with my business number?','In most cases, yes. It can usually be added to your existing number through your phone provider or a business texting tool, so customers keep calling the number they already know.'),
       ('Can it give prices or quotes?','It can share starting prices or ranges you approve and collect the details and photos you need to quote. Final quotes stay with you, so nothing is promised that you haven\'t signed off on.'),
       ('Will it work with my scheduling or field service software?','Often, yes. Many field service tools can connect directly or through automation platforms. If not, bookings can go into a calendar with an alert to you or your office.')],
  rel=['ai','ga','hvacmissed']),
 dict(slug='med-spa', name='Med Spas & Aesthetics', short='Med spa', forname='med spas & aesthetics clinics', biz='clinic', who='client',
  title='Lead Generation & AI Booking for Med Spas | Aftab Ahmed',
  desc='Turn ad leads into booked consultations. Instant replies, AI booking, reminders and Facebook and Instagram ads for US med spas and aesthetics clinics.',
  h1='Turn ad leads into booked consultations',
  lead='For med spas and aesthetics clinics: Instagram and Facebook ads with offers people act on, instant replies to every lead, and booking and reminders that keep your treatment rooms full.',
  card='Offer-led Meta ads, instant replies, AI booking and rebooking reminders.',
  takeaways=['Med spa leads are often impulse-driven, so the first few minutes after someone enquires matter most.',
             'Instant text and DM replies with a booking link turn more ad leads into consultations.',
             'Reminders and deposits reduce no-shows, and rebooking messages bring clients back for repeat treatments.',
             'Facebook and Instagram ads work well for med spas when the offer, the creative and the follow-up work together.'],
  pains_h='Why don\'t med spa ad leads turn into bookings?',
  pains_a='Usually because the follow-up is slower than the interest. Someone fills in a form on a whim, and by the time the clinic calls back the moment has passed.',
  pains=[('Leads that cool off fast','People enquire on impulse from an Instagram ad and lose interest within hours.'),
         ('DMs and forms everywhere','Enquiries arrive through Instagram, Facebook, website chat and forms, and some get missed.'),
         ('No-shows on consultations','Free consultations get booked and then forgotten, leaving empty slots.'),
         ('One-time clients','Clients come in once and never get a timely nudge to rebook their next treatment.')],
  fix_h='How can a med spa get more booked consultations?',
  fix_a='By pairing strong offers and creative with instant follow-up, so every lead is contacted while they\'re still interested, and by automating reminders and rebooking.',
  fixes=[('Offer-led Meta ads','Facebook and Instagram campaigns with clear, compliant offers and creative built to stop the scroll.','fb'),
         ('Instant lead replies','Every form, DM and chat gets a reply within seconds with answers and a booking link.','ai'),
         ('AI booking assistant','Answers common questions about treatments, pricing ranges and downtime, then books a consultation.','ai'),
         ('Reminders & deposits','Automatic reminders and optional deposits so booked consultations actually show up.','ai'),
         ('Rebooking & memberships','Timed reminders when clients are due for their next treatment, plus membership offers.','lg'),
         ('Reviews & referrals','Review requests after visits and simple referral prompts for happy clients.','lg')],
  journey=['Someone sees your Instagram ad for a skin treatment and taps to learn more.',
           'They fill in a short form and get a text within seconds answering their question.',
           'They book a consultation from the link, with a reminder the day before.',
           'After the treatment, they get aftercare tips and a review request.',
           'When they\'re due for their next session, they get a friendly rebooking reminder.'],
  fit=['Med spas offering injectables, laser and skin treatments','Aesthetics, skin and laser clinics','Wellness, IV therapy and weight-loss clinics','Clinics running ads that bring leads but not bookings'],
  faq=[('Are there rules for med spa advertising on Facebook and Instagram?','Yes. Meta has policies on health and cosmetic ads, such as avoiding before-and-after claims that imply guaranteed results or target body image negatively. Campaigns are written to stay within those policies and any rules that apply to your services.'),
       ('Can the AI answer questions about treatments?','It can answer general questions you approve, such as what a treatment involves, typical downtime and price ranges. Medical questions and suitability are always handed to your licensed staff.'),
       ('Will this work with my booking software?','Usually, yes. Most med spa booking platforms can connect directly or through automation tools, so appointments land in the calendar you already use.')],
  rel=['fb','ai','fbcalls']),
 dict(slug='law', name='Law Firms', short='Law firm', forname='law firms', biz='firm', who='client',
  title='Client Intake Automation & Lead Generation for Law Firms',
  desc='Never lose a potential client to voicemail. AI intake, instant follow-up, consultation booking and Google Ads for US law firms and solo attorneys.',
  h1='Never lose a potential client to voicemail',
  lead='For law firms and solo attorneys: intake that answers around the clock, screens for the cases you take, books consultations and follows up, so good cases don\'t go to the firm that answered first.',
  card='24/7 intake, case screening, consultation booking and Google Ads.',
  takeaways=['Many people contact several firms and hire the one that responds first and makes the next step easy.',
             'An AI intake assistant can answer around the clock, ask screening questions and book consultations, with no legal advice given.',
             'Automated follow-up and reminders reduce missed consultations and lost leads.',
             'Google Ads for specific practice areas work best when intake is instant and every lead is tracked.'],
  pains_h='Where do law firms lose potential clients?',
  pains_a='At intake. Calls go to voicemail, web forms wait until the next business day, and potential clients keep searching until someone responds.',
  pains=[('Calls to voicemail','Attorneys are in court or with clients, and callers rarely leave a message.'),
         ('Slow web-form replies','Forms submitted at night or on weekends wait until Monday, by which time the person has hired someone else.'),
         ('Time spent on poor-fit enquiries','Staff spend hours on calls about practice areas or locations the firm doesn\'t handle.'),
         ('Unclear marketing results','It\'s hard to tell which ads and sources produce signed cases, not just calls.')],
  fix_h='How can a law firm automate client intake?',
  fix_a='With an intake assistant that responds instantly, asks your screening questions, books consultations for good-fit cases and routes everything else politely, without ever giving legal advice.',
  fixes=[('24/7 intake assistant','Answers on your website and by text, collects contact details and the basics of the matter, and explains next steps.','ai'),
         ('Case screening','Asks your screening questions (practice area, location, timing) and flags good-fit cases to you immediately.','ai'),
         ('Consultation booking','Qualified prospects book a consultation in your calendar, with reminders and easy rescheduling.','ai'),
         ('Missed-call text back','Callers who reach voicemail get a text within seconds so the conversation continues.','ai'),
         ('Practice-area search ads','Google Ads for specific case types and locations, with landing pages written for each.','ga'),
         ('Source tracking','Every lead tagged by source so you can see which marketing produces consultations and signed cases.','lg')],
  journey=['Someone searches for a lawyer for their type of case late in the evening and finds your page.',
           'Your intake assistant responds immediately and asks a few screening questions.',
           'Their matter fits your practice, so they book a consultation from your calendar.',
           'You get a summary of the enquiry, and they get reminders before the appointment.',
           'If the matter isn\'t a fit, they get a polite reply and, if you like, a referral resource.'],
  fit=['Personal injury, family and criminal defense firms','Immigration, estate planning and employment law practices','Solo attorneys and small firms without a full-time intake team','Firms running ads that bring calls but few consultations'],
  faq=[('Will the AI give legal advice?','No. It is set up only to handle intake: collecting contact details and basic facts, answering general questions about your firm and booking consultations. It makes clear that no attorney-client relationship is formed and that legal questions go to an attorney.'),
       ('What about confidentiality?','The intake assistant collects only what\'s needed to screen and book, and the tools are chosen with confidentiality in mind. Anything sensitive is handed to your team, and the setup is reviewed with you before launch.'),
       ('Does it follow attorney advertising rules?','Ads and intake messages are written to avoid guarantees and misleading claims. Advertising rules vary by state, so final wording is reviewed by you before anything goes live.')],
  rel=['ai','ga','lg']),
]

def head(title, desc, url, ld, extra=''):
    return f'''<!doctype html>
<html lang="en">
<head>
{TRACK_HEAD}
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow">
<meta name="author" content="Aftab Ahmed">
<meta name="theme-color" content="#0A0A0A">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Aftab Ahmed">
<meta property="og:locale" content="en_US">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{U}images/aftab-cutout.webp">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{ICON}">
<link rel="alternate" type="application/rss+xml" title="Aftab Ahmed Blog" href="/feed.xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,500..900&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{extra}../blog/blog.css">
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False)}
</script>
</head>
<body>
{TRACK_BODY}
'''

def topbar(up):
    return f'<header class="top"><div class="wrap"><a class="logo" href="{up}">AFTAB <span>AHMED</span></a><a class="btn" href="{up}#book">Book a call</a></div></header>\n'

def foot(up):
    return f'''<footer><div class="wrap"><span>© 2026 Aftab Ahmed · AI, Automation &amp; Marketing</span><nav><a href="{up}">Home</a><a href="{up}industries/">Industries</a><a href="{up}blog/">Blog</a><a href="{up}#book">Book a call</a><a href="{up}privacy/">Privacy</a></nav></div></footer>
</body>
</html>
'''

def page(it):
    url = f"{U}industries/{it['slug']}/"
    ld = {"@context":"https://schema.org","@graph":[
      {"@type":"Service","name":f"AI automation & lead generation for {it['name'].lower()}","url":url,"description":it['desc'],
       "serviceType":"AI automation and lead generation",
       "audience":{"@type":"BusinessAudience","name":it['name']},
       "provider":{"@type":"Person","@id":U+"#person","name":"Aftab Ahmed","url":U},
       "areaServed":{"@type":"Country","name":"United States"}},
      {"@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":U},
        {"@type":"ListItem","position":2,"name":"Industries","item":U+"industries/"},
        {"@type":"ListItem","position":3,"name":it['name'],"item":url}]},
      {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in it['faq']]}]}
    tk = ''.join(f'<li>{e(x)}</li>' for x in it['takeaways'])
    pains = ''.join(f'<div><b>{e(a)}</b><p>{e(b)}</p></div>' for a,b in it['pains'])
    fixes = ''.join(f'<div><b>{e(a)}</b><p>{e(b)}</p></div>' for a,b,_ in it['fixes'])
    used = []
    for _,_,k in it['fixes']:
        if k not in used: used.append(k)
    svc_links = ', '.join(f'<a href="../../{SV[k][1]}">{e(SV[k][0])}</a>' for k in used)
    journey = ''.join(f'<li>{e(x)}</li>' for x in it['journey'])
    fit = ''.join(f'<li>{e(x)}</li>' for x in it['fit'])
    faq = ''.join(f'<h3>{e(q)}</h3><p>{e(a)}</p>' for q,a in it['faq'])
    rel = ''
    for k in it['rel']:
        t,u = SV[k] if k in SV else POSTS[k]
        rel += f'<li><a href="../../{u}">{e(t[0].upper() + t[1:])}</a></li>'
    rel += ''.join(f'<li><a href="../{o["slug"]}/">For {e(o["forname"])}</a></li>' for o in I if o is not it)
    return head(it['title'] + ' | Aftab Ahmed' if len(it["title"]) < 40 else it['title'], it['desc'], url, ld, '../') + topbar('../../') + f'''
<section class="hero"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="../../">Home</a><span>/</span><a href="../">Industries</a><span>/</span>{e(it['name'])}</nav>
  <div class="kicker">{e(it['name'])} · United States</div>
  <h1>{e(it['h1'])}</h1>
  <p class="lead">{e(it['lead'])}</p>
  <a class="btn" href="../../#book">Book a free 30-minute call →</a>
</div></section>

<article>
  <div class="takeaways"><b>At a glance</b><ul>{tk}</ul></div>

  <h2 id="problems">{e(it['pains_h'])}</h2>
  <p>{e(it['pains_a'])}</p>
  <div class="svc-grid pains" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr))">{pains}</div>

  <h2 id="solution">{e(it['fix_h'])}</h2>
  <p>{e(it['fix_a'])} It combines {svc_links}, set up around the way your {e(it['short'].lower())} {it['biz']} already works.</p>
  <div class="svc-grid">{fixes}</div>

  <h2 id="journey">What does this look like for a new {it.get('who', 'patient' if it['slug']=='dental' else 'client' if it['slug']=='accounting' else 'lead')}?</h2>
  <ol class="steps">{journey}</ol>

  <div class="callout">You stay in control: anything sensitive, complex or high-value is handed to you or your team, with the full conversation attached.</div>

  <h2 id="fit">Who is this for?</h2>
  <ul class="check">{fit}</ul>

  <h2 id="process">How do we get started?</h2>
  <ol class="steps">
    <li><strong>Book a call.</strong> 30 minutes on where your business is losing time or leads right now.</li>
    <li><strong>Get a clear plan.</strong> What to build first and why, with the tools you already use, before anything is built.</li>
    <li><strong>We build, you grow.</strong> I set it up, test it on real scenarios and hand it over running, with clear reporting.</li>
  </ol>

  <h2 id="faq">FAQ</h2>
  {faq}

  <div class="related"><b>Related</b><ul>{rel}</ul></div>

  <div class="cta">
    <h2>See what this could look like for your {it['biz']}</h2>
    <p>Book a free 30-minute call. You'll leave with a clear idea of what's possible, whether we work together or not.</p>
    <a class="btn" href="../../#book">Book a free call →</a>
  </div>
</article>

''' + foot('../../')

def hub():
    url = U + 'industries/'
    title = 'Industries: AI Automation & Lead Generation | Aftab Ahmed'
    desc = 'AI automation, follow-up and lead generation built for specific US industries: dental, real estate, accounting, home services, med spas and law firms.'
    ld = {"@context":"https://schema.org","@graph":[
      {"@type":"CollectionPage","name":"Industries","url":url,"description":desc,"about":{"@id":U+"#service"},
       "hasPart":[{"@type":"WebPage","name":it['name'],"url":f"{U}industries/{it['slug']}/"} for it in I]},
      {"@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":U},
        {"@type":"ListItem","position":2,"name":"Industries","item":url}]}]}
    cards = ''.join(f'''
  <a class="card" href="{it['slug']}/">
    <div class="kicker">{e(it['name'])}</div>
    <h2>{e(it['h1'])}</h2>
    <p>{e(it['card'])}</p>
    <span>See how it works →</span>
  </a>''' for it in I)
    return head(title, desc, url, ld, '') + topbar('../') + f'''
<section class="hero"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="../">Home</a><span>/</span>Industries</nav>
  <div class="kicker">Industries</div>
  <h1>Built for the way your industry works</h1>
  <p class="lead">Every industry loses leads and time in different places. These pages show where that happens and how AI automation, follow-up and ads fix it.</p>
</div></section>

<main class="wrap"><div class="cards">{cards}
</div>
<div class="related" style="margin:0 0 60px"><b>Don't see your industry?</b><p style="margin:0;color:var(--muted)">I also work with other local and service businesses, from fitness studios to auto shops. <a href="../#book" style="color:var(--red-text)">Book a free call</a> and we'll look at where your business is losing leads.</p></div>
</main>

''' + foot('../')

os.makedirs(f'{ROOT}/industries', exist_ok=True)
open(f'{ROOT}/industries/index.html', 'w').write(hub())
for it in I:
    d = f"{ROOT}/industries/{it['slug']}"; os.makedirs(d, exist_ok=True)
    open(f"{d}/index.html", 'w').write(page(it))
print('ok', len(I))

def privacy():
    url = U + 'privacy/'
    title = 'Privacy Policy | Aftab Ahmed'
    desc = 'How iamaftabahmed.com collects, uses and protects your information, including analytics, advertising cookies, bookings and email.'
    ld = {"@context":"https://schema.org","@graph":[{"@type":"WebPage","name":"Privacy Policy","url":url,"description":desc,"dateModified":"2026-10-01","publisher":{"@id":U+"#person"}},
      {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":U},{"@type":"ListItem","position":2,"name":"Privacy Policy","item":url}]}]}
    return head(title, desc, url, ld, '') + topbar('../') + """
<section class="hero"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="../">Home</a><span>/</span>Privacy Policy</nav>
  <div class="kicker">Legal</div>
  <h1>Privacy Policy</h1>
  <p class="lead">Plain-English details on what information this website collects, why, and the choices you have.</p>
  <div class="meta">Last updated: October 1, 2026</div>
</div></section>

<article>
  <p>This policy covers iamaftabahmed.com (the "site"), run by Aftab Ahmed ("I", "me"). If you have any questions, email <a href="mailto:hello@iamaftabahmed.com">hello@iamaftabahmed.com</a>.</p>

  <h2 id="collect">What information do I collect?</h2>
  <ul>
    <li><strong>Information you give me.</strong> When you book a call, email me or message me, I receive what you share, such as your name, email address, phone number, company and details about your project.</li>
    <li><strong>Usage information.</strong> Like most websites, the site collects information about how it's used: pages visited, clicks, approximate location (city or country), device and browser type, and how you arrived at the site.</li>
    <li><strong>Cookies and similar technologies.</strong> Small files and scripts used for analytics and advertising, described below.</li>
  </ul>

  <h2 id="tools">Which tools does this site use?</h2>
  <ul>
    <li><strong>Google Analytics and Google Tag Manager</strong> to understand how visitors use the site. <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">How Google uses data</a>.</li>
    <li><strong>Meta Pixel</strong> (Facebook and Instagram) to measure ads and show relevant ads to people who visited the site. <a href="https://www.facebook.com/privacy/policy" rel="noopener">Meta's privacy policy</a>.</li>
    <li><strong>Microsoft Clarity</strong> to see how pages are used (for example clicks and scrolling) so I can improve them. <a href="https://privacy.microsoft.com/privacystatement" rel="noopener">Microsoft's privacy statement</a>.</li>
    <li><strong>Cal.com</strong> to schedule calls. The details you enter in the booking form are processed by Cal.com. <a href="https://cal.com/privacy" rel="noopener">Cal.com's privacy policy</a>.</li>
    <li><strong>YouTube</strong> for embedded videos, which may set cookies when you play a video.</li>
  </ul>

  <h2 id="use">How is your information used?</h2>
  <ul class="check">
    <li>To reply to you, schedule calls and deliver any work we agree on</li>
    <li>To understand which pages and marketing are useful, and improve the site</li>
    <li>To measure and improve advertising, including showing ads to past visitors</li>
    <li>To keep the site secure and meet legal obligations</li>
  </ul>
  <p>I don't sell your personal information for money. Some states treat sharing data with advertising platforms for targeted ads as a "sale" or "sharing"; you can opt out as described below.</p>

  <h2 id="choices">What choices do you have?</h2>
  <ul>
    <li><strong>Cookies:</strong> you can block or delete cookies in your browser settings. The site still works without them.</li>
    <li><strong>Google Analytics:</strong> install the <a href="https://tools.google.com/dlpage/gaoptout" rel="noopener">Google Analytics opt-out add-on</a>.</li>
    <li><strong>Ads:</strong> adjust your <a href="https://www.facebook.com/adpreferences" rel="noopener">Meta ad preferences</a> and <a href="https://myadcenter.google.com/" rel="noopener">Google ad settings</a>, or use the <a href="https://optout.aboutads.info/" rel="noopener">Digital Advertising Alliance opt-out</a>.</li>
    <li><strong>Global Privacy Control:</strong> if your browser sends a GPC signal, it is treated as a request to opt out of targeted advertising where the law requires it.</li>
    <li><strong>Your rights:</strong> depending on where you live (for example California or other US states, the UK or the EU), you may have the right to access, correct or delete your personal information, or to opt out of targeted advertising. Email <a href="mailto:hello@iamaftabahmed.com">hello@iamaftabahmed.com</a> and I'll respond within the time the law requires.</li>
  </ul>

  <h2 id="keep">How long is information kept, and is it safe?</h2>
  <p>Messages and booking details are kept as long as needed to work with you and for normal business records, then deleted. Analytics data is kept according to each tool's retention settings. Reasonable steps are taken to protect your information, but no website or online service can be guaranteed 100% secure.</p>

  <h2 id="other">Anything else?</h2>
  <p>This site isn't meant for children under 13, and I don't knowingly collect their information. Links to other websites are covered by those sites' own policies. If this policy changes, the updated version will be posted on this page with a new date.</p>

  <h2 id="contact">How can you contact me?</h2>
  <p>Email <a href="mailto:hello@iamaftabahmed.com">hello@iamaftabahmed.com</a> with any privacy question or request.</p>
</article>

""" + foot('../')

os.makedirs(f'{ROOT}/privacy', exist_ok=True)
open(f'{ROOT}/privacy/index.html', 'w').write(privacy())
print('privacy ok')
