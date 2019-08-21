import os,sys
from PIL import Image,ImageDraw,ImageFont 
import shutil

def readfile():
    try:
        f = open("6656字模板-unicode.txt","rb")
    except Exception as e:
        raise e
    
    
    code_list = []
    code_dict = {}
    for i in f:
        tmp = str(i).replace("\\r\\n","").split(" ")[0].replace("b'","")
        tmp = tmp.replace("\\xef\\xbb\\xbf","").replace("b\\","")
        tmp = tmp.replace("b\"","")
        num = sixteen_to_ten(tmp)
        msg = tentofont(num)
        code_list.append(tmp)
        Photo(str(num[0]),msg)
        CopyFile(str(num[0]))
    code_dict["codes"] = code_list
    with open("new1/SJZZ.conf","w") as f:
        f.write(str(code_dict).replace("{","{\n\t").replace("'","\"").replace("[\"","[\n\t\"").replace("]}","\n\t]\n}").replace("\", \"","\",\n\t\""))
        f.close()

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
    f =  Image.new('RGBA', (500, 500), (255, 255, 255, 0))
    font = ImageFont.truetype("lang.otf", 280)
    draw = ImageDraw.Draw(f)
    # draw.text((100,100),msg,font=font, fill=(0,0,0,255))
    draw.text((100,100),".",font=font, fill=(0,0,0,255))
    f = f.convert('P')
    f.save("new1/"+name+".png")

def To8bit(img):
    lena = Image.open(img)
    lena = lena.convert('P')
    lena.save(img)


def CopyFile(name):
    try:
        shutil.copy("12354.gz","new1/"+name+".gz")
    except Exception as e:
        raise e
    



if __name__ == '__main__':
    readfile()