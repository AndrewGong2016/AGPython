#!/usr/bin/python3


import urllib.request
import os

while True:
    try:
        url = "https://dldir1.qq.com/weixin/android/weixin7014android1660.apk" #weichact apk。
        dir = os.getcwd(); #当前工作目录。
        urllib.request.urlretrieve(url, dir + '\\weixin.apk') #下载图片
    except:
        print ("unexcepted")
        break


