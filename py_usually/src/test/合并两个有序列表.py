'''
Created on 2016年11月4日

合并两个有序列表，采用递归的方法

@author: shengxiz
'''
def Merge_sorted_list(L1,L2,tmp):
    if len(L1)==0 or len(L2)==0:
        tmp.extend(L1)
        tmp.extend(L2)
        return tmp
    else:
        if L1[0]<L2[0]:
            tmp.append(L1[0])
            del L1[0]
        else:
            tmp.append(L1[0])
            del L2[0]
        return Merge_sorted_list(L1, L2, tmp)

print(Merge_sorted_list([1,3,5,7], [3,5,7,8,10], []))