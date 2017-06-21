#!/usr/bin/env python
# coding=utf-8

##-------------------------------------------bisect test
#import bisect
#
#data = [5, 3, 1, 7]
#print data
#data.sort()
#print data
#
##在L中查找x，x存在时返回x左侧的位置，x不存在返回应该插入的位置
#print 'insert 1->pos', bisect.bisect_left(data, 1)
#print 'insert 0->pos',bisect.bisect_left(data, 0)
#print 'insert 9->pos',bisect.bisect_left(data, 9)
#print 'insert 9<-pos',bisect.bisect_right(data, 1)
#print data
## -----------------------------------------------------------------

##-------------------------------------------test struct
# http://blog.csdn.net/stonesharp/article/details/32685159

#import struct
#str = struct.pack("ii", 20, 400)
#print str
#print struct.calcsize("i")
#a1, a2 = struct.unpack("ii", str)
#print 'a1:', a1
#print 'a2:', a2
## -----------------------------------------------------------------

##-------------------------------------------test md5
from hashlib import md5
import struct
#str=""
#print md5(str)  #这样算出的md5是个什么类型的值呢？？？ 怎么打出来怪怪的。 --应该是一个无符号整数加个nul符号
for str in ("1", "2", "3", "4", "100", "1000"):
    vv = md5(str).digest()
    print vv[0], vv[1]
    print md5(str).hexdigest().upper() 

    k = md5(str).digest()
    ha = struct.unpack_from(">I", k)[0] #用大端的无符号整数来unpack md5值。
    print k
    print ha
## -----------------------------------------------------------------

