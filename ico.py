# -*- coding: utf-8 -*-
import zipfile
import PythonMagick
img = PythonMagick.Image("E:\code\py\Annual\ico.png")
img.sample('100x100')
img.write(r'E:\code\py\Annual\001.ico')
# img.write('001.png')
# img.write('001.gif')