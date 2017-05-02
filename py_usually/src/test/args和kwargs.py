'''
Created on 2016年11月4日

注意区分*args和**kwargs,一个是数组，一个是字典

@author: shengxiz
'''

def test(a,*args,**kwargs):
    print (a)
    print (args)
    print (kwargs)

test(1,2,3,d='4',e=5)