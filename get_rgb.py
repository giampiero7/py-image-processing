import sys
import os
from PIL import Image

if len(sys.argv) < 2:
	print('')
	print('\tPrints RGBA values of first pixel in image files')
	print('')
	print('\tUsage: python ' + sys.argv[0] + ' image_file')
	print('')
	sys.exit(0)

for i in range(1, len(sys.argv)):
	print(sys.argv[i])
	img = Image.open(sys.argv[i])
	print(img.getdata()[0])
