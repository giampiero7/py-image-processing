import sys
import os
from PIL import Image

if len(sys.argv) < 6:
	print ''
	print '\tUsage: ' + sys.argv[0] + ' image_file left up right bottom'
	print '\tExample: ' + sys.argv[0] + ' img.png 10 20 10 10'
	print ''
	sys.exit(0)

argvLen = len(sys.argv);
left = int(sys.argv[argvLen - 4]);
up = int(sys.argv[argvLen - 3]);
right = int(sys.argv[argvLen - 2]);
bottom = int(sys.argv[argvLen - 1]);

for i in range(1, len(sys.argv) - 4):
	img = Image.open(sys.argv[i])
	w, h = img.size
	img2 = img.crop((left, up, w - right, h - bottom));
	img2.save(os.path.splitext(sys.argv[i])[0] + '_cropped' + os.path.splitext(sys.argv[i])[1])
