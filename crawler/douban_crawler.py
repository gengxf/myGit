# -*- coding: utf-8 -*-
import urllib2
import re

import BeautifulSoup


#get the content of html 
content = urllib2.urlopen('http://www.douban.com/group/machome/').read()


#def : extract_url
reg = 'http://www.douban.com/group/topic/\d{8}/'
re_url = re.findall(reg, content)
print re_url


#处理HTML
re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I)  #匹配CDATA
re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)  #Script
re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)  #style
re_p = re.compile('<P\s*?/?>')  #处理换行
re_h = re.compile('</?\w+[^>]*>')  #HTML标签
re_comment = re.compile('<!--[^>]*-->')  #HTML注释
s = re_cdata.sub('', content)  #去掉CDATA
s = re_script.sub('', s)  #去掉SCRIPT
s = re_style.sub('', s)  #去掉style
s = re_p.sub('\r\n', s)  #将<p>转换为换行
s = re_h.sub('', s)  #去掉HTML 标签
s = re_comment.sub('', s)  #去掉HTML注释
blank_line = re.compile('\n+')  #去掉多余的空行
s = blank_line.sub('\n', s)
print s
   

