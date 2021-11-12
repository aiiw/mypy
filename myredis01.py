import redis
client=redis.Redis(host='192.168.0.7')
client.set('a', 'aiiw')