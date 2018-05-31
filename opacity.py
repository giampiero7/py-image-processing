import sys
import os
from PIL import Image

if len(sys.argv) < 3:
	print ''
	print '\tUsage: ' + sys.argv[0] + ' image_file opacity'
	print '\tExample: ' + sys.argv[0] + ' img.png 0.4'
	print ''
	sys.exit(0)

def opacity(image):
    return image.point(lambda p: p * float(sys.argv[len(sys.argv) - 1]))

for i in range(1, len(sys.argv) - 1):
	img = Image.open(sys.argv[i]).convert('RGBA')
	r, g, b, a = img.split()
	a = opacity(a)
	img2 = Image.merge(img.mode, (r, g, b, a))
	img2.save(os.path.splitext(sys.argv[i])[0] + '_opacity_' + str(sys.argv[len(sys.argv) - 1]) + os.path.splitext(sys.argv[i])[1])
