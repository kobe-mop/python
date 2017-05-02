'''
Created on 2016年8月16日

@author: shengxiz
'''
#17 继承
class SchoolMember:
    '''Represent any school member.'''
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('Initialized SchoolMember:%s'%self.name)
    def tell(self):
        '''Tell my details.'''
        print('Name:"%s" Age:"%s"'%(self.name,self.age))

class Teacher(SchoolMember):
    '''Represent a teacher.'''
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print('Initialized teacher:%s'%self.name)
    def tell(self):
        SchoolMember.tell(self)
        print('Salary:%d'%self.salary)

class Student(SchoolMember):
    '''Represent a student.'''
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print('Initialized student:%s'%self.marks)
    def tell(self):
        SchoolMember.tell(self)
        print('Marks:%d'%self.marks)

t = Teacher('Mr Kobe',40,3000)
s = Student('Shengxiz',24,81)

#打印空行
print() 

member = [t,s]
for Mem in member:
    Mem.tell()