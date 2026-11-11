// Lead capture: sends forms marked data-lead to the site Worker (saved in Cloudflare D1, emailed to Aftab).
(function () {
  var API = 'https://site-api.itsaftabahmedhere.workers.dev/lead';
  window.sendLead = function (data) {
    data = Object.assign({ page: location.pathname }, data);
    return fetch(API, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { if (!r.ok || !j.ok) throw new Error(j.error || 'failed'); return j; }); })
      .then(function (j) {
        (window.dataLayer = window.dataLayer || []).push({ event: 'generate_lead', lead_kind: data.kind || 'contact' });
        if (window.fbq) fbq('track', 'Lead'); if (window.gtag) gtag('event', 'generate_lead', { lead_kind: data.kind || 'contact' });
        return j;
      });
  };
  function wire(form) {
    if (form.__lead) return; form.__lead = true;
    var msg = form.querySelector('.lead__msg'), btn = form.querySelector('button[type=submit]');
    form.addEventListener('submit', function (e) {
      e.preventDefault(); if (btn.disabled) return;
      var d = { kind: form.getAttribute('data-lead') || 'contact' };
      [].forEach.call(form.elements, function (el) { if (el.name) d[el.name] = el.value; });
      if (typeof form.leadExtra === 'function') d.extra = form.leadExtra();
      var label = btn.textContent; btn.disabled = true; btn.textContent = 'Sending…'; if (msg) { msg.textContent = ''; msg.className = 'lead__msg'; }
      window.sendLead(d).then(function () {
        form.classList.add('lead--done');
        if (msg) { msg.textContent = form.getAttribute('data-ok') || 'Thanks! I’ll get back to you within one business day.'; msg.className = 'lead__msg ok'; }
        form.reset();
      }).catch(function (err) {
        if (msg) { msg.innerHTML = err.message === 'email' ? 'Please check your email address.' : 'Something went wrong. Please email <a href="mailto:hello@iamaftabahmed.com">hello@iamaftabahmed.com</a>.'; msg.className = 'lead__msg err'; }
      }).then(function () { btn.disabled = false; btn.textContent = label; });
    });
  }
  function init() { [].forEach.call(document.querySelectorAll('form[data-lead]'), wire); }
  window.wireLeadForms = init;
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
