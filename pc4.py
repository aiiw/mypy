import requests
from lxml import html


# headers["abce"]="abc"
# url="http://192.168.0.7:8075/api/01"
# t=requests.post(url,headers=headers)
# print(t.headers)
headers={"content-type": "application/json","digi-protocol": "raw","digi-type": "sync"}
print(headers)