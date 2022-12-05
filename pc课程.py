import os
import requests,json
from urllib.parse import  quote,unquote
from urllib import request
from remonth import remonths

ua='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
header  =  {"User-Agent"  : ua,
            "Cookie":r"connect.sid=s:jSCYyrvq0iNfj4zjYzX3dYCuZz-f7hbE.RzSSheWzrUnLrptwx6nxvPP4cVOFJUen8g+JamImkgs"
            }

i2 = requests.get('https://upload.mzyun.ren/pdf/web/viewer.html?file=https://public.mzyun.ren/ppd/2923be60-146a-11ec-9d0b-bfdb0beb590a.pdf', headers = header)
print(i2.content.decode('utf-8','ignore'))

# from selenium import webdriver
# import time

# # 实例化一款浏览器
# from selenium import webdriver

# mychrome = webdriver.Chrome()

# mychrome.get("https://www.mzyun.ren/")