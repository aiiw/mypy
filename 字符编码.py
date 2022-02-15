#coding:gbk
import sys,json
print(sys.getdefaultencoding())
a="中"
s="中"
s = s.encode('unicode_escape')
print(s)
a1=a.encode()
print(a1)
a2=a.encode('utf-8')
print(a2)
a3=a.encode('gbk')
print(a3)
# s1 = {'TO_UID':'1','TO_NAME':'','TD_HTML_EDITOR_CONTENT':a1,'I_VER':'2','C':'web','ACTION_TYPE':'sms'}
# # encode 卤脿脗毛拢卢脠莽潞脦陆芦str --> bytes, ()
# # s11=json.dumps(s1)
# # s12 = s11.encode('utf-8')
# # print(s12)
# # s12 = s11.encode('gbk')
# # print(s12)
# print(s1,type(a1))

# # s2='脛茫脫脨脪禄脤玫脨脗碌脛脨脜脧垄,脟毛脳垄脪芒虏茅脢脮'
# # print(s2.encode('utf-8'))
# # print(s2.encode('gbk'))
from urllib.parse import  quote,unquote
from bs4 import BeautifulSoup
import re
html_doc='''
error during connect: Get http://%2F%2F.%2Fpipe%2Fdocker_engine/v1.37/containers/json: open //./pipe/docker_engine: The system cannot find the file specified. In the default daemon configuration on Windows, the docker client must be run elevated to connect. This error may also indicate that the docker daemon is not running.
'''

print(unquote(html_doc)) #quote url编码 unquote url解码
# html_doc1=html_doc.encode().decode()
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.select('span'))
b='方高燕'
print('unicode',b.encode('unicode_escape'))
print('utf-8   ',b.encode('utf-8'))
print('utf-8   ',b.encode('gbk'))
print('gbk  ',b.encode('gbk').decode('gbk').encode('gbk'))

u=b.encode('unicode_escape')
print(u.encode())


