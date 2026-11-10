// Announcement capsule: pop-up entrance (first page of a visit only) and message rotation.
(function () {
  var box = document.querySelector('.ann'); if (!box) return;
  var link = box.querySelector('.ann__in'), ms = [].slice.call(box.querySelectorAll('.ann__m')), ds = [].slice.call(box.querySelectorAll('.ann__dots i'));
  var seen = false; try { seen = sessionStorage.getItem('annSeen') === '1'; sessionStorage.setItem('annSeen', '1'); } catch (e) {}
  if (!seen) box.classList.add('pop');
  // size the window to the longest message so nothing gets cut off
  var w = 0; ms.forEach(function (m) { w = Math.max(w, m.scrollWidth); }); box.querySelector('.ann__msgs').style.width = Math.ceil(w) + 'px';
  if (matchMedia('(prefers-reduced-motion: reduce)').matches || ms.length < 2) return;
  var i = 0, paused = false;
  link.addEventListener('mouseenter', function () { paused = true; }); link.addEventListener('mouseleave', function () { paused = false; });
  setInterval(function () {
    if (paused || document.hidden) return;
    var j = (i + 1) % ms.length, old = ms[i];
    old.classList.remove('on'); old.classList.add('out'); ds[i] && ds[i].classList.remove('on');
    ms[j].classList.remove('out'); ms[j].classList.add('on'); ds[j] && ds[j].classList.add('on');
    link.href = ms[j].getAttribute('data-href');
    setTimeout(function () { old.classList.remove('out'); }, 600); i = j;
  }, 2600);
  link.addEventListener('click', function () { (window.dataLayer = window.dataLayer || []).push({event: 'announcement_click', target: link.getAttribute('href')}); });
})();
