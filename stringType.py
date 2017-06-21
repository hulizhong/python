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

