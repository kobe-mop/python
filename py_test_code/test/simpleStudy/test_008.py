'''
Created on 2016年8月16日


当我们执行python using_sys.py we are arguments的时候，我们使用python命令运行
using_sys.py模块，后面跟着的内容被作为参数传递给程序。Python为我们把它存储在sys.argv变
量中。

记住，脚本的名称总是sys.argv列表的第一个参数。所以，在这里，'using_sys.py'是sys.argv
[0]、'we'是sys.argv[1]、'are'是sys.argv[2]以及'arguments'是sys.argv[3]。注意，Python从0开始计
数，而非从1开始。

python using_sys.py we are arguments

输出为：
The command line arguments are:
using_sys.py
we
are
arguments

@author: shengxiz
'''
##8模块
import sys
print ('the second line argument are:')
for i in sys.argv:
    print (i)
print ('\n\nThe PYTHONPATH is', sys.path, '\n')






