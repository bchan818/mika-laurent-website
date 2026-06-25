from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "social-preview.jpg"
HERO = ROOT / "assets" / "mika-laurent-hero.jpg"

W, H = 1200, 630
cream = "#fbf6ed"
beige = "#ead9c2"
brown = "#2f241d"
taupe = "#806b58"
beige_deep = "#c7a782"
white = "#fffdf8"

canvas = Image.new("RGB", (W, H), cream)
draw = ImageDraw.Draw(canvas)
for x in range(0, W, 72):
    draw.line((x, 0, x, H), fill="#f5eadb", width=1)
for y in range(0, H, 72):
    draw.line((0, y, W, y), fill="#f5eadb", width=1)

# Soft glow behind image
for radius, alpha in [(260, 34), (190, 40), (120, 46)]:
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((650 - radius, 315 - radius, 650 + radius, 315 + radius), fill=(199, 167, 130, alpha))
    canvas = Image.alpha_composite(canvas.convert("RGBA"), glow).convert("RGB")

hero = Image.open(HERO).convert("RGB")
# Crop portrait to 4:5 and place right.
w0, h0 = hero.size
target_ratio = 4 / 5
current_ratio = w0 / h0
if current_ratio > target_ratio:
    new_w = int(h0 * target_ratio)
    left = (w0 - new_w) // 2
    hero = hero.crop((left, 0, left + new_w, h0))
else:
    new_h = int(w0 / target_ratio)
    top = max(0, (h0 - new_h) // 2)
    hero = hero.crop((0, top, w0, top + new_h))
hero = hero.resize((390, 450), Image.Resampling.LANCZOS)
mask = Image.new("L", hero.size, 0)
md = ImageDraw.Draw(mask)
md.rounded_rectangle((0, 0, hero.size[0], hero.size[1]), radius=34, fill=255)
card = Image.new("RGB", (438, 536), white)
cd = ImageDraw.Draw(card)
cd.rounded_rectangle((0, 0, 437, 535), radius=42, fill=white)
card.paste(hero, (24, 24), mask)
shadow = Image.new("RGBA", (500, 590), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.rounded_rectangle((30, 30, 468, 566), radius=42, fill=(83, 60, 38, 42))
shadow = shadow.filter(ImageFilter.GaussianBlur(20))
canvas = canvas.convert("RGBA")
canvas.alpha_composite(shadow, (670, 20))
canvas.paste(card, (700, 45))
canvas = canvas.convert("RGB")
draw = ImageDraw.Draw(canvas)

font_candidates = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/Library/Fonts/Arial.ttf",
]
def font(size, bold=False):
    if bold:
        for p in font_candidates[:1] + font_candidates:
            if Path(p).exists():
                return ImageFont.truetype(p, size)
    for p in font_candidates:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

eyebrow = font(20, True)
title = font(78, True)
body = font(29)
small = font(20, True)

draw.text((72, 108), "MIKA LAURENT · AI FASHION MODEL", fill=beige_deep, font=eyebrow)
draw.text((72, 155), "Come See Me", fill=brown, font=title)
draw.text((72, 265), "Soft beige editorial visuals,\ndigital beauty, and brand storytelling.", fill=taupe, font=body, spacing=12)
# Disclosure pill
pill = (72, 420, 500, 480)
draw.rounded_rectangle(pill, radius=30, fill=brown)
draw.text((100, 438), "Fictional AI-generated persona", fill=white, font=small)
draw.text((724, 544), "Mika Laurent", fill=taupe, font=font(18))
draw.text((990, 544), "Press & media kit", fill=brown, font=font(18, True))

OUT.parent.mkdir(parents=True, exist_ok=True)
canvas.save(OUT, quality=92, optimize=True)
print(OUT)
