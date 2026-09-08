/* Progressive enhancements only. All discovery works through server-side forms. */
document.documentElement.classList.add('js');
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
const finePointer = window.matchMedia('(hover: hover) and (pointer: fine)');
const menu = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#nav-links');
function closeMenu() {
  navigation?.classList.remove('open');
  menu?.setAttribute('aria-expanded', 'false');
}
menu?.addEventListener('click', () => {
  const expanded = menu.getAttribute('aria-expanded') === 'true';
  menu.setAttribute('aria-expanded', String(!expanded));
  navigation.classList.toggle('open', !expanded);
});
navigation?.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && menu?.getAttribute('aria-expanded') === 'true') {
    closeMenu();
    menu.focus();
  }
});

document.querySelectorAll('[data-tilt]').forEach(card => {
  let frame;
  const reset = () => {
    cancelAnimationFrame(frame);
    card.style.transform = '';
  };
  card.addEventListener('pointermove', event => {
    if (reduceMotion.matches || !finePointer.matches) return;
    const bounds = card.getBoundingClientRect();
    const x = Math.max(-.5, Math.min(.5, (event.clientX - bounds.left) / bounds.width - .5));
    const y = Math.max(-.5, Math.min(.5, (event.clientY - bounds.top) / bounds.height - .5));
    cancelAnimationFrame(frame);
    frame = requestAnimationFrame(() => {
      card.style.transform = `perspective(1000px) rotateX(${-y * 6}deg) rotateY(${x * 6}deg) translateY(-3px)`;
    });
  });
  card.addEventListener('pointerleave', reset);
  card.addEventListener('blur', reset);
  reduceMotion.addEventListener('change', reset);
});

if ('IntersectionObserver' in window && !reduceMotion.matches) {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.remove('pending');
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: .08 });
  document.querySelectorAll('.reveal').forEach(section => {
    // Leave above-the-fold and very tall sections visible even without a callback.
    if (section.getBoundingClientRect().top > window.innerHeight) section.classList.add('pending');
    observer.observe(section);
  });
}

document.querySelectorAll('img[data-fallback]').forEach(img => {
  const fallback = () => {
    if (!img.dataset.fallback) return;
    img.src = img.dataset.fallback;
    delete img.dataset.fallback;
  };
  img.addEventListener('error', fallback);
  if (img.complete && img.naturalWidth === 0) fallback();
});
document.querySelectorAll('.mood-form').forEach(form => {
  form.addEventListener('submit', event => {
    form.classList.add('is-loading');
    event.submitter?.classList.add('selected');
    form.querySelector('[role="status"]').textContent = 'Finding movies for your mood…';
  });
});
window.addEventListener('pageshow', () => {
  document.querySelectorAll('.mood-form').forEach(form => {
    form.classList.remove('is-loading');
    form.querySelector('[role="status"]').textContent = '';
    form.querySelectorAll('.mood-card').forEach(button => {
      button.classList.toggle('selected', button.getAttribute('aria-pressed') === 'true');
    });
  });
});
