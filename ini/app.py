# -*- coding: utf-8 -*-
import os
import sys
from bs4 import BeautifulSoup
import re
from lxml.html.clean import Cleaner
import datetime
import json
from flask import Flask,render_template,jsonify
from flask import request
from flask import render_template
from flask import redirect
from flask import make_response
from werkzeug.utils import secure_filename
import time
import webbrowser
reload(sys)
nowtime=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
sys.setdefaultencoding("utf-8")

zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')

teshu =["，","。","！","~","：","；","、","？","...","， "]


app = Flask(__name__)


def is_chinese(uchar):

        """判断一个unicode是否是汉字"""

        if uchar >= u'/u4e00' and uchar<=u'/u9fa5':

                return True

        else:

                return False

def contain_zh(word):
    '''
    判断传入字符串是否包含中文
    :param word: 待判断字符串
    :return: True:包含中文  False:不包含中文
    '''
    word = word.decode()
    global zh_pattern
    match = zh_pattern.search(word)
    return match


def readfile(file,ininame):
	# logwrite("run model _2")
	clsss = ""
	print("{} *****{}".format(file,type(file)))
	# logwrite(file)
	try:
		f = open(file.decode('utf-8'))
	except Exception as e:
		raise e
	html = str(f.readlines())
	soup= BeautifulSoup(html)
	trs=soup.findAll("script")
	length=len(trs)
	arr=[]
	Str=""
	pattern = re.compile(r'function()*?', re.I | re.M)
	dict_={}
	dict_["padding"]=25
	pages=[]
	pag_1={}
	
	
	ini_file = open(ininame,"a")
	for i in range(length):
   		s = trs[i].contents[0]
   		urls = pattern.findall(s)
   		text_s=s[169816:-1].replace("$(function()","").replace("-->\\n',","").replace(");\\n',","").replace("'     '","")
   		str_text=((text_s.encode('unicode-escape').decode('string_escape').replace("SMApp","").replace("{ (","").replace(") } ","")))
   		dict_text=(eval(str_text))
   		code_list=dict_text.get('artboards')
   		
   		dict_["pages"]=pages
   		
   		for i in range(len(code_list)):

   			code_dict = code_list[i]
   			pageName=code_dict.get('pageName')
   			print(pageName)
   			p_dic={}
   			layers = code_dict.get('layers')
   			layers_len = len(layers)
   			chars=[]
   			for i in range(layers_len):
   				code_3=layers[i]
   				if  contain_zh(code_3.get('name')):
   					rotation=(code_3.get('rotation'))
	   				width =(code_3.get("rect").get('width'))
	   				height =(code_3.get("rect").get('height'))
	   				x =(code_3.get("rect").get('x'))
	   				y =(code_3.get("rect").get('y'))
	   				character = code_3.get("name").strip()
	   				pag_1["x"] = x*2
	   				pag_1["y"] = y*2
	   				pag_1["size"] = int(width)*2
	   				pag_1["character"] = character.decode('utf-8')
	   				pag_1["rotation"] =rotation*2
	   				chars.append((json.dumps(pag_1).decode('unicode-escape')))
	   				# print(pag_1)
	   				# print("=="*10)
	   			elif code_3.get('name') in teshu:
	   				rotation=(code_3.get('rotation'))
	   				width =(code_3.get("rect").get('width'))
	   				height =(code_3.get("rect").get('height'))
	   				x =(code_3.get("rect").get('x'))
	   				y =(code_3.get("rect").get('y'))
	   				character = code_3.get("name").strip()
	   				pag_1["x"] = x*2
	   				pag_1["y"] = y*2
	   				pag_1["size"] = int(width)*2
	   				pag_1["character"] = character.decode('utf-8')
	   				pag_1["rotation"] =rotation*2
	   				chars.append((json.dumps(pag_1).decode('unicode-escape')))
	   				if i == layers_len -1:
	   					pass
	   				else:
	   					pass
	   			else :
	   				pass
	   			p_dic["chars"]=chars
	   			# print(p_dic)
   			pages.append(p_dic)
	rs=json.dumps(dict_, encoding='UTF-8', ensure_ascii=False).replace('\\','').replace("\"{","{").replace("}\"","}")
	# print(rs)
	ini_file.write(rs)

	


ALLOWED_EXTENSIONS = set(['html','HTML'])

# 用于判断文件后缀
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS



@app.route('/update', methods=['GET', "POST"])
def updatefile():
    f = request.files['file']
    # response = make_response(render_template('index.html'))
    # response.delete_cookie('key')
    # response.set_cookie('key', 'value')
    # response.headers['X-Something'] = 'A value'
    if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型
        fname = secure_filename(f.filename)
        ext = fname.rsplit('.',1)[1]  # 获取文件后缀
        unix_time = int(time.time())
        new_filename = str(unix_time)+'.ini'  # 修改了上传的文件名
        f.save(os.path.join("tmp", "tmp.html"))
	print("/Users/miaomiaoyin/Desktop/ini/"+new_filename)
        readfile("tmp/tmp.html","/Users/miaomiaoyin/Desktop/ini/"+new_filename)
        return render_template('index.html',ww=new_filename)
    else:
        return jsonify({"errno": 1001, "errmsg": u"failed"})

@app.route('/')
def indexview():
    return render_template('index.html', ww="")

if __name__ == '__main__':
    webbrowser.open("http://192.168.248.144:5000")
    app.run(host='0.0.0.0',port=5000)

    
