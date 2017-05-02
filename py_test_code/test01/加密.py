'''
Created on 2017年4月6日

@author: shengxiz
'''
cipher_text = "hHsdai hyGas? jk!jdk!"

def decipher(cipher):
    plan_text = ''
    txt = cipher.split(' ')
    for i in txt:
        t = change(i)
        plan_text = plan_text + ' ' + t[::-1]
    return plan_text

def change(lst):
    num = len(lst)
    a=''
    while(num):
        if ord(lst[num-1])>=97 and ord(lst[num-1])<=122:
            if ord(lst[num-1])>=110:
                a=a+(chr(ord(lst[num-1])-13))
            else:
                a=a+(chr(ord(lst[num-1])+13))  
        elif ord(lst[num-1])>=65 and ord(lst[num-1])<=90:
            if ord(lst[num-1])>=78:
                a=a+(chr(ord(lst[num-1])-13))
            else:
                a=a+(chr(ord(lst[num-1])+13))  
        else:
            a=a+lst[num-1]
        num =num-1
    return a

print(decipher(cipher_text))
            
            
    