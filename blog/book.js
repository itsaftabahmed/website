// Booking pop-up: "Book a call" buttons open the Cal.com calendar in a modal on every page.
// On the homepage, #book links scroll to the contact section instead (its "Pick a time" button opens the pop-up).
(function () {
  var me = document.currentScript && document.currentScript.src;
  if (me && !document.querySelector('link[href*="book.css"]')) {   // load the pop-up styles even where a cached stylesheet lacks them
    var l = document.createElement('link'); l.rel = 'stylesheet'; l.href = me.replace(/book\.js(\?.*)?$/, 'book.css'); document.head.appendChild(l);
  }
  var HOME = !!document.querySelector('.ct#contact');
  var CAL_LINK = 'aftab-ahmed-4rjr3m/30min', NS = '30min', modal, booted = false, lastFocus;
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  function track(ev, extra) { (window.dataLayer = window.dataLayer || []).push(Object.assign({ event: ev }, extra || {})); }
  function boot() {
    if (booted) return; booted = true;
    (function (C, A, L) { var p = function (a, ar) { a.q.push(ar); }; var d = C.document; C.Cal = C.Cal || function () { var cal = C.Cal; var ar = arguments; if (!cal.loaded) { cal.ns = {}; cal.q = cal.q || []; d.head.appendChild(d.createElement('script')).src = A; cal.loaded = true; } if (ar[0] === L) { var api = function () { p(api, arguments); }; var namespace = ar[1]; api.q = api.q || []; if (typeof namespace === 'string') { cal.ns[namespace] = cal.ns[namespace] || api; p(cal.ns[namespace], ar); p(cal, ['initNamespace', namespace]); } else p(cal, ar); return; } p(cal, ar); }; })(window, 'https://app.cal.com/embed/embed.js', 'init');
    Cal('init', NS, { origin: 'https://app.cal.com' });
    Cal.ns[NS]('inline', { elementOrSelector: '#bkCal', config: { layout: 'month_view', useSlotsViewOnSmallScreen: 'true', theme: 'dark' }, calLink: CAL_LINK });
    Cal.ns[NS]('ui', { theme: 'dark', cssVarsPerTheme: { dark: { 'cal-brand': '#E01119' } }, hideEventTypeDetails: true, layout: 'month_view' });
    Cal.ns[NS]('on', { action: 'bookingSuccessful', callback: function () {
      track('booking_completed', { booking_type: '30min' });
      if (window.fbq) fbq('track', 'Schedule');
      if (window.gtag) gtag('event', 'generate_lead', { method: 'cal_booking', booking_type: '30min' });
    } });
  }
  function build() {
    modal = document.createElement('div'); modal.className = 'bk'; modal.hidden = true;
    modal.innerHTML = '<div class="bk__ov" data-close></div><div class="bk__box" role="dialog" aria-modal="true" aria-labelledby="bkT">'
      + '<button type="button" class="bk__x" data-close aria-label="Close">✕</button>'
      + '<div class="bk__head"><div class="bk__k">Book a call</div><h2 id="bkT">Pick a time that suits you</h2><p>30 minutes, no pressure: a clear look at how AI, automation and marketing can grow your business.</p></div>'
      + '<div id="bkCal" class="bk__cal"><div class="bk__load"><i></i><i></i><i></i></div></div>'
      + '<p class="bk__alt">Calendar not loading? <a href="https://cal.com/' + CAL_LINK + '" target="_blank" rel="noopener">Open it in a new tab</a> · or <a href="mailto:hello@iamaftabahmed.com">email me</a></p></div>';
    document.body.appendChild(modal);
    modal.addEventListener('click', function (e) { if (e.target.closest('[data-close]')) close(); });
  }
  function open() {
    if (!modal) build();
    lastFocus = document.activeElement; modal.hidden = false; document.documentElement.classList.add('bk-lock');
    requestAnimationFrame(function () { modal.classList.add('open'); });
    boot(); modal.querySelector('.bk__x').focus();
    track('booking_popup_open', { page_path: location.pathname });
  }
  function close() {
    if (!modal || modal.hidden) return;
    modal.classList.remove('open'); document.documentElement.classList.remove('bk-lock');
    setTimeout(function () { modal.hidden = true; }, reduce ? 0 : 250);
    if (lastFocus && lastFocus.focus) lastFocus.focus();
    if (location.hash === '#call' || (!HOME && location.hash === '#book')) history.replaceState(null, '', location.pathname + location.search);
  }
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest(HOME ? '[data-book], a[href$="#call"]' : '[data-book], a[href$="#call"], a[href$="#book"]');
    if (!a || e.metaKey || e.ctrlKey || e.shiftKey) return;
    if (a.href) { var url = new URL(a.href, location.href); if (url.origin !== location.origin) return; }
    e.preventDefault(); open();
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
  window.openBooking = open;
  if (location.hash === '#call' || (!HOME && location.hash === '#book')) { if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', open); else open(); }
})();
