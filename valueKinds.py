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
