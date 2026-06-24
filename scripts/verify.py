from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    ROOT / "index.html",
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
    ROOT / "scripts" / "main.js",
    ROOT / "scripts" / "make_intro_video.py",
    ROOT / "social-launch-kit.md",
    ROOT / "social-profile-links.md",
    ROOT / "social-first-posts.md",
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
    "DZ8G2tHDwi3",
    "122095256211377085",
    "7654729929526971679",
    "Website Launch",
    "Portfolio",
    "Brand Visuals",
    "Project idea",
    "og:image",
    "twitter:card",
    "data-contact-form",
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
css = (ROOT / "styles.css").read_text(encoding="utf-8")
parser = Parser()
parser.feed(html)

for text in REQUIRED_TEXT:
    if text not in html:
        raise SystemExit(f"Missing required text: {text}")

if "styles.css" not in parser.links:
    raise SystemExit("index.html does not link styles.css")

if not any(img.get("src") == "assets/mika-laurent-hero.jpg" and img.get("alt") for img in parser.images):
    raise SystemExit("Hero image missing or missing alt text")

for token in ["font-family: Inter", "--beige", "#ead9c2", "sans-serif", "@media"]:
    if token not in css:
        raise SystemExit(f"Missing expected CSS token: {token}")

print("Verification passed: files exist, hero copy is present, stylesheet/image links are valid, and responsive beige sans-serif styling is included.")
