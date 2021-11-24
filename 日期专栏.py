
import arrow
d=arrow.now().format('YYYY-MM-DD HH:MM:SS')#错误
d1=arrow.now().format("YYYY-MM-DD:HH:mm:ss")#正确


print(d)
print(d1)
e=arrow.utcnow().format('YYYY-MM-DD HH:MM:SS')
print(e)

t1 = arrow.now()
print(t1)


#from DateTime.DateTime import datetime
from datetime import datetime, date, time, timezone

# 当前时间+3天 print(datetime.datetime.now() + datetime.timedelta(3))
print(datetime.now())

print(date.today())

#使用time 表示
import time
# 把结构化时间转换为格式化时间 # %Y年-%m月-%d天 %X时分秒=%H时:%M分:%S秒 
print(time.strftime("%Y-%m-%d %X", time.localtime() ))
# 把格式化时间化为结构化时间，它和strftime()是逆操作 
print(time.strptime('2013-05-20 13:14:52', '%Y-%m-%d %X'))
start = time.time() 
time.sleep(3) 
end = time.time()
print(time.strftime("%Y-%m-%d %X", time.localtime(start) ),end,end-start)

