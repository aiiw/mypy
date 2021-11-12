dic={}
n=24
for j in range(2021,2100):
	for k in range(1,13): #左开右闭
			n=n+1
			if len(str(k))==1:
				kk='0'+str(k)
			else:
				kk=str(k)
			key=str(j)+str(kk)
			dic[key]=n


key1='202109'
print(dic[key1])