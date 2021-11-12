import hashlib
sha1 = hashlib.sha1()
sha1.update('1236473411'.encode('utf-8'))
sha1.update('1618967351'.encode('utf-8'))
sha1.update('alidongxing'.encode('utf-8'))

hashcode = sha1.hexdigest() #获取加密串
print (hashcode)