import redis
client=redis.Redis(host='192.168.0.7',port='6379')
print(client.get('a'))
str1='aiiw'
# for a in range(1,200):
# 	str1=str1+str(a)
# 	client.set(a, 'a')
# client.set('aa','bb')
print(client.keys())