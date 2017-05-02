'''
Created on 2016年8月16日

@author: shengxiz
'''
#7 DocString#
def printMax(x,y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    if x>y:
        print(x,'is maximum')
    else:
        print(y,'is maximum')
printMax(3,5)
print (printMax.__doc__)