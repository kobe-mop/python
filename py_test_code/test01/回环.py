'''
Created on 2017年4月6日

判断list中的字符串是否是回环字符串

@author: shengxiz
'''

lst =['RAdar','Lemon','aka','Do geese see God']

def is_palindrome(letters):
    #str=letters.replace(' ','')
    str =''.join(letters.split(' '))
    str1 = str.lower()
    str2 = str1[::-1]
    if str1 == str2:
        print(letters)
    else:
        pass
        
if __name__ =="__main__":
    for i in lst:
        is_palindrome(i)