import sys
import os
from PIL import Image

if len(sys.argv) < 5:
	print ''
	print '\tUsage: python ' + sys.argv[0] + ' image_file r g b'
	print '\tExample: python ' + sys.argv[0] + ' img.png 20 30 255'
	print ''
	sys.exit(0)

def tint(image, c):
    return image.point(lambda p: c)

for i in range(1, len(sys.argv) - 3):
	img = Image.open(sys.argv[i]).convert('RGBA')
	r, g, b, a = img.split()
	l = len(sys.argv)
	r = tint(r, int(sys.argv[l - 3]))
	g = tint(g, int(sys.argv[l - 2]))
	b = tint(b, int(sys.argv[l - 1]))
	img2 = Image.merge(img.mode, (r, g, b, a))
	img2.save(os.path.splitext(sys.argv[i])[0] + '_tinted' + os.path.splitext(sys.argv[i])[1])
