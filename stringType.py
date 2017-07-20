#!/usr/bin/env python
'''
# -*- coding:utf-8 -*-
#coding=utf-8
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import chardet


s_str = "tian"
s_uni = u"tian"
if isinstance(s_str, str):
    print type(s_str).__name__
if isinstance(s_uni, unicode):
    print type(s_uni).__name__

print chardet.detect(s_str)
#print chardet.detect(s_uni)
print chardet.detect(s_uni.encode('utf-8'))

format1 = "string"
format2 = 5
format4 = -5
format3 = 5.5
strFormat = "I'm format string with %-10s %d %d %.2f" % (format1, format2, format4, format3)
print strFormat

## only use in []
#format1.join("Joinstr")
#print format1

format1 += "+str"
print format1
