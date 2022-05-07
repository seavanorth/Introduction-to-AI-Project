# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 13:22:05 2022

@author: Ryan
"""

image_path = 'F:/Blue-Image/[Graphis]/20210613/gra_tsubaki-s2_112.jpg'

# encoding:utf-8

import requests
import base64

'''
人像动漫化
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/selfie_anime"
# 二进制方式打开图片文件
f = open(image_path, 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = 'xxx'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())
    
# https://aip.baidubce.com/rest/2.0/image-process/v1/selfie_anime
# 24.cc1f7205fe00e022c6b09558a9dd52f0.2592000.1648962980.282335-25704329

import json

image_name = 'SA'

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
 
 

 
 
