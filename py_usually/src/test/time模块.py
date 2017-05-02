'''
Created on 2016年11月4日

@author: shengxiz
'''
import time
print(time.ctime())
time.sleep(1)
print(time.ctime())#把时间戳转化为标准时间，无参数使用默认使用time.time()
print(time.time())   #返回时间戳
print(time.localtime())      #把时间戳转化为struct_time,无参数默认使用使用time.time()
print(time.strftime("%Y-%m-%d %H:%M:%S"))#把时间戳转化为自己设定的格式，无参数默认使用time.time()