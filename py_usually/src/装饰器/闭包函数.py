'''
Created on 2016年11月3日

返回的闭包不能引用循环变量，能正确返回能计算1*1 ，2*2,3*3

@author: shengxiz
'''

def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
 
f1,f2,f3 = count()
print(f1(),f2(),f3())


# def count():
#     fs=[]
#     for i in range(1,4):
#         def f(j):
#             def g():
#                 return j*j
#             return g
#         fs.append(f(i))
#     return fs
# 
# f1,f2,f3 = count()
# print(f1(),f2(),f3())