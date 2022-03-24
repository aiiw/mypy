from flask import Flask, make_response,request

import json

import string

import hashlib

import random

import time

import urllib

import redis

import requests


r = redis.Redis(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379


appid = 'wwda00f8b50a26dbd2' 

sceret = 'ANWGMbduyJhzLoragXRKuYYdH9y4QcDfxNS7oQXc7w0'
sceret='qUnxp4hfdkV9Lseh06CnjWNVYTSWKK84TszSrgq1kuY' #通信录的私钥

def get__token(appid,sceret): 

	ACCESS_TOKEN = r.get('wx:ACCESS_TOKEN') # 从redis中获取ACCESS_TOKEN

	if ACCESS_TOKEN:

		return ACCESS_TOKEN

	try:

		token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}".format(appid,sceret) # 创建获取token的url

		response = urllib.request.urlopen(token_url)

		b = response.read().decode('utf-8')

		token = json.loads(b)

		ACCESS_TOKEN = token.get("access_token")

		#r.setex('wx:ACCESS_TOKEN', ACCESS_TOKEN, 7200) # 将获取到的 ACCESS_TOKEN 存入redis中并且设置过期时间为7200s  这里有一个坑,看到没有?

		r.setex('wx:ACCESS_TOKEN', 7200,ACCESS_TOKEN)


		return ACCESS_TOKEN

	except Exception as e:

		return e


# https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid='wwda00f8b50a26dbd2'&corpsecret='ANWGMbduyJhzLoragXRKuYYdH9y4QcDfxNS7oQXc7w0'

def wxapi():
	ACCESS_TOKEN=get__token(appid,sceret)
	dept_id='1'
	op='1'
	api_url='https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token={}&department_id={}&fetch_child={}'.format(ACCESS_TOKEN,dept_id,op)
	response=requests.get(api_url)
	b = response.content.decode( 'utf-8' )





def getemp(user_id):
	
	ACCESS_TOKEN=get__token(appid,sceret)


	api_url='https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={}&userid={}'.format(ACCESS_TOKEN,user_id)
	response=requests.get(api_url).text
	response1=json.loads(response)
	response2=json.dumps(response1,indent=3,sort_keys=True,ensure_ascii=False)
	#print json.dumps(dic,ensure_ascii=False).decode("utf-8").encode("gb2312") #{"a":"中国"}
	print(response2)


if __name__ == '__main__':
	# getdept() #获取指定部门
	getemp('11608')

