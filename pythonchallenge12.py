# http://www.pythonchallenge.com/pc/return/evil.html

from PIL import Image
from io import BytesIO

s = open("evil2.gfx", "rb").read()
for i in range(5):
    piece = s[i::5]  # every fifth byte, starting at i
    im = Image.open(BytesIO(piece))
    f = open("%d.%s" % (i, im.format.lower()), "wb")
    f.write(piece)
    f.close()

