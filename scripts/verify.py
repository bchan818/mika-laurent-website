from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    ROOT / "index.html",
    ROOT / "press-kit.html",
    ROOT / "privacy-disclosure.html",
    ROOT / "terms-asset-use.html",
    ROOT / "robots.txt",
    ROOT / "sitemap.xml",
    ROOT / "assets" / "social-preview.jpg",
    ROOT / "assets" / "downloads" / "mika-laurent-media-kit.pdf",
    ROOT / "styles.css",
    ROOT / "assets" / "mika-laurent-hero.jpg",
    ROOT / "assets" / "gallery" / "soft-studio.jpg",
    ROOT / "assets" / "gallery" / "luxury-editorial.jpg",
    ROOT / "assets" / "gallery" / "modern-casual.jpg",
    ROOT / "assets" / "gallery" / "beauty-closeup.jpg",
    ROOT / "assets" / "gallery" / "fashion-profile.jpg",
    ROOT / "assets" / "gallery" / "brand-campaign.jpg",
    ROOT / "assets" / "favicon.svg",
    ROOT / "assets" / "social" / "01-introduction.jpg",
    ROOT / "assets" / "social" / "05-ai-disclosure.svg",
    ROOT / "assets" / "social" / "09-website-launch.svg",
    ROOT / "assets" / "social" / "mika-intro-short.mp4",
    ROOT / "assets" / "social" / "mika-intro-short-preview.jpg",
    ROOT / "assets" / "social" / "mika-youtube-short.mp4",
    ROOT / "assets" / "social" / "mika-youtube-short-preview.jpg",
    ROOT / "scripts" / "main.js",
    ROOT / "scripts" / "make_intro_video.py",
    ROOT / "scripts" / "make_youtube_short.py",
    ROOT / "scripts" / "make_media_kit_pdf.py",
    ROOT / "scripts" / "make_social_preview.py",
    ROOT / "social-launch-kit.md",
    ROOT / "social-profile-links.md",
    ROOT / "social-first-posts.md",
    ROOT / "analytics-tracking-plan.md",
    ROOT / "mika-14-day-content-calendar.md",
    ROOT / "assets" / "ai-model-portrait.svg",
]
REQUIRED_TEXT = [
    "Mika Laurent",
    "Come See Me",
    "Six polished looks",
    "Brand story",
    "AI disclosure",
    "not a real person",
    "Instagram",
    "TikTok",
    "Social launch",
    "@hellomikalaurent",
    "YouTube",
    "Facebook",
    "61591312558404",
    "First 9-post launch grid",
    "Featured posts",
    "Content calendar",
    "Open Calendar",
    "mika-14-day-content-calendar.md",
    "Press Kit",
    "press-kit.html",
    "privacy-disclosure.html",
    "terms-asset-use.html",
    "Brand assets",
    "Download Mika’s media kit and launch assets.",
    "One-page media kit",
    "Open Press Kit",
    "assets/downloads/mika-laurent-media-kit.pdf",
    "DZ8G2tHDwi3",
    "122095256211377085",
    "7654729929526971679",
    "XFcMqR0LX4o",
    "Website Launch",
    "Portfolio",
    "Brand Visuals",
    "Project idea",
    "og:image",
    "og:image:width",
    "og:image:height",
    "og:image:alt",
    "og:site_name",
    "twitter:card",
    "twitter:image:alt",
    "application/ld+json",
    "assets/social-preview.jpg",
    "data-contact-form",
    "data-track",
    "media_kit_pdf_download",
    "featured_post_click",
    "site-footer",
    "soft beige",
    "Explore the Gallery",
    "Meet Her",
]

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.links = []
        self.images = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self.in_title = True
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.links.append(attrs.get("href"))
        if tag == "img":
            self.images.append(attrs)

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data

for path in REQUIRED_FILES:
    if not path.exists():
        raise SystemExit(f"Missing required file: {path}")

html = (ROOT / "index.html").read_text(encoding="utf-8")
press_html = (ROOT / "press-kit.html").read_text(encoding="utf-8")
privacy_html = (ROOT / "privacy-disclosure.html").read_text(encoding="utf-8")
terms_html = (ROOT / "terms-asset-use.html").read_text(encoding="utf-8")
main_js = (ROOT / "scripts" / "main.js").read_text(encoding="utf-8")
css = (ROOT / "styles.css").read_text(encoding="utf-8")
parser = Parser()
parser.feed(html)

for text in REQUIRED_TEXT:
    if text not in html:
        raise SystemExit(f"Missing required text: {text}")

for text in [
    "Mika Laurent | Press Kit",
    "Media kit for a digital fashion muse",
    "Short bio",
    "Long bio",
    "Recommended disclosure",
    "Official Mika Laurent links",
    "Creative assets for review and sharing",
    "hellomikalaurent@gmail.com",
    "assets/mika-laurent-hero.jpg",
    "assets/social/mika-youtube-short.mp4",
    "assets/downloads/mika-laurent-media-kit.pdf",
    "Download PDF",
    "og:image:width",
    "og:image:height",
    "twitter:image:alt",
    "application/ld+json",
    "assets/social-preview.jpg",
    "data-track",
    "media_kit_pdf_download",
    "contact_intent",
]:
    if text not in press_html:
        raise SystemExit(f"Missing required press kit text: {text}")

for text in [
    "Mika Laurent | Privacy & AI Disclosure",
    "Mika Laurent is not a real person",
    "What not to send",
    "Privacy-friendly measurement only",
    "current tracking is designed for basic click measurement",
    "analytics-tracking-plan.md",
    "data-track",
    "contact_intent",
    "application/ld+json",
    "assets/social-preview.jpg",
]:
    if text not in privacy_html:
        raise SystemExit(f"Missing required privacy/disclosure text: {text}")

for text in [
    "Mika Laurent | Terms & Asset Use",
    "Usage boundaries for Mika Laurent assets",
    "This is plain-language project guidance, not legal advice",
    "Mika Laurent is fictional and AI-generated",
    "Reference and share with clear disclosure",
    "Do not mislead, impersonate, or exploit",
    "Ask before using Mika in commercial campaigns",
    "No real-world endorsement",
    "assets/downloads/mika-laurent-media-kit.pdf",
    "privacy-disclosure.html",
    "data-track",
    "contact_intent",
    "application/ld+json",
    "assets/social-preview.jpg",
]:
    if text not in terms_html:
        raise SystemExit(f"Missing required terms/asset use text: {text}")

if "styles.css" not in parser.links:
    raise SystemExit("index.html does not link styles.css")

for text in [
    "mika:track",
    "window.dataLayer.push",
    "debugTracking=true",
    "contact_intent",
]:
    if text not in main_js:
        raise SystemExit(f"Missing tracking script text: {text}")

if not any(img.get("src") == "assets/mika-laurent-hero.jpg" and img.get("alt") for img in parser.images):
    raise SystemExit("Hero image missing or missing alt text")

for token in ["font-family: Inter", "--beige", "#ead9c2", "sans-serif", "@media"]:
    if token not in css:
        raise SystemExit(f"Missing expected CSS token: {token}")

print("Verification passed: files exist, hero copy is present, stylesheet/image links are valid, and responsive beige sans-serif styling is included.")
