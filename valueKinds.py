#!/usr/bin/env python
# coding=utf-8
import copy


dic1 = {1 : "hulz", 2 : "hulh"}
dic2 = copy.copy(dic1)
dic3 = copy.deepcopy(dic1)
print dic1
print dic2
print dic3
print '------------------------'

dic1[2] = "hulz"
print dic1
print dic2
print dic3

################################
t2 = (3)
print t2
t3 = (3,)
print t3


num = 5
while num > 0:
    print num
    num = num - 1

##-----------------------------------------------------------##section 
### 测试传参方式，list
print "测试传参方式，list"
listarg = [1, 2, 3]
def processListarg(arg):
    #arg.append("can i change outside-arg ?")
    arg = ["sadf", "asdfsdf"]
    return arg
## 默认是走的引用，亦即python中的=
#print listarg
#print processListarg(listarg)
#print listarg
## 让它走下浅拷贝呢。。。
print listarg
print processListarg(copy.copy(listarg))
print listarg

### 测试传参方式，str
print "测试传参方式，str"
strarg = "1, 2, 3 "
def processStrarg(arg):
    print '-----before', id(arg)
    arg = "can i change outside-arg ?"
    print '-----after', id(arg)
    return arg
## 亦即python中的=，这可没走引用啊？？？？ 什么意思？？ ---还是走了引用，只不过是不可变对象，进行了新对象的构造。 
print strarg
print id(strarg)
print processStrarg(strarg)
print strarg



