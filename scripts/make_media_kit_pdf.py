from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "downloads"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT = OUT_DIR / "mika-laurent-media-kit.pdf"
HERO = ROOT / "assets" / "mika-laurent-hero.jpg"

PAGE_W, PAGE_H = letter
cream = colors.HexColor("#fbf6ed")
beige = colors.HexColor("#ead9c2")
taupe = colors.HexColor("#806b58")
brown = colors.HexColor("#2f241d")
beige_deep = colors.HexColor("#c7a782")
white = colors.HexColor("#fffdf8")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Eyebrow", fontName="Helvetica-Bold", fontSize=8, leading=10, tracking=1.5, textColor=beige_deep, spaceAfter=8, uppercase=True))
styles.add(ParagraphStyle(name="MikaTitle", fontName="Helvetica-Bold", fontSize=30, leading=31, textColor=brown, spaceAfter=12))
styles.add(ParagraphStyle(name="Section", fontName="Helvetica-Bold", fontSize=14, leading=18, textColor=brown, spaceBefore=12, spaceAfter=6))
styles.add(ParagraphStyle(name="BodyCopy", fontName="Helvetica", fontSize=9.5, leading=14, textColor=taupe))
styles.add(ParagraphStyle(name="Small", fontName="Helvetica", fontSize=8.5, leading=12, textColor=taupe))
styles.add(ParagraphStyle(name="Link", fontName="Helvetica-Bold", fontSize=8.7, leading=12, textColor=brown))
styles.add(ParagraphStyle(name="Disclosure", fontName="Helvetica-Bold", fontSize=9.2, leading=13, textColor=white))

def p(text, style="BodyCopy"):
    return Paragraph(text, styles[style])

story = []

hero_img = Image(str(HERO), width=2.35 * inch, height=2.85 * inch)
hero_img.hAlign = "RIGHT"

left = [
    p("MIKA LAURENT · PRESS / MEDIA KIT", "Eyebrow"),
    p("Mika Laurent", "MikaTitle"),
    p("Fictional AI-generated fashion muse for soft editorial visuals, digital beauty, lifestyle storytelling, and modern brand concepts.", "BodyCopy"),
    Spacer(1, 0.14 * inch),
    p("Contact: hellomikalaurent@gmail.com", "Link"),
    p("Website: https://bchan818.github.io/mika-laurent-website/", "Link"),
]
hero_table = Table([[left, hero_img]], colWidths=[4.2 * inch, 2.45 * inch])
hero_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), cream),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
]))
story.append(hero_table)
story.append(Spacer(1, 0.2 * inch))

bio_cells = [
    [p("SHORT BIO", "Eyebrow"), p("LONG BIO", "Eyebrow")],
    [
        p("Mika Laurent is a fictional AI-generated fashion muse created for soft editorial visuals, digital beauty, lifestyle storytelling, and modern brand concepts."),
        p("Mika Laurent is a digital fashion persona with a warm beige editorial identity, long layered waves, refined styling, and a calm luxury presence. The project explores how AI-generated model visuals can support creative portfolios, campaign mockups, social content, and brand storytelling while keeping disclosure clear."),
    ],
]
bio_table = Table(bio_cells, colWidths=[3.25 * inch, 3.25 * inch])
bio_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), white),
    ("BOX", (0, 0), (-1, -1), 0.5, beige),
    ("INNERGRID", (0, 0), (-1, -1), 0.25, beige),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("PADDING", (0, 0), (-1, -1), 12),
]))
story.append(bio_table)
story.append(Spacer(1, 0.18 * inch))

story.append(p("AI DISCLOSURE", "Eyebrow"))
disclosure_table = Table([[p("Mika Laurent is not a real person. Mika is a fictional AI-generated fashion persona created for visual storytelling, digital campaigns, creative portfolio work, and brand concept development.", "Disclosure")]], colWidths=[6.55 * inch])
disclosure_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), brown),
    ("BOX", (0, 0), (-1, -1), 0, brown),
    ("PADDING", (0, 0), (-1, -1), 14),
]))
story.append(disclosure_table)
story.append(Spacer(1, 0.18 * inch))

story.append(p("OFFICIAL LINKS", "Eyebrow"))
links = [
    [p("Website", "Link"), p("https://bchan818.github.io/mika-laurent-website/", "Small")],
    [p("Instagram", "Link"), p("https://www.instagram.com/hellomikalaurent/", "Small")],
    [p("TikTok", "Link"), p("https://www.tiktok.com/@hellomikalaurent", "Small")],
    [p("YouTube Short", "Link"), p("https://youtube.com/shorts/XFcMqR0LX4o", "Small")],
    [p("Facebook", "Link"), p("https://www.facebook.com/profile.php?id=61591312558404", "Small")],
]
link_table = Table(links, colWidths=[1.25 * inch, 5.3 * inch])
link_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), white),
    ("BOX", (0, 0), (-1, -1), 0.5, beige),
    ("INNERGRID", (0, 0), (-1, -1), 0.25, beige),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("PADDING", (0, 0), (-1, -1), 7),
]))
story.append(link_table)
story.append(Spacer(1, 0.18 * inch))

story.append(p("FEATURED LAUNCH POSTS", "Eyebrow"))
post_data = [[
    p("Instagram<br/>DZ8G2tHDwi3", "Small"),
    p("Facebook<br/>122095256211377085", "Small"),
    p("TikTok<br/>7654729929526971679", "Small"),
    p("YouTube<br/>XFcMqR0LX4o", "Small"),
]]
post_table = Table(post_data, colWidths=[1.62 * inch] * 4)
post_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#fff8ee")),
    ("BOX", (0, 0), (-1, -1), 0.5, beige),
    ("INNERGRID", (0, 0), (-1, -1), 0.25, beige),
    ("PADDING", (0, 0), (-1, -1), 9),
]))
story.append(post_table)
story.append(Spacer(1, 0.16 * inch))

story.append(p("CREATIVE ASSETS", "Eyebrow"))
story.append(p("Hero portrait: assets/mika-laurent-hero.jpg · Intro image: assets/social/01-introduction.jpg · TikTok intro video: assets/social/mika-intro-short.mp4 · YouTube Short: assets/social/mika-youtube-short.mp4", "Small"))

class BackgroundDoc(SimpleDocTemplate):
    def handle_pageBegin(self):
        super().handle_pageBegin()

def draw_background(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(cream)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setStrokeColor(colors.Color(1, 1, 1, alpha=0.3))
    for x in range(0, int(PAGE_W), 54):
        canvas.line(x, 0, x, PAGE_H)
    for y in range(0, int(PAGE_H), 54):
        canvas.line(0, y, PAGE_W, y)
    canvas.restoreState()

doc = SimpleDocTemplate(str(OUT), pagesize=letter, rightMargin=0.48 * inch, leftMargin=0.48 * inch, topMargin=0.42 * inch, bottomMargin=0.42 * inch)
doc.build(story, onFirstPage=draw_background, onLaterPages=draw_background)
print(OUT)
