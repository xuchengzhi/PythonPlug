import os,sys
from PIL import Image,ImageDraw,ImageFont 
import shutil
import imageio


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
	
def GetGif(imglist):
    frames = []
    for i in imglist:
        frames.append(imageio.imread(i))#
    imageio.mimsave("ceshi.gif", frames, 'GIF', duration = 2)		
 
#将gif图片转成PNG图片

def iter_frames(im):
    try:
        i= 0
        while 1:
            im.seek(i)
            imframe = im.copy()
            if i == 0:
                palette = imframe.getpalette()
            else:
                imframe.putpalette(palette)
            yield imframe
            i += 1
    except EOFError:
        pass
    
 




if __name__ == '__main__':
	# GetFile()
	# img = Image.open("p/0.png")
	# img = transparent_back(img)
	# img.show()
	# img.save("111.png")
    im = Image.open('1.gif')
    frames = []
    for i, frame in enumerate(iter_frames(im)):

        frame.save("p/"+str(i)+'.png',**frame.info)
        img = Image.open("p/"+str(i)+'.png')
        img = transparent_back(img)
        img.save("new/"+str(i)+'.png')
        frames.append(imageio.imread("new/"+str(i)+'.png'))
    imageio.mimsave("ceshi.gif", frames, 'GIF', duration = 2)
    # shutil.rmtree("p")
