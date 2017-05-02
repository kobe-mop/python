'''
Created on 2017年3月2日

@author: shengxiz
'''
# 闭包
def line_conf(a,b):
    def line(x):
        return a*x+b
    return line       # return a function object

lines = line_conf(3, 4)
print(lines(5))

########################
# 装饰器
def decorator(F):
    def new_F(a, b):
        print("input", a, b)
        return F(a, b)
    return new_F

# get square sum
@decorator
def square_sum(a, b):
    return a**2 + b**2

# get square diff
@decorator
def square_diff(a, b):
    return a**2 - b**2

print(square_sum(3, 4))
print(square_diff(3, 4))
print("%+10x" % 10)
print("%04d" % 5)
print("%6.3f" % 2.3)
print("%.*f" % (4, 1.2))