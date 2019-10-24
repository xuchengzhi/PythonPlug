import itchat
import re
import jieba
import matplotlib.pyplot as plt
import PIL.Image as Image
import numpy as np
import os
from wordcloud import WordCloud,ImageColorGenerator
 
TList = ["我与父亲不相见已二年余了我最不能忘记的是他的背影那年冬天祖母死了父亲的差使也交卸了正是祸不单行的日子我从北京到徐州打算跟着父亲奔丧回家到徐州见着父亲看见满院狼藉的东西又想起祖母不禁簌簌地流下眼泪父亲说事已如此不必难过好在天无绝人之路回家变卖典质父亲还了亏空又借钱办了丧事这些日子家中光景很是惨澹一半为了丧事一半为了父亲赋闲丧事完毕父亲要到南京谋事我也要回北京念书我们便同行到南京时有朋友约去游逛勾留了一日第二日上午便须渡江到浦口下午上车北去父亲因为事忙本已说定不送我叫旅馆里一个熟识的茶房陪我同去他再三嘱咐茶房甚是仔细但他终于不放心怕茶房不妥帖颇踌躇了一会其实我那年已二十岁北京已来往过"]
 
def cloud_pic():
    raw_signature_string = ''.join(TList)
    text = jieba.cut(raw_signature_string, cut_all=True)
    wl_space_split = ' '.join(text)
 
    d = os.path.dirname(os.path.abspath(__file__))
 
    alice_coloring = np.array(Image.open(os.path.join(d, "1.png"))) #原图
 
    my_wordcloud = WordCloud(background_color="white", #背景色
            max_words=2000,    #字数上限
            mask=alice_coloring, #形状
            max_font_size=100,#字体大小
            random_state=150, #随机数量
            font_path='huocaiti.ttf').generate(wl_space_split) #中文字体
    image_color = ImageColorGenerator(alice_coloring)
    my_wordcloud.recolor(color_func=image_color)
    my_wordcloud.to_file('result.png')
 
def main():
    cloud_pic()
 
if __name__ == '__main__':
    main()
 
 

