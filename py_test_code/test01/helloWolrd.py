'''
Created on 2017年4月6日

@author: shengxiz
'''

#!/usr/bin/env python
# coding: utf-8
def guessAge():
    a= int(input("please input your age:"))
    age = 49
    if a>age:
        print("bigger!")
        b=1
    elif a<age:
        print("smaller!")
        b=-1
    else:
        b=0
        print("bingo!")
    return b

cout =5
while(cout):
    result = guessAge()
    if result==0:
        break
    cout=cout-1
print("bad luck!")