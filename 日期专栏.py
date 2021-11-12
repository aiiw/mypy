import time
import arrow
d=arrow.now().format('YYYY-MM-DD HH:MM:SS')#错误
d1=arrow.now().format("YYYY-MM-DD:HH:mm:ss")#正确

# for i in dir(d):#这里的time替换成需要查询的对象

#     try:
#         print('a','arrow.'+i ,type(eval('arrow.' +str(i))))#这里的time替换成需要查询的对象
#         print('b',arrow.str(10))
#     except:
#         # print(i,'error')
#         pass# 出现异常不做任何处理
# print (d.utcnow())
print(d)
print(d1)
e=arrow.utcnow().format('YYYY-MM-DD HH:MM:SS')
print(e)

t1 = arrow.now()
print(t1)


# with open(r'd:\log\f2.txt','a+') as f:
# 	f.writelines('\n')
# 	f.writelines(str(d))

# import requests
# import json

# body = {
#       "name": "yanshu",
#       "description": "yanshu's blog",
#       "price": 100,
#       "tax": 0
#     }

# body = json.dumps(body) # 需要先解析

# response = requests.put('http://127.0.0.1:8011/items/3',data = body)


