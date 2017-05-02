'''
Created on 2017年3月14日

@author: shengxiz
'''
str1 = "abcdefg"
str2 = "0000000this is string example....wow!!!0000000";
print(str1.ljust(20,"#"))
print(str1.center(20,"$"))
print(str1.split("b"))
print("-".join(str1))
print(str2.strip('0'))

a=["a","b","c"]
b = [1,2,3]
a.extend(b)
print(a)


