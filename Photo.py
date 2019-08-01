import os,sys
from PIL import Image,ImageDraw,ImageFont 
import shutil

def tentofont(msglist):
    '''10进制转汉字'''
    word=''
    # print(msglist)
    for msg in msglist:
        try:
            msg1='{:x}'.format(int(msg))
            msg2="\\u"+msg1
            word+=msg2.decode("unicode_escape")
        except Exception as e:

            word+=chr(int(msg))
    return word



def sixteen_to_ten(num):
    '''16进制转10进制'''
    nums = []
    if ',' in num:
        num = num.split(',')
        for i in num:
            msg ="0x"+i
            nums.append(int(msg,16))
    elif '\\u' in num:
        tmp = num.replace("\\u",',')
        
        num = tmp.split(',')
        print(num)
        for i in num:
            if i == ',' or i =='':
                pass
            else:
                msg ="0x"+i
                nums.append(int(msg,16))
    else:
        msg ="0x"+num
        nums.append(int(msg,16))
    

    
    return nums

def Photo(name,msg):
    #生成图片
    f =  Image.new('RGBA', (500, 500), (255, 255, 255, 0))
    font = ImageFont.truetype("lang.otf", 280)
    draw = ImageDraw.Draw(f)
    draw.text((100,100),msg,font=font, fill=(0,0,0,255))
    # f = f.convert('P')#转8位深度
    f.save(name+".png")

def To8bit(img):
    lena = Image.open(img)
    lena = lena.convert('P')
    lena.save(img)
    

if __name__ == '__main__':
    Photo("32","ceshi")
    To8bit("32.png")