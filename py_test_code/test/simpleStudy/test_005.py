'''
Created on 2016年8月10日

@author: shengxiz
'''


#5 默认参数#
def say(message,times=1):
    print(message*times)
say('hello')
say('world',5)


#输出不换行
for i in range(5):
    print(i,end="")