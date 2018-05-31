import sys
import os
from PIL import Image

if len(sys.argv) < 2:
	print ''
	print '\tUsage: python ' + sys.argv[0] + ' image_file'
	print '\tExample: python ' + sys.argv[0] + ' img.png'
	print ''
	sys.exit(0)

def invert(image):
    return image.point(lambda p: 255 - p)

for i in range(1, len(sys.argv)):
	img = Image.open(sys.argv[i]).convert('RGBA')
	r, g, b, a = img.split()
	a = invert(a)
	img2 = Image.merge(img.mode, (r, g, b, a))
	img2.save(os.path.splitext(sys.argv[i])[0] + '_inverted' + os.path.splitext(sys.argv[i])[1])
