'''
Created on 2016年8月19日

@author: shengxiz
'''
#!/usr/bin/python
#Filename: cat.py

import sys
def readfile(filename):
    '''Print a file to the standard output.'''
    f=open(filename, mode='r')
    while True:
        line=f.readline()
        if len(line)==0:
            break
        print (line,)
    f.close()
    
    
#Script strats from here
if len(sys.argv)<2:
    print('No action specified')
    sys.exit()

if sys.argv[1].startswith('--'):
    option=sys.argv[1][2:]
    if option == 'version':
        print('Version1.2')
    elif option == 'help':
        print('''
        This progranm prints files to standard output.
        Any number of files can be specified.
        Option include:
         --version: Print the version number
         --help   : Display this help''')
    else:
        print('Unkonwn option')
    sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)
    