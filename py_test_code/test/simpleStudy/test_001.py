'''
Created on 2016年8月10日

@author: shengxiz
'''


"""
函数的定义
"""

def sayHello():
    print ('hello world!')
sayHello()


"""
生成器yield 3种表示形式
"""
def gen():
    a = 100
    yield a
    a = a*8
    yield a
    yield 1000

def gen1():
    for i in range(4):
        yield i
        
G = (x for x in range(4))
        
for i in G:
    print (i)
    
def decorator(aClass):
    class newClass:
        def __init__(self, age):
            self.total_display   = 0
            self.wrapped         = aClass(age)
        def display(self):
            self.total_display += 1
            print("total display", self.total_display)
            self.wrapped.display()
    return newClass

@decorator
class Bird:
    def __init__(self, age):
        self.age = age
    def display(self):
        print("My age is",self.age)

eagleLord = Bird(5)
for i in range(3):
    eagleLord.display()