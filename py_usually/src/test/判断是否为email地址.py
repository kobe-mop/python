'''
Created on 2016年9月2日

注意！！！！！

re.match是从头开始匹配，找到了返回，没找到返回None

re.search是在整个字符串进行匹配，并不一定是从头开始匹配，没找到返回None




@author: shengxiz
'''
import re
def email(e):
    if len(e)>=5:
        if re.match('[a-zA-Z0-9]+\@+[a-zA-Z0-9]+\.+[a-zA-Z]',e) != None:
            print('Email Found:'+e)
    else:
        print('Email not Correct:'+e)

if __name__ =='__main__':
    m = input('please input a email:')
    email(m)