# 标题字体 MaShanZheng.ttf（马善政毛笔体）请从 Google Fonts 取得（OFL 1.1），与印章子集字体 tobpage-seal.ttf 同置于本目录
# 站名+印章整图合成：马善政毛笔体鎏金大字 + 篆字朱砂印（贴右下角）
from PIL import Image, ImageDraw, ImageFont, ImageFilter

TITLE_FONT = '/home/hatch/workspace/tobpage/assets-src/MaShanZheng.ttf'
SEAL_FONT  = '/home/hatch/workspace/tobpage/assets-src/tobpage-seal.ttf'
OUT_PNG    = '/home/hatch/workspace/tobpage/assets-src/hero-title.png'

F = 300                      # 标题字号
TRACK = int(F * 0.05)        # 字距
PAD_L, PAD_T = 40, 30
SEAL = 148                   # 印章边长
SEAL_OVER_X = 0.42           # 印章左缘压入标题右界的比例（相对印宽）
SEAL_OVER_Y = 0.60           # 印章顶缘距标题底界（相对印高，越小越靠下）

title_font = ImageFont.truetype(TITLE_FONT, F)
probe = ImageDraw.Draw(Image.new('RGBA', (10, 10)))
chars = list('普客网')
widths, boxes = [], []
for c in chars:
    b = probe.textbbox((0, 0), c, font=title_font)
    boxes.append(b); widths.append(b[2] - b[0])
text_w = sum(widths) + TRACK * (len(chars) - 1)
ink_top = min(b[1] for b in boxes); ink_bot = max(b[3] for b in boxes)
text_h = ink_bot - ink_top

W = PAD_L + text_w + int(SEAL * 0.85)
H = PAD_T + text_h + int(SEAL * 0.62)
img = Image.new('RGBA', (W, H), (0, 0, 0, 0))

# 1) 金色渐变字（先做掩模，再贴渐变；下加柔和投影增立体）
mask = Image.new('L', (W, H), 0)
md = ImageDraw.Draw(mask)
x = PAD_L
for c, b, w in zip(chars, boxes, widths):
    md.text((x - b[0], PAD_T - ink_top), c, font=title_font, fill=255)
    x += w + TRACK
shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
sh = Image.new('RGBA', (W, H), (0, 0, 0, 170))
shadow.paste(sh, (0, 7), mask.filter(ImageFilter.GaussianBlur(7)))
img.alpha_composite(shadow)
grad = Image.new('RGBA', (W, H))
gd = ImageDraw.Draw(grad)
stops = [(0.0, (246, 220, 150)), (0.45, (232, 194, 104)), (0.78, (185, 140, 52)), (1.0, (143, 106, 36))]
y0, y1 = PAD_T, PAD_T + text_h
for yy in range(y0, y1 + 1):
    t = (yy - y0) / max(1, (y1 - y0))
    for i in range(len(stops) - 1):
        if stops[i][0] <= t <= stops[i + 1][0]:
            tt = (t - stops[i][0]) / (stops[i + 1][0] - stops[i][0])
            col = tuple(int(stops[i][1][k] + (stops[i + 1][1][k] - stops[i][1][k]) * tt) for k in range(3))
            break
    gd.line([(0, yy), (W, yy)], fill=col + (255,))
img.paste(grad, (0, 0), mask)

title_right = PAD_L + text_w
title_bottom = PAD_T + text_h

# 2) 印章（单独图层，画完旋转再贴）
seal = Image.new('RGBA', (SEAL, SEAL), (0, 0, 0, 0))
sd = ImageDraw.Draw(seal)
for yy in range(SEAL):
    t = yy / SEAL
    col = tuple(int((208, 80, 56)[k] + ((165, 47, 30)[k] - (208, 80, 56)[k]) * t) for k in range(3))
    sd.line([(0, yy), (SEAL, yy)], fill=col + (255,))
base = Image.new('RGBA', (SEAL, SEAL), (0, 0, 0, 0))
bd = ImageDraw.Draw(base)
bd.rounded_rectangle([0, 0, SEAL - 1, SEAL - 1], radius=15, fill=(255, 255, 255, 255))
seal.putalpha(base.split()[3])
sd = ImageDraw.Draw(seal)
sd.rounded_rectangle([7, 7, SEAL - 8, SEAL - 8], radius=10, outline=(248, 239, 219, 115), width=3)
sf = ImageFont.truetype(SEAL_FONT, int(SEAL * 0.40))
cells = {'普': (0.71, 0.28), '客': (0.71, 0.72), '网': (0.29, 0.28), '印': (0.29, 0.72)}
for c, (cx, cy) in cells.items():
    sd.text((SEAL * cx, SEAL * cy), c, font=sf, fill=(248, 239, 219, 255), anchor='mm')
seal = seal.rotate(5, expand=True, resample=Image.BICUBIC)  # PIL 正角为逆时针，+5 等于视觉 -5°
px = int(title_right - SEAL * SEAL_OVER_X)
py = int(title_bottom - SEAL * SEAL_OVER_Y)
img.alpha_composite(seal, (px, py))
img.save(OUT_PNG)
print('saved', OUT_PNG, img.size, 'title_right/bottom =', title_right, title_bottom, 'seal at', px, py, seal.size)
