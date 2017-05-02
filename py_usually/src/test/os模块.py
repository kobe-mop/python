'''
Created on 2016年11月4日

这个函数接受文件夹的名称作为输入参数， 

返回该文件夹中文件的路径， 

以及其子文件夹中文件的路径。

os.listdir(XX/XX)   列出所有文件，返回列表
os.path.join(XX/XX，test.py)  返回文件的完整路径
os.path.isdir() 判断是否为dir


@author: shengxiz
'''
import os
def Print_content(path,tmp):
    for item in os.listdir(path):
        spath = os.path.join(path,item)
        if os.path.isdir(spath):
            Print_content(spath,tmp)
        else:
            tmp.append(spath)
    return tmp
    
print(Print_content(r'D:\VNC',[]))