# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 00:23:50 2022

@author: Ryan
"""

'''
cartoon：卡通画风格
pencil：铅笔风格
color_pencil：彩色铅笔画风格
warm：彩色糖块油画风格
wave：神奈川冲浪里油画风格
lavender：薰衣草油画风格
mononoke：奇异油画风格
scream：呐喊油画风格
gothic：哥特油画风格
'''

image_path = 'xxx'

# encoding:utf-8

import requests
import base64

'''
图像风格转换
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/style_trans"
# 二进制方式打开图片文件
f = open(image_path, 'rb')
img = base64.b64encode(f.read())

params = {"image":img,"option":"cartoon"} #  Replacable
access_token = 'xxx'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())
    
    
import json

image_name = 'ST'

json_str = json.dumps(response.json()['image'])
file=open(image_name + '.txt','wt')#写成文本格式
file.write(json_str)
file.close()
    
import os,base64 
 
with open(image_name + '.txt',"r") as f:
    imgdata = base64.b64decode(f.read())
    file = open(image_name + '.jpg','wb')
    file.write(imgdata)
    file.close()
