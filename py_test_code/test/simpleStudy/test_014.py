'''
Created on 2016年8月16日

@author: shengxiz
'''
#14 使用类的方法，和函数类似，多了一个self
class Person:
    def sayHi(self):
        print("Hello,World!")
p=Person()
p.sayHi()