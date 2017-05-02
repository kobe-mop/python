'''
Created on 2016年11月3日

编写一个函数calc_prod(lst),它接收一个list。返回一个函数，返回的函数可以计算参数的乘积

@author: shengxiz
'''
from _functools import reduce

def calc_prod(lst):
    print('in calc_prod')
    def in_calc_prod():
        print('in in_calc_prod')
        return prod(lst)
    return in_calc_prod

def prod(lst):
    return reduce((lambda x,y:x*y),lst)

f = calc_prod([1,2,3,4])
print(f())