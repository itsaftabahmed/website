// Inner-page menu (mobile toggle, dropdowns) and blog reading progress bar.
(function () {
  var top = document.querySelector('.top'), burger = document.querySelector('.nav__burger');
  if (burger) burger.addEventListener('click', function () {
    var open = top.classList.toggle('open'); burger.setAttribute('aria-expanded', open);
  });
  document.querySelectorAll('.nav__dd > button').forEach(function (b) {
    b.addEventListener('click', function (e) {
      var dd = b.parentNode, open = !dd.classList.contains('open');
      document.querySelectorAll('.nav__dd.open').forEach(function (d) { d.classList.remove('open'); d.firstChild.setAttribute('aria-expanded', 'false'); });
      dd.classList.toggle('open', open); b.setAttribute('aria-expanded', open); e.stopPropagation();
    });
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.nav__dd')) document.querySelectorAll('.nav__dd.open').forEach(function (d) { d.classList.remove('open'); });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { document.querySelectorAll('.nav__dd.open').forEach(function (d) { d.classList.remove('open'); }); if (top) top.classList.remove('open'); }
  });
  var art = document.querySelector('article'), toc = document.querySelector('.toc');
  if (art && toc) {
    var bar = document.createElement('div'); bar.className = 'prog'; document.body.appendChild(bar);
    var links = [].slice.call(toc.querySelectorAll('a[href^="#"]')), heads = links.map(function (a) { return document.getElementById(a.getAttribute('href').slice(1)); });
    var tick = function () {
      var r = art.getBoundingClientRect(), h = r.height - innerHeight;
      bar.style.width = Math.max(0, Math.min(1, h > 0 ? -r.top / h : 0)) * 100 + '%';
      var cur = -1; heads.forEach(function (el, i) { if (el && el.getBoundingClientRect().top < 140) cur = i; });
      links.forEach(function (a, i) { a.classList.toggle('on', i === cur); });
    };
    addEventListener('scroll', tick, { passive: true }); addEventListener('resize', tick); tick();
  }
})();
