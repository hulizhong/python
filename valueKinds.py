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

print '##-----------------------------------------------------------##section '
### -----------------------------------------------------------##section 
### 测试传参方式，可变对象
print "测试传参方式，list"
listarg = [1, 2, 3]
def processListarg(arg):
    print '-----before id', id(arg)
    arg.append(4)
    print '-----after id', id(arg)
print 'pre', id(listarg), listarg
#print processListarg(copy.copy(listarg))
print processListarg(listarg)
print 'post', id(listarg), listarg

### 测试传参方式，不可变对象
print "\n测试传参方式，str"
strarg = "1, 2, 3 "
def processStrarg(arg):
    print '-----before id', id(arg)
    arg += "can i change outside-arg ?"
    print '-----after id', id(arg), arg
print 'pre', id(strarg), strarg
print processStrarg(strarg)
print 'post', id(strarg), strarg


### 测试赋值
## 不可变对象
str1 = 'ssss'
str2 = str1
print '\n\n= ', id(str1), id(str2)
# 单看1个赋值有点像写时复制的效果，但其实不是，因为字符串为不可变对象，所以只要有改变就会是一个新对象；
str1 += 'mmm1'
print 'change orig ', id(str1), id(str2)
str2 += 'mmm2'
print 'change refer ', id(str1), id(str2),   str1, str2

## 可变对象
lst1 = [1, 2, [2,2]]
lst2 = lst1
print '\n= ', id(lst1), id(lst2)
lst1.append(31)
print 'change orig ', id(lst1), id(lst2)
lst2.append(32)
print 'change refer ', id(lst1), id(lst2), lst1, lst2

lst3 = copy.copy(lst1)
print id(lst3), id(lst1)
lst4 = copy.deepcopy(lst1)
print id(lst4), id(lst1)

