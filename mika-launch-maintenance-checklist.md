# Mika Laurent Launch & Maintenance Checklist

Use this checklist to keep the Mika Laurent website, social links, disclosures, and downloadable assets accurate after launch.

## Weekly checks

- [ ] Open the live homepage: https://bchan818.github.io/mika-laurent-website/
- [ ] Open the live press kit: https://bchan818.github.io/mika-laurent-website/press-kit.html
- [ ] Open the Privacy & AI Disclosure page: https://bchan818.github.io/mika-laurent-website/privacy-disclosure.html
- [ ] Open the Terms & Asset Use page: https://bchan818.github.io/mika-laurent-website/terms-asset-use.html
- [ ] Confirm main navigation links work.
- [ ] Confirm footer links work.
- [ ] Confirm the homepage hero image loads.
- [ ] Confirm the gallery images load.
- [ ] Confirm the Brand Assets / Downloads section links work.

## Social profile checks

- [ ] Confirm Instagram profile link works.
- [ ] Confirm TikTok profile link works.
- [ ] Confirm YouTube profile or Short link works.
- [ ] Confirm Facebook profile link works.
- [ ] Confirm featured post links still point to the correct public posts.
- [ ] Confirm social bios or descriptions still include a clear AI-generated / fictional persona disclosure.

## Disclosure visibility checks

- [ ] Confirm the homepage still includes AI disclosure language.
- [ ] Confirm the press kit includes the recommended AI disclosure.
- [ ] Confirm the Privacy & AI Disclosure page clearly states Mika is fictional and AI-generated.
- [ ] Confirm the Terms & Asset Use page clearly states Mika is not a real person and cannot be misrepresented as one.
- [ ] Confirm media kit and social planning documents do not imply Mika has real-world lived experience or personal endorsements.

## PDF and media asset checks

- [ ] Open the downloadable media kit PDF.
- [ ] Confirm the media kit PDF displays correctly.
- [ ] Confirm the PDF contact email is current.
- [ ] Confirm the hero portrait opens from the downloads section.
- [ ] Confirm TikTok intro video asset opens.
- [ ] Confirm YouTube Short asset opens.
- [ ] Confirm social preview image exists at `assets/social-preview.jpg`.

## Sitemap, robots, and SEO checks

- [ ] Open `robots.txt` from the live site.
- [ ] Open `sitemap.xml` from the live site.
- [ ] Confirm sitemap includes homepage, press kit, privacy page, terms page, calendar, and media kit PDF.
- [ ] Confirm homepage social preview metadata still points to `assets/social-preview.jpg`.
- [ ] Confirm press kit, privacy page, and terms page have canonical URLs.
- [ ] Confirm major pages still have page titles and meta descriptions.

## Analytics event checks

- [ ] Open the homepage with `?debugTracking=true`.
- [ ] Click the hero CTA and confirm a `mika:track` debug event appears in the browser console.
- [ ] Click a social profile link and confirm a tracking event is emitted.
- [ ] Click the media kit PDF link and confirm a tracking event is emitted.
- [ ] Click the contact form submit button during a controlled test and confirm contact intent tracking occurs without storing form values.
- [ ] Confirm no external analytics provider is loaded unless intentionally added.

## Contact email test

- [ ] Submit a controlled test through the homepage contact form.
- [ ] Confirm the email app opens with recipient `hellomikalaurent@gmail.com`.
- [ ] Confirm the generated subject is appropriate.
- [ ] Confirm the generated body includes only expected inquiry details.
- [ ] Do not send passwords, MFA codes, private keys, payment numbers, IDs, or other sensitive information.

## Featured post updates

- [ ] Review featured Instagram post link.
- [ ] Review featured Facebook post link.
- [ ] Review featured TikTok video link.
- [ ] Review featured YouTube Short link.
- [ ] Replace stale featured links with newer launch or campaign posts when needed.
- [ ] Keep AI disclosure visible in any new featured post descriptions.

## Content calendar refresh

- [ ] Review `mika-14-day-content-calendar.md`.
- [ ] Mark completed content ideas separately if needed.
- [ ] Add new weekly or monthly content prompts after the first 14 days.
- [ ] Refresh captions so they match current active platforms.
- [ ] Keep a regular disclosure rhythm in captions and pinned content.

## Monthly privacy and terms review

- [ ] Review `privacy-disclosure.html` for accuracy.
- [ ] Review `terms-asset-use.html` for accuracy.
- [ ] Confirm the analytics description still matches the live implementation.
- [ ] Confirm contact handling language still matches how the form works.
- [ ] Confirm commercial use language is still appropriate for current project goals.
- [ ] Consider qualified legal review before paid collaborations, licensing, sponsorships, or client-facing commercial reuse.

## Local verification before publishing changes

Run these checks before committing site changes:

```bash
npm run verify
node --check scripts/main.js
git diff --check
```

If behavior changes are added, create a focused temporary ad-hoc verification script under the OS temp directory using a `hermes-verify-` filename prefix, run it, and remove it after verification.
