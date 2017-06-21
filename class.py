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

class InitTest(object):
    def __init__(self):
        try:
            self.stateok = False
            self.attr1 = 'hulz'
            fd = open("/home/hulz/noexistfile", "rb")

            self.stateok = True
            print '++'
            #return True  ---> TypeError: __init__() should return None, not 'bool'
        except Exception, e:
            print '++ failed. ', e

    def __del__(self):
        try:
            if self.stateok == False:
                raise AssertionError("connect no ok")
            print '--'
        except Exception, e:
            print '-- failed. ', e

    def tstFun(self):
        try:
            rows = []
            raise AssertionError("raise test")
        except Exception, e:
            print 'tstFun failed. ', e
            #raise e
        else:
            print 'tstFun ok....'
            return rows

itest = InitTest()
res = itest.tstFun()
if res == None:
    print 'None case: ', type(res)
else:
    print 'else case: ', type(res)
#if itest == None:
#    print 'itest is None'
#else:
#    print type(itest)
#    print 'itest is ok'


class MultiInitClass(object):
    '''
    '''
    def __init__(self, des):
        print 'args with ', des

    def __init__(self):
        print 'no args'

#multiInit = MultiInitClass()
#multiInit2 = MultiInitClass('ddddd')


class ClassFeature(object):
    """
    test class feature.
    """
    def _privateFun(self):
        print "my name is _privateFun, but i'm public"

    def __privateFun(self):
        print "my name is __privateFun"


cfObj = ClassFeature()
cfObj._privateFun()
#cfObj.__privateFun()

