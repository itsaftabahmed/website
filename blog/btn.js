// Buttons: on hover the letters roll up one by one, a trailing arrow swaps, and the button pulls gently toward the mouse.
// Runs on every page (loaded from the shared footer). Styles live in blog/blog.css and the homepage's inline CSS.
(function () {
  // Only run when the matching CSS is loaded, so a stale cached stylesheet never shows raw letter spans.
  if (getComputedStyle(document.documentElement).getPropertyValue('--btn-roll').trim() !== '1') return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var NS = 'http://www.w3.org/2000/svg';

  function arrow(cls) {
    var s = document.createElementNS(NS, 'svg'), p = document.createElementNS(NS, 'path');
    s.setAttribute('class', cls); s.setAttribute('viewBox', '0 0 24 24'); s.setAttribute('fill', 'none'); s.setAttribute('stroke', 'currentColor');
    s.setAttribute('stroke-width', '2.5'); s.setAttribute('stroke-linecap', 'round'); s.setAttribute('stroke-linejoin', 'round');
    p.setAttribute('d', 'M4.5 12h15M13 5.5l6.5 6.5-6.5 6.5'); s.appendChild(p); return s;
  }

  // Each character sits in a small window; its copy (CSS ::after) waits below and rolls into place on hover.
  // The text itself appears once in the page, so links keep clean anchor text and labels.
  function roll(text) {
    var r = document.createElement('span'), i = 0; r.className = 'roll';
    text.split(/(\s+)/).forEach(function (part) {
      if (!part) return;
      var w = document.createElement('span'); w.className = /^\s+$/.test(part) ? 'rsp' : 'rw';
      Array.from(/^\s+$/.test(part) ? ' ' : part).forEach(function (c) {
        var ch = document.createElement('span'), t = document.createElement('span');
        ch.className = 'ch'; ch.style.setProperty('--i', i++);
        t.setAttribute('data-c', c); t.textContent = c; ch.appendChild(t); w.appendChild(ch);
      });
      r.appendChild(w);
    });
    return r;
  }

  function wrap(el) {
    if (el.__roll || el.getAttribute('data-roll') === 'off') return;
    var nodes = [].slice.call(el.childNodes), text = '', before = [], tail = false;
    for (var k = 0; k < nodes.length; k++) {
      var n = nodes[k];
      if (n.nodeType === 3) text += n.nodeValue;
      else if (n.nodeName.toLowerCase() === 'svg') { if (text.trim()) tail = true; else before.push(n); }   // icon before the text stays; one after it is the arrow
      else if (n.nodeType === 1) return;   // anything richer is left exactly as written
    }
    text = text.replace(/\s+/g, ' ').trim();
    if (/\s*→$/.test(text)) { text = text.replace(/\s*→$/, ''); tail = true; }
    if (!text) return;
    el.__roll = true;
    var inner = document.createElement('span'); inner.className = 'btn__in';
    before.forEach(function (n) { inner.appendChild(n); });
    inner.appendChild(roll(text));
    if (tail) { var s = document.createElement('span'); s.className = 'swap'; s.setAttribute('aria-hidden', 'true'); s.appendChild(arrow('i1')); s.appendChild(arrow('i2')); inner.appendChild(s); }
    el.textContent = ''; el.appendChild(inner);
    if (!el.hasAttribute('aria-label')) el.setAttribute('aria-label', text);
  }

  // Magnetic pull for mouse users: the button leans toward the cursor and its label leans a little further.
  function magnet(el) {
    if (el.__mag) return; el.__mag = true;
    var clamp = function (v, m) { return Math.max(-m, Math.min(m, v)); };
    el.addEventListener('mousemove', function (e) {
      var r = el.getBoundingClientRect(), x = e.clientX - r.left - r.width / 2, y = e.clientY - r.top - r.height / 2, inner = el.querySelector('.btn__in');
      el.classList.remove('out');
      el.style.transform = 'translate(' + clamp(x * .18, 14) + 'px,' + clamp(y * .32, 8) + 'px)';
      if (inner) inner.style.transform = 'translate(' + clamp(x * .08, 6) + 'px,' + clamp(y * .14, 4) + 'px)';
    });
    el.addEventListener('mouseleave', function () {
      var inner = el.querySelector('.btn__in');
      el.classList.add('out'); el.style.transform = ''; if (inner) inner.style.transform = '';
    });
  }

  var fine = matchMedia('(hover: hover) and (pointer: fine)').matches;
  function run(scope) {
    [].forEach.call((scope || document).querySelectorAll('.btn'), function (el) { wrap(el); if (fine) magnet(el); });
  }
  window.rollButtons = run;
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { run(); }); else run();
})();
