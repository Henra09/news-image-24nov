#!/usr/bin/env python3
"""Draw the 24 November 2026 world-news infographic -> entry.png (1024x1024 PNG)."""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (16, 20, 30)
TITLE_BG = (8, 12, 22)
CARD_BG = (28, 34, 48)
TEXT = (238, 240, 245)
SUB = (160, 168, 182)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
f_title = ImageFont.truetype(FB, 44)
f_date = ImageFont.truetype(FB, 26)
f_head = ImageFont.truetype(FB, 21)
f_det = ImageFont.truetype(FR, 16)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# ---- Title bar
d.rectangle([0, 0, W, 118], fill=TITLE_BG)
d.rectangle([0, 118, W, 124], fill=(230, 60, 60))
d.text((30, 18), "WORLD NEWS", font=f_title, fill=TEXT)
d.text((30, 74), "Tuesday, 24 November 2026 - The day in one picture", font=f_date, fill=(235, 90, 90))
d.text((W - 30, 74), "9 stories", font=f_date, fill=SUB, anchor="ra")

# ---- Stories: (region tag, tag color, icon drawer, headline lines, detail)
def icon_globe(d, x, y, c):  # middle east
    d.ellipse([x, y, x+26, y+26], outline=c, width=3)
    d.arc([x-4, y+6, x+30, y+20], 0, 360, fill=c, width=2)
    d.line([x+13, y, x+13, y+26], fill=c, width=2)

def icon_ship(d, x, y, c):  # iran tankers = fire ship
    d.polygon([(x+2, y+20), (x+24, y+20), (x+20, y+12), (x+6, y+12)], fill=c)
    for i, h in enumerate((10, 14, 8)):
        d.polygon([(x+7+i*7, y+11), (x+10+i*7, y+11-h), (x+13+i*7, y+11)], fill=c)

def icon_plane(d, x, y, c):  # ukraine/russia war
    d.polygon([(x+13, y), (x+17, y+10), (x+26, y+16), (x+17, y+16), (x+17, y+26), (x+13, y+26), (x+13, y+16), (x, y+16), (x+9, y+10)], fill=c)

def icon_chart(d, x, y, c):
    d.line([x, y+24, x+26, y+24], fill=c, width=3)
    d.line([x+2, y+22, x+9, y+10], fill=c, width=4)
    d.line([x+11, y+22, x+17, y+4], fill=c, width=4)
    d.line([x+19, y+22, x+25, y+14], fill=c, width=4)

def icon_tag(d, x, y, c):  # tariffs
    d.polygon([(x, y+6), (x+8, y), (x+26, y), (x+26, y+22), (x+8, y+22), (x, y+16)], outline=c, width=3)
    d.ellipse([x+4, y+10, x+9, y+15], fill=c)

def icon_peso(d, x, y, c):
    d.ellipse([x, y, x+26, y+26], outline=c, width=3)
    d.text((x+6, y+2), "$", font=ImageFont.truetype(FB, 19), fill=c)

def icon_bomb(d, x, y, c):
    d.ellipse([x+2, y+12, x+20, y+28], fill=c)
    d.line([x+16, y+12, x+24, y+2], fill=c, width=3)
    d.ellipse([x+22, y, x+27, y+5], fill=c)

def icon_atom(d, x, y, c):
    for a in (0, 60, 120):
        d.ellipse([x, y+4+a*0, x+26, y+22], outline=c, width=2)

def icon_knight(d, x, y, c):
    d.polygon([(x+4, y+26), (x+22, y+26), (x+20, y+8), (x+12, y+2), (x+8, y+8), (x+14, y+12), (x+8, y+16)], fill=c)

stories = [
    ("MIDDLE EAST", (230, 120, 60), icon_ship, "Saudi strikes kill dozens in Yemen",
     "Airstrike on buses/trucks kills 26; Houthis say 41 civilians in one day"),
    ("GULF", (240, 90, 90), icon_globe, "Mines blamed for tanker fires",
     "Iran's Guard navy says mine blasts set 3 oil tankers ablaze"),
    ("EASTERN EUROPE", (120, 160, 230), icon_plane, "Ukraine hits Russian warship",
     "Kyiv says drones sank corvette off Libya; Zaporizhzhia strike kills 2"),
    ("MARKETS", (90, 200, 140), icon_chart, "AI sell-off drags Wall Street",
     "Nvidia-led slump: S&P 500 -0.5%, 8th loss in a row"),
    ("TRADE", (230, 180, 80), icon_tag, "Trump readies new tariffs",
     "Targets China, EU, Japan, Mexico over subsidized factory output"),
    ("AMERICAS", (200, 140, 220), icon_peso, "Venezuela opens its books",
     "Reveals $237.5 bn debt pile, key step to restructuring"),
    ("SOUTH AMERICA", (220, 100, 110), icon_bomb, "Car bomb injures 25 in Colombia",
     "Blast hits Villavicencio; government buildings damaged"),
    ("SCIENCE", (100, 190, 220), icon_atom, "GPT-6 designs new proteins",
     "OpenAI says its models can create novel working protein shapes"),
    ("SPORT", (240, 200, 100), icon_knight, "Chess title: Game 1 drawn",
     "Gukesh holds Sindarov; Galatasaray beat Villa 1-0 in UCL"),
]

top = 134
card_h = 96
gap = 3
for i, (tag, col, icon, h1, det) in enumerate(stories):
    y = top + i * (card_h + gap)
    d.rectangle([0, y, W, y + card_h], fill=CARD_BG)
    d.rectangle([0, y, 10, y + card_h], fill=col)
    # region tag chip
    tw = d.textlength(tag, font=ImageFont.truetype(FB, 14))
    d.rounded_rectangle([24, y + 12, 24 + tw + 22, y + 36], 8, fill=col)
    d.text((35, y + 14), tag, font=ImageFont.truetype(FB, 14), fill=(15, 17, 24))
    icon(d, 26, y + 48, col)
    d.text((64, y + 44), h1, font=f_head, fill=TEXT)
    d.text((64, y + 70), det, font=f_det, fill=SUB)

img.save("entry.png", optimize=True)
print("saved")
