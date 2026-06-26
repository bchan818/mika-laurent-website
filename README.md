# Mika Laurent — Come See Me AI Model Website

A clean, soft beige landing page concept for Mika Laurent, an AI fashion/lifestyle model.

## What is included

- `index.html` — one-page landing website with gallery, social links, featured posts, content calendar CTA, and brand asset downloads
- `press-kit.html` — press/media kit with bios, AI disclosure, official links, featured posts, and creative assets
- `privacy-disclosure.html` — plain-language privacy, AI disclosure, media usage, contact handling, and analytics page
- `assets/downloads/mika-laurent-media-kit.pdf` — downloadable one-page PDF media kit
- `assets/social-preview.jpg` — 1200x630 social preview image for shared links
- `robots.txt` and `sitemap.xml` — basic crawl and discovery files
- `styles.css` — responsive beige design with clean sans-serif typography
- `assets/mika-laurent-hero.jpg` — realistic AI model hero visual
- `assets/gallery/*.jpg` — six-gallery image set for Soft Studio, Luxury Editorial, Modern Casual, Beauty Close-Up, Fashion Profile, and Brand Campaign
- `assets/ai-model-portrait.svg` — previous illustrated placeholder backup
- `assets/favicon.svg` — site favicon
- `scripts/main.js` — mailto contact-form behavior
- `social-launch-kit.md` — recommended handles, bios, AI disclosure wording, first 9 launch posts, and social setup checklist
- `social-profile-links.md` — profile-link walkthrough for Instagram, TikTok, YouTube, and Facebook
- `social-first-posts.md` — platform-specific pinned/intro post copy for Instagram, TikTok, YouTube, and Facebook
- `analytics-tracking-plan.md` — privacy-friendly event tracking plan for clicks, downloads, and contact intent
- `mika-14-day-content-calendar.md` — two-week posting plan with captions, assets, disclosures, and platform guidance
- `assets/social/` — first 9 launch post visuals, text-card assets, and vertical intro video
- `scripts/make_intro_video.py` — generates the 1080x1920 TikTok/YouTube Shorts intro video
- `scripts/make_youtube_short.py` — generates the 1080x1920 YouTube-specific Short video
- `scripts/make_media_kit_pdf.py` — generates the downloadable one-page PDF media kit
- `scripts/make_social_preview.py` — generates the 1200x630 social preview image
- `scripts/verify.py` — local verification script

## Run locally

Open `index.html` directly in a browser, or run:

```bash
npm run verify
npm run preview
```

Then visit `http://127.0.0.1:4173`.

## Deploy

This is a static site and is ready for Vercel deployment. The deployment config is in `vercel.json`.

If Vercel CLI is installed and logged in, deploy with:

```bash
vercel --prod
```

If using the Vercel dashboard, upload/import this folder as a static project:

`/Users/bchan8/Developer/ai-model-website`

Note: The hero image is a realistic AI-generated portrait asset saved locally as `assets/mika-laurent-hero.jpg`.

Contact inquiries are currently routed to `hellomikalaurent@gmail.com`.

Confirmed social profiles:

- Instagram: https://www.instagram.com/hellomikalaurent/
- TikTok: https://www.tiktok.com/@hellomikalaurent
- YouTube: https://www.youtube.com/@hellomikalaurent
- Facebook: https://www.facebook.com/profile.php?id=61591312558404

Featured social posts:

- Instagram intro: https://www.instagram.com/p/DZ8G2tHDwi3/
- Facebook intro: https://www.facebook.com/photo/?fbid=122095256211377085
- TikTok intro: https://www.tiktok.com/@hellomikalaurent/video/7654729929526971679
- YouTube Short: https://youtube.com/shorts/XFcMqR0LX4o
