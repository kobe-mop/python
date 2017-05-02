'''
Created on 2016年11月2日

@author: shengxiz
'''
import math
def add(a,b,f):
    return f(a)+f(b)

print(add(9,25,math.sqrt))