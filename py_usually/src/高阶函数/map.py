'''
Created on 2016年11月2日

python3 map()的返回值为迭代器，不是列表了。

@author: shengxiz
'''
# def f(x):
#     return x*x
# 
# print(list(map(f,[1,2,3])))


def format_name(s):
    return s[0].upper()+ s[1:].lower()   #第一种方法
#     return s.capitalize()               #第二种方法
print(list(map(format_name,['adam','LISA','barT'])))

#第三种方法
# print(list(map(lambda s:s.capitalize(),['adam','LISA','barT'])))  