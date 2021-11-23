import time
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


print(datetime.now())

print(date.today())

