// Click-to-play YouTube Shorts: loads the player only when someone clicks, so pages stay fast.
document.querySelectorAll('.vid[data-yt]').forEach(function (el) {
  function play() {
    if (el.querySelector('iframe')) return;
    var f = document.createElement('iframe');
    f.src = 'https://www.youtube-nocookie.com/embed/' + el.dataset.yt + '?autoplay=1&rel=0&playsinline=1';
    f.title = el.getAttribute('aria-label') || 'YouTube video';
    f.allow = 'autoplay; encrypted-media; picture-in-picture; web-share';
    f.allowFullscreen = true;
    el.innerHTML = ''; el.appendChild(f); el.classList.add('vid--on');
    if (window.gtag) gtag('event', 'video_play', {video_id: el.dataset.yt});
  }
  el.addEventListener('click', play);
  el.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); play(); } });
});
