list=[]
data = {
    '中国':'北京',
    '韩国':'首尔',
    '日本':'东京',
    '泰国':'曼谷',
    '马来西亚':'吉隆坡',
    '越南':'河内',
    '朝鲜':'平壤',
    '印度':'新德里'
    }
for item in data:
    list.append([item,data.get("%s"%(item)),"aaa"])
print(list)
list1=[]
for key,value in data.items():  
    list1.append([key,value,"aaa"])
print(list1)
