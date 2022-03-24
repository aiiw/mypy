# from functools import wraps
# def super(fn):
# 	@wraps(fn)
# 	def w():
# 		fn()
# 		print("这个是上级节点")
# 		fn()
# 	return w
# @super
# def node1():
# 	print("这个是子节点")

# print(node1.__name__)

# import os
# from pathlib import Path
# p = Path(r"d:\py")
# print(type(p))
# for i in p.iterdir():
#   print(i)

# print(p.parts)  # 分割路径 类似os.path.split(), 不过返回元组

# print(p.drive)  # 返回驱动器名称

# print(p.root)  # 返回路径的根目录

# print(p.anchor)  # 自动判断返回drive或root

# print(p.parents)  # 返回所有上级目录的列表
# print(p.anchor)


import requests

# weatherday Python示例代码
if __name__ == '__main__':
    url = 'http://gwgp-h4bqkmub7dg.n.bdcloudapi.com/day'
    params = {}
    params['cityid'] = ''
    params['city'] = ''
    params['province'] = ''
    params['ip'] = ''
    
    
    headers = {
        
        'Content-Type': 'application/json;charset=UTF-8',
        'X-Bce-Signature': 'AppCode/123'
    }
    r = requests.request("GET", url, params=params, headers=headers)
    print(r.text)
    print(r.content)


    