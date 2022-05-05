import xlwings as xw
app=xw.App(visible=False,add_book=True)
list4=[[(1,),(2),]]
book=app.books.add()
sheet=book.sheets['sheet1']
list=[(1,2,3),(4,5,6)]
list=[[12,33,33],[22,3,32]]
sheet.range('a1').value=list
book.save('77.xlsx')
book.close()
app.quit()

#写表的方式[[],[],[]]  [(),(),()]