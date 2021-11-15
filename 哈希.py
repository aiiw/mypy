import hashlib
sha1 = hashlib.sha1()
sha1.update('1236473411'.encode('utf-8'))
sha1.update('1618967351'.encode('utf-8'))
sha1.update('alidongxing'.encode('utf-8'))
hashcode = sha1.hexdigest() #获取加密串
print (hashcode)
#
#
# # md5加密
def md5sum(str):
    name=r'''<host prod="T100" ver="1.0" ip="10.40.40.18" id="t10tst" timestamp="20160414190605947" acct=""/><service prod="MES" name="create_mo" srvver="1.0"/>'''
    m = hashlib.md5()  # 创建一个hashlib.md5()对象
    m.update(name.encode(encoding='utf-8') ) # 将参数转换为UTF8编码
    print(m.hexdigest())  # 用十六进制输出加密后的数据



from hashlib import md5


def encrypt_md5(s):
    # 创建md5对象
    new_md5 = md5()
    # 这里必须用encode()函数对字符串进行编码，不然会报 TypeError: Unicode-objects must be encoded before hashing
    new_md5.update(s.encode(encoding='utf-8'))
    # 加密
    return new_md5.hexdigest()


# 调用
if __name__ == '__main__':
    name = r'''<host prod="T100" ver="1.0" ip="10.40.40.18" id="t10tst" timestamp="20160414190605947" acct=""/><service prod="MES" name="create_mo" srvver="1.0"/>'''
    print(encrypt_md5(name))