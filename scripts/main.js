document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('[data-contact-form]');
  if (!form) return;

  const status = form.querySelector('[data-form-status]');

  form.addEventListener('submit', (event) => {
    event.preventDefault();

    const data = new FormData(form);
    const name = String(data.get('name') || '').trim();
    const email = String(data.get('email') || '').trim();
    const message = String(data.get('message') || '').trim();

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

    const recipient = form.dataset.contactEmail || 'hello@example.com';
    window.location.href = `mailto:${encodeURIComponent(recipient)}?subject=${subject}&body=${body}`;

    if (status) {
      status.textContent = `Your email app should open with the inquiry details. Current recipient: ${recipient}.`;
    }
  });
});
