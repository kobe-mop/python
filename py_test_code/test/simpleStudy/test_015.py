'''
Created on 2016年8月16日

@author: shengxiz
'''
#15 类的__init__函数 （初始化）
class Person:
    def __init__(self,name):
        self.name=name
    def sayHi(self):
        print("My name is:",self.name)
p=Person('kobe')
p.sayHi()