# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 12:52:57 2022

@author: Ryan
"""



# encoding:utf-8
import requests 

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=xFZeSRjaIfqwKCBicAQkTTaU&client_secret=wQyeqtVhAjIlzSkKBIrpbnchu9UIyGbh'
response = requests.get(host)
if response:
    print(response.json())
    
# 'access_token': '24.cc1f7205fe00e022c6b09558a9dd52f0.2592000.1648962980.282335-25704329'
# 'expires_in': 2592000