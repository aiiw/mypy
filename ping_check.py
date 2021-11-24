import connector
import os
import xlwings as xw
from datetime import datetime,date
#################################
app = xw.App(visible=False, add_book=False)#其中参数visible（表示处理过程是否可视，也就是处理Excel的过程会不会显示出来），
                                           # add_book（是否打开新的Excel程序，也就是是不是打开一个新的excel窗口）
book = app.books.add()
filename=str(date.today())
sheet = book.sheets['sheet1'] #这个地方好像固定是这样写的?
##################################
os.system('color 12')
from pymysql.cursors import DictCursor
import pymysql

mydb = connector.connect(
    host="192.168.0.7",
    user="root",
    passwd="123456",
    database="dj3",
    auth_plugin='mysql_native_password',

)

mycursor = mydb.cursor()
sql="select user_name,byname,LAST_VISIT_IP from auto_user"
mycursor.execute(sql)
rs_all=mycursor.fetchall()
ls=[]
print(datetime.now())
for rs_one in  rs_all:
        ip=rs_one[2]
        print(ip)
        a=os.system("ping %s -n 1 "%ip)
        print(a) #0为成功非0为失败
        if a==0:
            date=datetime.now(), #将内容转为元组
            newTuple=date+rs_one #类似 列表.append
            ls.append(newTuple)  #构建一个列表,每个列表是一个元组,即列表为行,元组为列的内容.
sheet.range('a1').value = ls #这个ls为[(row),(row)]
book.save('ip.xlsx')
book.close()
app.quit()
print(datetime.now())
