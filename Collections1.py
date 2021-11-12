dic={}
dic['a']='a'

# dict =defaultdict( factory_function)
# 这个factory_function可以是list、set、str等等，作用是当key不存在时，返回的是工厂函数的默认值，
#比如list对应[ ]，str对应的是空字符串，set对应set( )，int对应0，如下举例：

from collections import defaultdict

dict1 = defaultdict(int)
dict2 = defaultdict(set)
dict3 = defaultdict(str)
dict4 = defaultdict(list)
dict1[2] ='two'
dict4["a"].append("aaa")
dict4['a'].append("abs")
dict4["a"].append("bbs")
dict4['b']="bbbb"
dict4['adsd'].append("dsafd")
print(dict(dict4)) #这个解决了当时的问题,所以应该很好用吧
tdict4=dict(dict4)
print(tdict4.get('a'))
print(dict4)
print(dict4.items())
print(dict(dict4.items())) #这个就转换为字典了~~

#字典也是可以append的,首先定义了key的值为[]

a = [11,22,33,44,55,66,77,88,99,90]
b ={
"key1" : [],
"key2" : []
}
for i in a:
    if i > 66:
        b["key1"].append(i)
    elif i < 66:
        b["key2"].append(i)
print(b)

print("------------list-----------------")
import collections 
dic = collections.defaultdict(list)    
#指定字典的值为列表 
dic["k1"].append("kkkkk") 
dic["k1"].append("kkkkk") 
dic["k1"].append("kkkkk") 
print(dict(dic) )

print("------------tree-----------------")
from collections import defaultdict
def tree(): return defaultdict(tree)
d = tree()
d["person"]["name"]["first_name"] = 'raymon'
d["person"]["name"]["last_name"] = 'Gen'
d["person"]["age"] = 18
# for key,values in d.iteritems():
# 	print(key,'aa')
# print(d["person"][2][1])
# #[{"id":1,"text":"text1"},{"id":2,"text":"text2"},{"id":3,"text":"text3","selected":true},{"id":4,"text":"text4"},{"id":5,"text":"text5"}]

import datetime
import arrow
from dateutil import rrule
a = arrow.now()
year = str(a.year)
month = str(a.month)
day = str(a.day)
d1 = datetime.date(2018, 10, 29)
d2 = datetime.date(2021, 8, 1)

months = rrule.rrule(rrule.MONTHLY, dtstart=d1, until=d2).count()

print(f"months={months}")


d1 = datetime.datetime.strptime('2012-03-05 17:41:20', '%Y-%m-%d %H:%M:%S')
d2 = datetime.datetime.strptime('2013-03-02 17:41:20', '%Y-%m-%d %H:%M:%S')
delta = d1 - d2
print (delta)