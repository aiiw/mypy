import json

data = {
    'name' : '简',
    'sex' : 'boy',
    'age' : 26
}
print("-----------------原始-----------------------")
print(data,type(data)) 
data1=json.dumps(data)
print("-----------------dumps-----------------------")
print(data1,type(data1))
data2=json.loads(data1)
print("-----------------loads-----------------------")
print(data2,type(data2))
print(type(data))#输出原始数据格式
print(type(data1))#输出经过json.dumps的数据格式
print(type(data2))#输出经过json.loads的数据格式
for index,qq in enumerate(data):
	print(index)