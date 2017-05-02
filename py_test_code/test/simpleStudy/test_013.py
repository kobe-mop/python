'''
Created on 2016年8月16日

@author: shengxiz
'''
#13 编写一个备份的脚本 
import os
import time
source_dir = r'home/shengxiz/test'
target_dir = r'home/shengxiz'
target_name = target_dir + time.strftime('%Y%m%d%H%M%S')+'.zip'
zip_command = "zip -qr '%s' %s"%(target_name,''.join(source_dir))
print(zip_command)
if os.system(zip_command)==0:
    print('Succeful backup to',target_name)
else:
    print('Backup Failed')