'''
Created on 2016年8月10日

#4 全局变量global#

@author: shengxiz
'''

def func():
    global x
    print('x is: ',x)
    x=2
    print('Change Local x to',x)
x=50
func()
print('x is still',x)