// AI receptionist demo. Uses the Cloudflare Worker when WORKER_URL is set; otherwise (or on any error) a guided script.
(function () {
  var API = 'https://site-api.itsaftabahmedhere.workers.dev';   // site Worker, e.g. 'https://site-api.yourname.workers.dev' (see _tools/site-worker)
  var WORKER_URL = API ? API + '/demo' : '';
  var BIZ = {
    dental: { tab: 'Dental', name: 'Bright Smile Dental', av: 'BS', hi: 'Hi, this is Bright Smile Dental! How can I help you today?', who: 'Dr. Lee', visit: 'visit',
      chips: ['I have a toothache, can I come in tomorrow?', 'Do you take my insurance?', 'What are your hours?'],
      hours: 'We\'re open Mon to Fri 8 am to 5 pm and Sat 9 am to 1 pm.', price: 'It depends on the treatment, and we accept most PPO plans. The team confirms your coverage before the visit.', extra: [/insur|ppo|cover/, 'We accept most PPO dental plans, and the team confirms your coverage before your visit.'] },
    hvac: { tab: 'HVAC', name: 'Cool Air Heating & Cooling', av: 'CA', hi: 'Hi, this is Cool Air Heating & Cooling! What\'s going on with your system?', who: 'a technician', visit: 'service visit',
      chips: ['My AC is blowing warm air', 'How much is a service call?', 'Do you work weekends?'],
      hours: 'We\'re open Mon to Sat 7 am to 7 pm, with emergency service 24/7.', price: 'The diagnostic visit is $89, and it\'s credited toward the repair.', extra: [/gas|carbon|smell/, 'If you smell gas or a CO alarm is going off, please leave the home and call 911 or your gas company first. I\'m alerting our team now.'] },
    law: { tab: 'Law firm', name: 'Carter & Hayes Law', av: 'CH', hi: 'Hi, this is Carter & Hayes Law. I can help you set up a free consultation. What kind of matter is it?', who: 'an attorney', visit: 'free consultation',
      chips: ['I was in a car accident last week', 'How much is a consultation?', 'Can I talk to a lawyer today?'],
      hours: 'The office is open Mon to Fri 9 am to 5:30 pm.', price: 'The first 20-minute consultation is free. An attorney explains fees on that call.', extra: [/advice|should i|can i sue|what do i do/, 'I can\'t give legal advice, but an attorney can on a free consultation. Please don\'t share confidential details here.'] },
    medspa: { tab: 'Med spa', name: 'Glow Studio Med Spa', av: 'GS', hi: 'Hi, welcome to Glow Studio! Are you looking for a treatment or a free skin consultation?', who: 'a provider', visit: 'free consultation',
      chips: ['How much is laser hair removal?', 'Do you have Saturday appointments?', 'I want to book a facial'],
      hours: 'We\'re open Tue to Sat 10 am to 7 pm.', price: 'Pricing depends on your treatment plan, so we start with a free 15-minute consultation.', extra: [/safe|side effect|pregnan|medical/, 'That\'s a great question for a provider. I can book you a free consultation so they can answer it properly.'] },
    realestate: { tab: 'Real estate', name: 'Parkside Realty', av: 'PR', hi: 'Hi, this is Parkside Realty! Are you looking to buy or sell?', who: 'Jordan', visit: 'showing',
      chips: ['Is the house on Oak St still available?', 'I want to know what my home is worth', 'Can I see it this weekend?'],
      hours: 'We\'re available every day 9 am to 7 pm.', price: 'A home valuation call is free. I can book one with Jordan.', extra: [/worth|valu|sell/, 'Happy to help. Jordan can do a free home valuation call. Want me to book one?'] }
  };
  var $ = function (id) { return document.getElementById(id); };
  var log = $('dmLog'), input = $('dmIn'), cur = 'dental', msgs = [], busy = false, state = null;
  var day = function (n) { var d = new Date(); do { d.setDate(d.getDate() + 1); if (d.getDay() !== 0) n--; } while (n > 0); return d.toLocaleDateString('en-US', { weekday: 'short' }); };
  function bubble(cls, text) { var el = document.createElement('div'); el.className = 'b ' + cls; el.textContent = text; log.appendChild(el); log.scrollTop = log.scrollHeight; return el; }
  function typing() { var el = document.createElement('div'); el.className = 'b ai typing'; el.innerHTML = '<i></i><i></i><i></i>'; log.appendChild(el); log.scrollTop = log.scrollHeight; return el; }
  function say(text) { msgs.push({ role: 'assistant', content: text }); if (/^booked:/i.test(text)) bubble('ok', '✓ ' + text); else bubble('ai', text); }
  // ---- guided script (no AI needed) ----
  function guided(text) {
    var b = BIZ[cur], t = text.toLowerCase(), t1 = day(1) + ' 9:30 am', t2 = day(1) + ' 2:00 pm';
    if (state && state.step === 'time') { state.time = /2|after|pm/.test(t) && !/9|morn|am\b/.test(t) ? t2 : t1; state.step = 'name'; return 'Great, ' + state.time + ' it is. What\'s your first name?'; }
    if (state && state.step === 'name') { var name = (text.match(/[A-Za-z]+/g) || ['there']).pop(); name = name.charAt(0).toUpperCase() + name.slice(1).toLowerCase(); var tm = state.time; state = null; return 'Booked: ' + name + ', ' + tm + ' with ' + b.who + '. You\'ll get a text reminder the day before.'; }
    if (b.extra[0].test(t)) return b.extra[1];
    if (/hour|open|close|weekend|saturday|sunday|when are/.test(t)) return b.hours + ' Want me to book you a ' + b.visit + '?';
    if (/price|cost|how much|fee|charge|\$/.test(t)) return b.price + ' Want me to find you a time?';
    if (/human|person|someone|agent|real/.test(t)) return 'Of course. I\'m an AI assistant, and I\'ll pass this to the team right away. Can I book a time for them to call you?';
    if (/\b(ai|bot|robot)\b/.test(t)) return 'I\'m an AI assistant for ' + b.name + '. I can answer questions and book you in. What do you need?';
    state = { step: 'time' }; return 'I can help with that. I have ' + t1 + ' or ' + t2 + ' with ' + b.who + '. Which works better?';
  }
  function reply(text) {
    var done = function (r) { setTimeout(function () { tp.remove(); say(r); busy = false; input.focus({ preventScroll: true }); }, 500); };
    var tp = typing(); busy = true;
    if (!WORKER_URL) return done(guided(text));
    fetch(WORKER_URL, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ industry: cur, messages: msgs.slice(-12) }) })
      .then(function (r) { if (!r.ok) throw 0; return r.json(); })
      .then(function (d) { if (!d.reply) throw 0; done(d.reply); })
      .catch(function () { WORKER_URL = ''; done(guided(text)); });   // fall back to the guided script
  }
  function send(text) {
    text = (text || '').trim().slice(0, 300); if (!text || busy) return;
    if (msgs.length >= 24) { bubble('ok', 'That\'s the end of the demo. Book a call to get one for your business.'); return; }
    bubble('me', text); msgs.push({ role: 'user', content: text }); input.value = '';
    (window.dataLayer = window.dataLayer || []).push({ event: 'demo_message', industry: cur, n: msgs.length });
    reply(text);
  }
  function start(k) {
    cur = k; msgs = []; state = null; busy = false; log.innerHTML = '';
    var b = BIZ[k]; $('dmName').textContent = b.name; $('dmAv').textContent = b.av;
    [].forEach.call(document.querySelectorAll('.dm__tab'), function (t) { t.classList.toggle('on', t.dataset.k === k); t.setAttribute('aria-selected', t.dataset.k === k); });
    $('dmChips').innerHTML = ''; b.chips.forEach(function (c) { var el = document.createElement('button'); el.type = 'button'; el.className = 'dm__chip'; el.textContent = c; el.onclick = function () { send(c); }; $('dmChips').appendChild(el); });
    say(b.hi);
  }
  Object.keys(BIZ).forEach(function (k) { var t = document.createElement('button'); t.type = 'button'; t.className = 'dm__tab'; t.dataset.k = k; t.setAttribute('role', 'tab'); t.textContent = BIZ[k].tab; t.onclick = function () { start(k); }; $('dmTabs').appendChild(t); });
  $('dmForm').addEventListener('submit', function (e) { e.preventDefault(); send(input.value); });
  var q = (location.hash || '').slice(1); start(BIZ[q] ? q : 'dental');
})();
