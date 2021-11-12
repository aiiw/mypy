from  oswalk import walk
import os
a=input("请输入要遍历的目录")
b=input("请输入要输出的文件名(固定目录放在：d://py)")
if not os.path.exists("d://py"):
	os.mkdir('d://py')
ins=walk(a)
str=ins.speak()
path=os.path.join(r'd:\\py',b)
print(path)

with open (path,'a+') as f:
	f.writelines(str)
print("-完成-")
c=input()


