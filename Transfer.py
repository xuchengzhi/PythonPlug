import os,sys
from PIL import Image,ImageDraw,ImageFont 
import shutil



def Photo(p,name):
    #生成图片
    f = Image.open(p+"/"+name)
    x,y = f.size
    
    n =  Image.new('RGBA', (x, y), (0, 0, 0, 0))
    box=(0,0,x,y)
    # # draw.text((100,100),msg,font=font, fill=(0,0,0,255))
    new = p.replace("Desktop","Desktop/New")
    if os.path.exists(new):
    	pass
    else:
    	os.makedirs(new)

    region = f.crop(box)
    r, g, b, alpha = n.split()
    n.paste(region,box)
    n = n.convert('P')
    n = transparent_back(n)
    n.save(new+"/"+name)
    f.close()


def transparent_back(img):
	img = img.convert('RGBA')
	L, H = img.size
	color_0 = img.getpixel((0,0))
	for h in range(H):
		for l in range(L):
			dot = (l,h)
			color_1 = img.getpixel(dot)
			if color_1 == color_0:
				color_1 = color_1[:-1] + (0,)
				img.putpixel(dot,color_1)
	return img




path = "/Users/xxx/Desktop/处理文件"

def GetFile():
	for root,dirs,files in os.walk(path):
		for i in range(len(files)):
			if files[i].endswith("png"):
				Photo(root,files[i])
			




if __name__ == '__main__':
	GetFile()
	# img = Image.open("ceshi.png")
	# img = transparent_back(img)
	# img.show()
	# img.save("111.png")