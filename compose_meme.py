#!/usr/bin/env python3
"""Composite the GTA 6 meme for gta6-meme-x-01.

Background: AI-generated Vice City neon sunset (assets/vice-city-bg.webp).
Mascot: make.fun's real press-pack ghost mark (assets/mark-on-dark-1024.png).
Text: Inter Bold (make.fun's press-pack font, assets/Inter-Bold.otf), white
with a black outline, so it reads at a glance even shrunk to 480px.

The joke: "WAITED" is a pun on GTA's iconic "WASTED" death screen — the
ghost waited 13 years for GTA 6, while its AI agent earned real money on
make.fun in the meantime.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

REPO = "/home/hatch/workspace/makefun/gta6-meme-x-01"
W, H = 1200, 675

bg = Image.open(f"{REPO}/assets/vice-city-bg.webp").convert("RGB")
bg = bg.resize((W, H), Image.LANCZOS)

# Soften the busy street centre slightly so the ghost and text read clean.
soft = bg.filter(ImageFilter.GaussianBlur(1.2))
bg = Image.blend(bg, soft, 0.35)

# A gentle dark veil at the top and bottom for the text.
veil = Image.new("RGBA", (W, H), (0, 0, 0, 0))
vd = ImageDraw.Draw(veil)
for y in range(0, 150):
    vd.line([(0, y), (W, y)], fill=(10, 8, 14, int(150 * (1 - y / 150))))
for y in range(H - 190, H):
    vd.line([(0, y), (W, y)], fill=(10, 8, 14, int(150 * ((y - (H - 190)) / 190))))
bg = Image.alpha_composite(bg.convert("RGBA"), veil)

# The make.fun ghost, large and central — the mascot must be recognisable
# even when the picture is shrunk to 480x480.
ghost = Image.open(f"{REPO}/assets/mark-on-dark-1024.png").convert("RGBA")
ghost = ghost.resize((300, 300), Image.LANCZOS)
bg.alpha_composite(ghost, (W // 2 - 150, 148))

d = ImageDraw.Draw(bg)
font_top = ImageFont.truetype(f"{REPO}/assets/Inter-Bold.otf", 64)
font_bot = ImageFont.truetype(f"{REPO}/assets/Inter-Bold.otf", 54)


def centred(y, text, font, fill=(255, 255, 255), stroke=4):
    bb = d.textbbox((0, 0), text, font=font, stroke_width=stroke)
    tw = bb[2] - bb[0]
    d.text(((W - tw) / 2 - bb[0], y), text, font=font, fill=fill,
           stroke_width=stroke, stroke_fill=(0, 0, 0))


centred(30, "WAITED 13 YEARS FOR GTA 6", font_top)
centred(478, "MY AI AGENT EARNS REAL MONEY", font_bot)
centred(548, "ON make.fun", font_bot)

bg.convert("RGB").save(f"{REPO}/meme.png", "PNG")
print("wrote", f"{REPO}/meme.png")
