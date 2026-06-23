from pathlib import Path
import subprocess

import imageio_ffmpeg
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "social" / "01-introduction.jpg"
OUT = ROOT / "assets" / "social" / "mika-intro-short.mp4"

W, H = 1080, 1920
FPS = 24
DURATION = 12
FRAMES = FPS * DURATION
BG = (251, 246, 237)
BROWN = (47, 36, 29)
TAUPE = (128, 107, 88)
BEIGE = (199, 167, 130)
WHITE = (255, 253, 248)

FONT_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
]

def font(size, bold=False):
    paths = FONT_CANDIDATES if not bold else [FONT_CANDIDATES[0], *FONT_CANDIDATES[1:]]
    for path in paths:
        try:
            return ImageFont.truetype(path, size=size)
        except Exception:
            pass
    return ImageFont.load_default()

TITLE = font(82, True)
TITLE_SMALL = font(62, True)
BODY = font(40, False)
CAPTION = font(28, True)
DISCLOSURE = font(26, False)

slides = [
    (0.0, 2.1, "Come See Me", "Meet Mika Laurent"),
    (2.1, 4.2, "AI-generated fashion muse", "Soft editorial visuals"),
    (4.2, 6.4, "Digital beauty", "Lifestyle storytelling"),
    (6.4, 8.8, "Fictional AI persona", "Not a real person"),
    (8.8, 12.0, "Follow the story", "@hellomikalaurent"),
]

img = Image.open(SOURCE).convert("RGB")
# Crop square center, then make portrait hero area.
side = min(img.size)
left = (img.width - side) // 2
top = (img.height - side) // 2
img = img.crop((left, top, left + side, top + side))

def rounded_rect_mask(size, radius):
    mask = Image.new("L", size, 0)
    d = ImageDraw.Draw(mask)
    d.rounded_rectangle((0, 0, size[0], size[1]), radius=radius, fill=255)
    return mask

def draw_center(draw, y, text, fnt, fill):
    bbox = draw.textbbox((0, 0), text, font=fnt)
    x = (W - (bbox[2] - bbox[0])) // 2
    draw.text((x, y), text, font=fnt, fill=fill)

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
cmd = [
    ffmpeg,
    "-y",
    "-f", "rawvideo",
    "-vcodec", "rawvideo",
    "-s", f"{W}x{H}",
    "-pix_fmt", "rgb24",
    "-r", str(FPS),
    "-i", "-",
    "-an",
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    "-movflags", "+faststart",
    str(OUT),
]

proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
for i in range(FRAMES):
    t = i / FPS
    base = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(base)

    # Soft decorative circles.
    d.ellipse((760, -130, 1220, 330), fill=(234, 217, 194))
    d.ellipse((-170, 1440, 380, 1990), fill=(238, 224, 203))

    # Image card with slow zoom.
    zoom = 1.0 + 0.06 * (i / max(1, FRAMES - 1))
    crop_side = int(side / zoom)
    l = (side - crop_side) // 2
    zimg = img.crop((l, l, l + crop_side, l + crop_side)).resize((920, 920), Image.Resampling.LANCZOS)
    card = Image.new("RGB", (960, 1040), WHITE)
    card.paste(zimg, (20, 20), rounded_rect_mask((920, 920), 42))
    card_d = ImageDraw.Draw(card)
    card_d.text((42, 964), "Mika Laurent", font=CAPTION, fill=TAUPE)
    card_d.text((648, 964), "AI fashion muse", font=CAPTION, fill=BROWN)
    shadow = Image.new("RGBA", (1000, 1080), (0, 0, 0, 0))
    shd = ImageDraw.Draw(shadow)
    shd.rounded_rectangle((20, 20, 980, 1060), radius=54, fill=(47, 36, 29, 32))
    shadow = shadow.filter(ImageFilter.GaussianBlur(28))
    base.paste(shadow.convert("RGB"), (40, 118), shadow)
    base.paste(card, (60, 120), rounded_rect_mask(card.size, 54))

    # Text panel.
    d.rounded_rectangle((80, 1210, 1000, 1710), radius=54, fill=(255, 253, 248), outline=(229, 211, 187), width=2)
    d.text((110, 1260), "MIKA LAURENT · AI FASHION MODEL", font=CAPTION, fill=BEIGE)

    active = slides[-1]
    for sl in slides:
        if sl[0] <= t < sl[1]:
            active = sl
            break
    title, subtitle = active[2], active[3]
    draw_center(d, 1340, title, TITLE if len(title) < 24 else TITLE_SMALL, BROWN)
    draw_center(d, 1440, subtitle, BODY, TAUPE)
    draw_center(d, 1558, "AI-generated fictional persona · Not a real person", DISCLOSURE, TAUPE)
    draw_center(d, 1640, "hellomikalaurent@gmail.com", CAPTION, BEIGE)

    # Subtle fade in/out.
    alpha = 1.0
    if t < 0.5:
        alpha = t / 0.5
    elif t > DURATION - 0.6:
        alpha = max(0, (DURATION - t) / 0.6)
    if alpha < 1:
        overlay = Image.new("RGB", (W, H), BG)
        base = Image.blend(overlay, base, alpha)

    proc.stdin.write(np.asarray(base, dtype=np.uint8).tobytes())

proc.stdin.close()
code = proc.wait()
if code:
    raise SystemExit(f"ffmpeg failed with exit code {code}")
print(OUT)
