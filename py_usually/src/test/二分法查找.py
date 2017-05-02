'''
Created on 2016年11月4日

二分法查找列表中的值，并返回索引值

@author: shengxiz
'''

def Binary_search(lst,val):
    low = 0
    high = len(lst)-1
    while low<=high:
        mid = (low+high)//2
        if lst[mid]<val:
            low = mid+1
        elif lst[mid]>val:
            high = mid-1
        else:
            print('Found {}!'.format(val))
            return mid #返回索引
    print('Not Found!')
    return False

print(Binary_search([1,3,7,34,78], 33))
        
    