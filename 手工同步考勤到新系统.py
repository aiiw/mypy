
import pymssql
#sql服务器名，这里(127.0.0.1)是本地数据库IP
serverName = '192.168.0.181'
#登陆用户名和密码
userName = 'sa'
passWord = '$u2930123WJ'
#建立连接并获取cursor
conn = pymssql.connect(serverName , userName , passWord, "T9IMS")
cursor = conn.cursor()
# try:
# 	print("aa1")
# 	sql="update emp0315 set id=(%s) where id=(%s)"
# 	cursor.executemany(sql,list1)
# 	conn.commit()
# 	print("aa2")
# except:
# 	print("aiiw")
# 	conn.rollback()



sql = '''
insert into T_HR_PunchRecord(time,EmpID,CardNumber,MachineNumber,DevicePurposeID,AppStatus)
select  wdate+' ' +wtime ,e.id,e.fpcode,a.address,2,0
from oldHR.KQA.dbo.v_kqsj a,T_HR_Employee e where a.Cardnum=e.code

and  not exists(select 1 from T_HR_PunchRecord where  wdate+' ' +wtime=Time and e.id=EmpID;
 commit  )
'''
cur=conn.cursor()
try:
	cur.execute(sql)
except ValueError:
	conn.rollback()
	print("fail")
cur.close()

conn.close()



















# # 快速写
# import xlwings as xw
# app=xw.App(visible=False,add_book=False)
# list4=[]
# book=app.books.add()
# sheet=book.sheets['sheet1']
# sheet.range('a1').value=list4
# book.save('excel02\\77.xlsx')
# book.close()
# app.quit()
		
# print(sheet.cell(0,0).value) #获取到指定单元格的内容
# print(sheet.cell(0,1).value) #获取到指定单元格的内容

# print(sheet.row_values(0))  #获取到整行的内容
# print(sheet.col_values(0))   #获取到整列的内容

# for i in range(sheet.nrows):  #循环获取每行的内容
#     print(sheet.row_values(i))