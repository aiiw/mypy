# import json
# list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
import os
print("东")
def abcd(**id):
	print(type(id))
	# os.mkdir(r'e:/ab')
def abc(*id):
	print(type(id))
	mid=','.join(["'%s'"%item for item in id])
	print(mid)

class wark():
	"""docstring for wark"""
	path=''
	def __init__(self, path):
		self.path = path
	def speak(self):
		print("path %s"%(self.path))
		if os.path.exists(self.path):
			for root,dir,file in os.walk(self.path):
				for name in dir:
					print(os.path.join(root, name))
				for name in file:
					print(os.path.join(root, name))

abc('1','2','3','d')
abcd()
a=wark(r'd:\\p123')
a.speak()
print("中国人")
