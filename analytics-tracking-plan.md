# Mika Laurent Analytics Tracking Plan

Purpose: define privacy-friendly events to measure interest in Mika Laurent without collecting passwords, private messages, or sensitive personal data.

## Current implementation

The site includes lightweight client-side tracking hooks in `scripts/main.js`:

- Elements can declare `data-track="event_name"`.
- Optional labels can be provided with `data-track-label="label"`.
- Optional destinations can be provided with `data-track-destination="category"`.
- When clicked or submitted, the script dispatches a browser `CustomEvent` named `mika:track`.
- If a future analytics provider creates `window.dataLayer`, the same event is pushed there.
- No external analytics vendor is loaded yet.
- No passwords, MFA codes, private keys, or message body content are collected.

## Core events

| Event | Trigger | Purpose |
|---|---|---|
| `cta_gallery_click` | Homepage hero gallery button | Measures interest in the gallery |
| `cta_about_click` | Homepage hero about button | Measures interest in the model concept |
| `social_profile_click` | Instagram/TikTok/YouTube/Facebook profile links | Measures outbound social interest |
| `featured_post_click` | Featured launch post links | Measures launch content engagement |
| `calendar_open` | Content calendar CTA | Measures creator workflow interest |
| `media_kit_pdf_download` | Media kit PDF links | Measures press/media kit interest |
| `press_kit_open` | Press kit links | Measures brand/press interest |
| `asset_open` | Hero image / media assets | Measures creative asset interest |
| `contact_intent` | Contact email buttons or form submit | Measures inquiry intent |

## Event payload shape

```json
{
  "event": "media_kit_pdf_download",
  "label": "homepage_downloads_pdf",
  "destination": "download",
  "href": "assets/downloads/mika-laurent-media-kit.pdf",
  "page": "https://example.com/current-page",
  "timestamp": "2026-06-25T00:00:00.000Z"
}
```

## Future analytics provider options

If analytics is added later, prefer a privacy-friendly provider or self-hosted option:

1. Plausible Analytics
2. Fathom Analytics
3. Cloudflare Web Analytics
4. Google Analytics 4 only if needed for ad/platform integrations

## Recommended dashboard metrics

Weekly review:

- Homepage visits
- Press kit visits
- PDF downloads
- Contact clicks/form submits
- Social outbound clicks by platform
- Featured post outbound clicks
- Calendar opens
- Asset opens

## Privacy notes

- Do not track form field values.
- Do not track email addresses entered by visitors.
- Do not collect device fingerprints.
- Do not add third-party analytics until the privacy/trust tradeoff is intentional.
- Keep the AI disclosure visible on public-facing pages and media assets.
