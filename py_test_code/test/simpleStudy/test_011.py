'''
Created on 2016年8月16日

@author: shengxiz
'''
##11字典
ab={'kobe':81,
    'T-Mac':60,
    'shengxiz':0}
print("T-Mac's top score is %d"%ab['T-Mac'])
ab['Bell']=100 
del ab['shengxiz']
print('\nthere are %d players in the list\n'%len(ab))
for name,score in ab.items():
    print('%s score is %d'%(name,score))
if 'kobe' in ab:
##if ab.__contains__('kobe'):
    print("\nkobe's score is %d"%ab['kobe'])