#kod för deutschlands flagga
from PIL import Image, ImageDraw

SVART = (0, 0, 0)
RÖD = (255, 0, 0)
GUL = (255, 206, 0)

tyskland = Image.new("RGB", (300, 180))

imd = ImageDraw.Draw(tyskland)

imd.rectangle([0, 0, 300, 60], fill=SVART)
imd.rectangle([0, 60, 300, 120], fill=RÖD)
imd.rectangle([0, 120, 300, 180], fill=GUL)

tyskland.save("flag-done/tyskland.png")