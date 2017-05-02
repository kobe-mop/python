'''
Created on 2016年8月10日

#3 局部变量#

@author: shengxiz
'''

def func(x):
    print('x is: ',x)
    x=2
    print('Change Local x to',x)
x=50
func(x)
print('x is still',x)