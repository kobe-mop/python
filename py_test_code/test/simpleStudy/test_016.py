'''
Created on 2016年8月16日

@author: shengxiz
'''
#16 类和对象的变量
class Person:
    '''Represents a person.'''
    population = 0

    def __init__(self,name):
        '''Initializes the person's data.'''
        self.name=name
        print('Initalizing %s'%self.name)
        Person.population+=1

    def __del__(self):
        print('%s say bye.'%self.name)
        Person.population-=1
        if Person.population ==0:
            print('the last one')
        else:
            print('There are still %d people left.'%Person.population)

    def sayHi(self):
        '''Greeting by the Person.'''
        print('Hi,my name is %s'%self.name)

p=Person('shengxiz')
p.sayHi()
print(p.__doc__)
print(p.sayHi.__doc__)
p.__del__()