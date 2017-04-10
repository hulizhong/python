#!/usr/bin/env python
# coding=utf-8


class Father(object):
    ##__init__之外定义的变量不能用self；
    #self.attr1 = 'hulz'
    attr1 = 'imattr1'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printObj(self):
        print self.name, " ", self.age

    def callPrint(self):
        self.printObj()

#f = Father('hulz', 29)
#f.callPrint()

class Child(Father):
    def __init__(self, name, age, isstudent):
        super(Child, self).__init__(name, age)
        self.isstudent = isstudent
    
    def printObj(self):
        if self.isstudent:
            print self.name, " ", self.age, " is a student"
        else:
            print self.name, " ", self.age, " not a student"

i = 5
print i.__class__
print type(i)
print int.__class__
print type(int)
f = Father('father', 38)
print f.__class__
print type(f)
print Father.__class__
print type(Father)
#f.printObj()
#print f.attr1
#print f.name
#
#ch = Child('hu', 5, False)
#ch.printObj()
#
