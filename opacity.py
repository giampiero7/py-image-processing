import sys
import os
import Image

if len(sys.argv) < 3:
	print ''
	print '\tUsage: ' + sys.argv[0] + ' image_file opacity'
	print '\tExample: ' + sys.argv[0] + ' img.png 0.4'
	print ''
	sys.exit(0)
	
img = Image.open(sys.argv[1]).convert('RGBA')

r, g, b, a = img.split()

def opacity(image):
    return image.point(lambda p: p * float(sys.argv[2]))

a = opacity(a)

img2 = Image.merge(img.mode, (r, g, b, a))

img2.save(os.path.splitext(sys.argv[1])[0] + '_opacity_' + str(sys.argv[2]) + os.path.splitext(sys.argv[1])[1])
