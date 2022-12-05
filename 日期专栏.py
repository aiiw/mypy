
########################################## arrow #################################################################
import arrow
from  datetime import timedelta #([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
a=timedelta(days=1,minutes=12)
b=arrow.now()+a
print(b)
d=arrow.now().format('YYYY-MM-DD HH:MM:SS')#错误
d1=arrow.now().format("YYYY-MM-DD:HH:mm:ss")#正确
#日期运算
t = arrow.now()
t1=t.shift(hours=-1)  # 前一天 weeks months years hours days
print(t1.format("YYYY-MM-DD:HH:mm:ss"))  # 前一天) 
a1=arrow.get('2022-02-01 12:15:15', 'YYYY-MM-DD HH:mm:ss') #这里少一个冒号

b2=arrow.get('2021-03-01')
print("b2-a1",b2-a1)
dd=b2-a1
print(type(dd))
print(d)
print(d1)
e=arrow.utcnow().format('YYYY-MM-DD HH:MM:SS')
print(e)

t1 = arrow.now()
print(t1)

###################################################################################################################
# #from DateTime.DateTime import datetime
# from datetime import datetime, date, time, timezone

# # 当前时间+3天 print(datetime.datetime.now() + datetime.timedelta(3))
# print("datatime.now 取当前时间",datetime.now()) # datatime.now 取当前时间

# print(date.today())  #取当前日期
# print("使用time 表示")
# #使用time 表示
# import time
# # 把结构化时间转换为格式化时间 # %Y年-%m月-%d天 %X时分秒=%H时:%M分:%S秒 
# print("把结构化时间转换为格式化时间 # %Y年-%m月-%d天 %X时分秒=%H时:%M分:%S秒 ",time.strftime("%Y-%m-%d %X", time.localtime() )) #取当前日期
# # 把格式化时间化为结构化时间，它和strftime()是逆操作 
# print("# 把格式化时间化为结构化时间，它和strftime()是逆操作 ",time.strptime('2013-05-20 13:14:52', '%Y-%m-%d %X'))
# print("time.localtime()",time.localtime(),"time.time()",time.time())
# start = time.time() 
# time.sleep(0.1) 
# end = time.time()
# total_time=end-start
# print(time.strftime("%X",time.localtime(total_time)))
# print(time.strftime("%Y-%m-%d %X",time.gmtime(11111123))) #GMTIME是按标准时间 LOCALTIME是按了北京时间
# now_time=time.time()
# #将秒变为日期
# print("将秒变为日期")
# print(time.strftime("%H:%M:%S", time.gmtime(36000)))
# def mmtohh(mm:int)->str:
# 	days=str(mm//3600//24)
# 	times=str(time.strftime("%H:%M:%S", time.gmtime(mm)))
# 	return days+"天"+times

# print(mmtohh(13600))
# print(time.time())
