# import threading
# import time

# def run(n):
#     print("task", n)
#     time.sleep(1)
#     print('2s')
#     time.sleep(1)
#     print('1s')
#     time.sleep(1)
#     print('0s')
#     time.sleep(1)

# if __name__ == '__main__':
#     t1 = threading.Thread(target=run, args=("t1",))
#     t2 = threading.Thread(target=run, args=("t2",))
#     t1.start()
#     t2.start()

class A:
     def __init__(self):
       
       print('value')
     def add(self, x):
         y = x+1
         print(y)
class B(A):
    # def __init__(self,x):
    #     super().__init__()
    pass
b = B()
b.add(1)



class A:
  def __init__(self):
    print("Enter A")
    print("Leave A")
class B(A):
  def __init__(self):
    print("Enter B")
    super(B, self).__init__()
    print("Leave B")
class C(A):
  def __init__(self):
    print("Enter C")
    super(C, self).__init__()
    print("Leave C")
class D(A):
  def __init__(self):
    print("Enter D")
    super(D, self).__init__()
    print("Leave D")
class E(B, C, D):
  def __init__(self):
    print("Enter E")
    super(E, self).__init__()
    print("Leave E")
E()

# from threading import Thread
# import time

# class MyThread(Thread):
#     def __init__(self, n):
#         super(MyThread, self).__init__()  # 重构run函数必须要写
#         self.n = n

#     def run(self):
#         print("task", self.n)
#         time.sleep(1)
#         print('2s')
#         time.sleep(1)
#         print('1s')
#         time.sleep(1)
#         print('0s')
#         time.sleep(1)

# if __name__ == "__main__":
#     t1 = MyThread("t1")
#     t2 = MyThread("t2")
#     t1.start()
#     t2.start()
#     