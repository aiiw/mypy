
import sys,locale

sys.path.append("..")
print(sys.getdefaultencoding())
print(locale.getdefaultlocale())
import pymssql
#sql服务器名，这里(127.0.0.1)是本地数据库IP
serverName = '192.168.0.180'
#登陆用户名和密码
userName = 'sa'
passWord = '$u2930123WJ'
#建立连接并获取cursor
conn = pymssql.connect(serverName , userName , passWord, "KQA")
cursor = conn.cursor()
value=('16','11608','2021-07-06 00:00:00.000','07:52:11')
sql= f'INSERT into WorkCardSource VALUES {value}'
# 查询记录
cursor.execute(sql)

# 获取一条记录
# row = cursor.fetchone()
# # 循环打印记录(这里只有一条，所以只打印出一条)
# while row:
# 	# a=row[0].encode('utf-8')
# 	# b=row[8].encode('gbk').decode('utf-8')
	
# 	row = cursor.fetchone()
# # 连接用完后记得关闭以释放资源
conn.commit()
conn.close()
