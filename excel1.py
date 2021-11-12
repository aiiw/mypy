import xlwings as xw
import cx_Oracle 
connection = cx_Oracle.Connection("dsdata/dsdata@T100")
cr=connection.cursor()
sql='''select  y.imaal003
  from tama t
  left join imaa_t x
    on t.imaa001 = x.imaa035
   and x.imaaent = '100'
   and x.imaastus = 'Y'
   And x.imaa010 = 2
  left join imaal_t y
    on y.imaal001 = x.imaa001 and y.imaalent = '100'
   and y.imaal002 = :ab 
'''
cr.execute(sql,ab='zh_CN')
rs=cr.fetchall();
import re
p=re.compile(r'[\u4e00-\u9fa5]')
ls=[]
list=[]
tups=()
newtuple=()
n=0
for row in rs:
 if row[0] is not None:#要求要查询的值不为空
    t = p.findall( str( row ))
    s = ''
    for t1 in t:
      s = s + '%' + t1 + '%'
      #print(s)
    sql1 = '''select y.imaal001,y.imaal003,y.imaal004 from imaa_t x left join imaal_t y on y.imaal001 = x.imaa001 and y.imaalent = '100'
                              where y.imaal003 like :bc'''
    
    cr.execute( sql1, bc=s )
    tups=(s,)
    rs1 = cr.fetchall()
    for tp in rs1:
         newtuple=tp+tups
         n=n+1
         ls.append(newtuple)
app=xw.App(visible=False,add_book=False)
book=app.books.add()
sheet=book.sheets['sheet1']
sheet.range('a1').value=ls
book.save('77.xlsx')
book.close()
app.quit()
