
########################################## arrow #################################################################
import arrow
d=arrow.now().format('YYYY-MM-DD HH:MM:SS')#错误
d1=arrow.now().format("YYYY-MM-DD:HH:mm:ss")#正确
#日期运算
t = arrow.now()
t1=t.shift(hours=-1)  # 前一天 weeks months years hours days
print(t1.format("YYYY-MM-DD:HH:mm:ss"))  # 前一天) 

print(d)
print(d1)
e=arrow.utcnow().format('YYYY-MM-DD HH:MM:SS')
print(e)

t1 = arrow.now()
print(t1)

###################################################################################################################
#from DateTime.DateTime import datetime
from datetime import datetime, date, time, timezone

# 当前时间+3天 print(datetime.datetime.now() + datetime.timedelta(3))
print(datetime.now()) # datatime.now 取当前时间

print(date.today())  #取当前日期
print("使用time 表示")
#使用time 表示
import time
# 把结构化时间转换为格式化时间 # %Y年-%m月-%d天 %X时分秒=%H时:%M分:%S秒 
print(time.strftime("%Y-%m-%d %X", time.localtime() )) #取当前日期
# 把格式化时间化为结构化时间，它和strftime()是逆操作 
print(time.strptime('2013-05-20 13:14:52', '%Y-%m-%d %X'))
start = time.time() 
time.sleep(0.1) 
end = time.time()
total_time=end-start
print(time.strftime("%X",time.localtime(total_time)))
print(time.strftime("%Y-%m-%d %X",time.gmtime(11111123))) #GMTIME是按标准时间 LOCALTIME是按了北京时间
now_time=time.time()
#将秒变为日期
print("将秒变为日期")
print(time.strftime("%H:%M:%S", time.gmtime(36000)))
def mmtohh(mm:int)->str:
	days=str(mm//3600//24)
	times=str(time.strftime("%H:%M:%S", time.gmtime(mm)))
	return days+"天"+times

print(mmtohh(13600))
print(time.time())
