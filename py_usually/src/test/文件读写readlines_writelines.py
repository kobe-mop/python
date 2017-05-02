'''
Created on 2016年11月4日


read() 每次读取整个文件，它通常用于将文件内容放到一个字符串变量中。

readlines() 自动将文件内容分析成一个字符串的列表，该列表可以由 Python 的 for ... in ... 结构进行处理。

readline() 每次只读取一行，通常比 readlines() 慢得多
仅当没有足够内存可以一次读取整个文件时，才应该使用 readline()

@author: shengxiz
'''
# f = open('score.txt')
# data = f.read()
# f.close()
# print(data)

f = open('score.txt')
lines = f.readlines()
f.close()

results = []
for line in lines:
    data = line.split()
    print(data)
    sum_score = 0
    for i in data[1:]:
        sum_score+=int(i)
    result = '{0}, \t:{1}, \n'.format(data[0],sum_score)
    results.append(result)
    
print(results)
    
f = open('result.txt','w')
f.writelines(results)
f.close()
    
    