# -*- coding: utf-8 -*-
import urllib2
import re


url = 'http://bj.58.com/sou/?key=%E7%9B%B4%E7%A7%9F%20%E6%B5%B7%E6%B7%80'
html = urllib2.urlopen(url).read()
title = re.findall(r'<a\sclass="t".*title="(.*)"', html)
for item in title:
    print item