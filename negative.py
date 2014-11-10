import sys
import os
import Image

if len(sys.argv) < 2:
	print ''
	print '\tUsage: ' + sys.argv[0] + ' image_file'
	print '\tExample: ' + sys.argv[0] + ' img.png'
	print ''
	sys.exit(0)

img = Image.open(sys.argv[1]).convert('RGBA')

r, g, b, a = img.split()

def negative(image):
    return image.point(lambda p: 255 - p)

r = negative(r)
g = negative(g)
b = negative(b)


img2 = Image.merge(img.mode, (r, g, b, a))

img2.save(os.path.splitext(sys.argv[1])[0] + '_negative' + os.path.splitext(sys.argv[1])[1])