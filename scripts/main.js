document.addEventListener('DOMContentLoaded', () => {
  const emitTrackingEvent = (eventName, detail = {}) => {
    if (!eventName) return;

    const payload = {
      event: eventName,
      label: detail.label || '',
      destination: detail.destination || '',
      href: detail.href || '',
      page: window.location.href,
      timestamp: new Date().toISOString(),
    };

    window.dispatchEvent(new CustomEvent('mika:track', { detail: payload }));

    if (Array.isArray(window.dataLayer)) {
      window.dataLayer.push(payload);
    }

    if (window.location.search.includes('debugTracking=true')) {
      console.info('Mika tracking event', payload);
    }
  };

  document.querySelectorAll('[data-track]').forEach((element) => {
    element.addEventListener('click', () => {
      emitTrackingEvent(element.dataset.track, {
        label: element.dataset.trackLabel || element.textContent.trim(),
        destination: element.dataset.trackDestination || '',
        href: element.getAttribute('href') || '',
      });
    });
  });

  const form = document.querySelector('[data-contact-form]');
  if (!form) return;

  const status = form.querySelector('[data-form-status]');

  form.addEventListener('submit', (event) => {
    event.preventDefault();

    const data = new FormData(form);
    const name = String(data.get('name') || '').trim();
    const email = String(data.get('email') || '').trim();
    const message = String(data.get('message') || '').trim();

    emitTrackingEvent('contact_intent', {
      label: form.dataset.trackLabel || 'homepage_contact_form',
      destination: 'email',
      href: `mailto:${form.dataset.contactEmail || 'hellomikalaurent@gmail.com'}`,
    });

    const subject = encodeURIComponent('Mika Laurent project inquiry');
    const body = encodeURIComponent([
      'New Mika Laurent project inquiry',
      '',
      `Name: ${name || 'Not provided'}`,
      `Email: ${email || 'Not provided'}`,
      '',
      'Project idea:',
      message || 'Not provided',
    ].join('\n'));

    const recipient = form.dataset.contactEmail || 'hellomikalaurent@gmail.com';
    window.location.href = `mailto:${encodeURIComponent(recipient)}?subject=${subject}&body=${body}`;

    if (status) {
      status.textContent = `Your email app should open with the inquiry details. Current recipient: ${recipient}.`;
    }
  });
});
