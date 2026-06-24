from pathlib import Path
import subprocess

import imageio_ffmpeg
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "social" / "01-introduction.jpg"
OUT = ROOT / "assets" / "social" / "mika-youtube-short.mp4"
PREVIEW = ROOT / "assets" / "social" / "mika-youtube-short-preview.jpg"

W, H = 1080, 1920
FPS = 24
DURATION = 15
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

TITLE = font(84, True)
TITLE_SMALL = font(60, True)
BODY = font(40, False)
CAPTION = font(28, True)
DISCLOSURE = font(26, False)

slides = [
    (0.0, 2.6, "Meet Mika Laurent", "AI Fashion Muse"),
    (2.6, 5.2, "Soft editorial visuals", "Digital beauty storytelling"),
    (5.2, 7.9, "Created for campaigns", "Lifestyle, fashion, and brand visuals"),
    (7.9, 10.9, "Fictional AI persona", "Mika Laurent is not a real person"),
    (10.9, 15.0, "Come See Me", "Explore the full visual identity"),
]

img = Image.open(SOURCE).convert("RGB")
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

def make_frame(i):
    t = i / FPS
    base = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(base)

    d.ellipse((740, -160, 1230, 330), fill=(234, 217, 194))
    d.ellipse((-180, 1460, 390, 2030), fill=(238, 224, 203))

    zoom = 1.0 + 0.075 * (i / max(1, FRAMES - 1))
    crop_side = int(side / zoom)
    l = (side - crop_side) // 2
    zimg = img.crop((l, l, l + crop_side, l + crop_side)).resize((900, 900), Image.Resampling.LANCZOS)

    card = Image.new("RGB", (940, 1025), WHITE)
    card.paste(zimg, (20, 20), rounded_rect_mask((900, 900), 42))
    card_d = ImageDraw.Draw(card)
    card_d.text((42, 948), "Mika Laurent", font=CAPTION, fill=TAUPE)
    card_d.text((602, 948), "YouTube Short", font=CAPTION, fill=BROWN)

    shadow = Image.new("RGBA", (980, 1065), (0, 0, 0, 0))
    shd = ImageDraw.Draw(shadow)
    shd.rounded_rectangle((20, 20, 960, 1045), radius=54, fill=(47, 36, 29, 32))
    shadow = shadow.filter(ImageFilter.GaussianBlur(28))
    base.paste(shadow.convert("RGB"), (50, 95), shadow)
    base.paste(card, (70, 100), rounded_rect_mask(card.size, 54))

    d.rounded_rectangle((80, 1185, 1000, 1728), radius=54, fill=(255, 253, 248), outline=(229, 211, 187), width=2)
    d.text((110, 1235), "MIKA LAURENT · AI FASHION MODEL", font=CAPTION, fill=BEIGE)

    active = slides[-1]
    for sl in slides:
        if sl[0] <= t < sl[1]:
            active = sl
            break
    title, subtitle = active[2], active[3]
    draw_center(d, 1320, title, TITLE if len(title) < 22 else TITLE_SMALL, BROWN)
    draw_center(d, 1430, subtitle, BODY, TAUPE)
    draw_center(d, 1548, "AI-generated fictional persona · Not a real person", DISCLOSURE, TAUPE)
    draw_center(d, 1628, "bchan818.github.io/mika-laurent-website", CAPTION, BEIGE)

    alpha = 1.0
    if t < 0.55:
        alpha = t / 0.55
    elif t > DURATION - 0.7:
        alpha = max(0, (DURATION - t) / 0.7)
    if alpha < 1:
        overlay = Image.new("RGB", (W, H), BG)
        base = Image.blend(overlay, base, alpha)
    return base

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
cmd = [
    ffmpeg, "-y",
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
preview_frame = None
for i in range(FRAMES):
    frame = make_frame(i)
    if i == FPS * 4:
        preview_frame = frame.copy()
    proc.stdin.write(np.asarray(frame, dtype=np.uint8).tobytes())
proc.stdin.close()
code = proc.wait()
if code:
    raise SystemExit(f"ffmpeg failed with exit code {code}")
if preview_frame:
    preview_frame.save(PREVIEW, quality=92)
print(OUT)
print(PREVIEW)
