'''
Created on 2016年9月2日

@author: shengxiz
'''
import re
def string(url):
    URL_list = ['.html','.php','.asp','.jsp']
    for lst in URL_list:
        k = re.findall(lst,url)
        if len(k)>0:
            print('Good!yes!')


URL = 'http://www.cnblogs.com/fnng/p/3782515.html'
string(URL)