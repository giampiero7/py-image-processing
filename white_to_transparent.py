import sys
import os
import Image

if len(sys.argv) < 2:
	print ''
	print '\tUsage: python ' + sys.argv[0] + ' image_file'
	print '\tExample: python ' + sys.argv[0] + ' img.png'
	print ''
	sys.exit(0)

for i in range(1, len(sys.argv)):
	img = Image.open(sys.argv[i]).convert('RGBA')
	datas = img.getdata()
	newData = []
	for item in datas:
	    if item[0] == 255 and item[1] == 255 and item[2] == 255:
	        newData.append((255, 255, 255, 0))
	    else:
	        newData.append(item)
	img.putdata(newData)
	img.save(os.path.splitext(sys.argv[i])[0] + '_transp' + os.path.splitext(sys.argv[i])[1])
