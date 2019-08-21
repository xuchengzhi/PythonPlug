#-*- coding: UTF-8 -*-
from PIL import Image
import imageio
import os,sys

# os.chdir("tupian")
def create_gif(image_list, gif_name):
 
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    # Save them as frames into a gif
    imageio.mimsave(gif_name, frames, 'GIF', duration = 0.1)
 
    return

def analyseImage(path):  
    ''''' 
    Pre-process pass over the image to determine the mode (full or additive). 
    Necessary as assessing single frames isn't reliable. Need to know the mode  
    before processing all frames. 
    '''  
    im = Image.open(path)  
    results = {  
        'size': im.size,  
        'mode': 'full',  
    }  
    try:  
        while True:  
            if im.tile:  
                tile = im.tile[0]  
                update_region = tile[1]  
                update_region_dimensions = update_region[2:]  
                if update_region_dimensions != im.size:  
                    results['mode'] = 'partial'  
                    break  
            im.seek(im.tell() + 1)  
    except EOFError:  
        pass  
    return results  
  
  
def processImage(path):  
    photo_file=path.split(".")[-2]
    photo_files=[]
    if os.path.exists(photo_file):
        print "ok"
    else :
        os.mkdir(photo_file)
    ''''' 
    Iterate the GIF, extracting each frame. 
    '''  
    
    mode = analyseImage(path)['mode']  
      
    im = Image.open(path)  
  
    i = 0  
    p = im.getpalette()  
    last_frame = im.convert('RGBA')  
    photo_list=[]
    try:  
        while True:  
            print "saving %s (%s) frame %d, %s %s" % (path, mode, i, im.size, im.tile)  
              
            ''''' 
            If the GIF uses local colour tables, each frame will have its own palette. 
            If not, we need to apply the global palette to the new frame. 
            '''  
            if not im.getpalette():  
                im.putpalette(p)  
              
            new_frame = Image.new('RGBA', im.size)  
              
            ''''' 
            Is this file a "partial"-mode GIF where frames update a region of a different size to the entire image? 
            If so, we need to construct the new frame by pasting it on top of the preceding frames. 
            '''  
            if mode == 'partial':  
                new_frame.paste(last_frame)  
              
            new_frame.paste(im, (0,0), im.convert('RGBA')) 
            name=("./"+photo_file+'/%s-%d.png' % (''.join(os.path.basename(path).split('.')[:-1]), i))
            photo_list.append(name)
            photo_files.append(photo_file)
            new_frame.save(photo_file+'/%s-%d.png' % (''.join(os.path.basename(path).split('.')[:-1]), i), 'PNG')  
            
            i += 1  
            last_frame = new_frame  
            im.seek(im.tell() + 1)  
    except EOFError:  
        pass  

    return {"photo_list":photo_list,"photo_file":photo_files}
def hebing(image_list,photo_file):
    file_name=[]
    for i in range(len(image_list)):
        base_img = Image.open(ur'./3.png')

        target = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
        box = (166, 64, 320, 337)
        region = Image.open(ur'./{}'.format(image_list[i]))
        region = region.rotate(0)

        region = region.convert("RGBA")
        region = region.resize((box[2] - box[0], box[3] - box[1]))

        target.paste(region,box)

        target.paste(base_img,(0,0),base_img) 
        target.save('./{}/{}.png'.format(photo_file[0],i))
        file_name.append('{}/{}.png'.format(photo_file[0],i))
    return file_name

def main():
    res=processImage('001.gif')
    photo_list=res.get("photo_list")
    image_list=res.get("photo_file")
    # print hebing(photo_list,image_list)
    
    gif_name = raw_input("请输入gif图片名称：\n")
    create_gif(hebing(photo_list,image_list), gif_name)

if __name__ == "__main__":
    main()
