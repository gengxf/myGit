# -*- coding: utf-8 -*-
import urllib2
import urllib
import re
import time
import random


iplist = ["1.63.18.22:8080"]
list_word = ['赶集']
for kw in list_word:
    keyword = urllib.quote(kw)
    url = "http://sug.so.360.cn/suggest/word?callback=suggest_so&encodein=utf-8&encodeout=utf-8&word=" + keyword
    ip = random.choice(iplist)
    header = {
        "GET": url,
        "Host": "sug.so.360.cn",
        "Referer": "http://www .so.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36"
    }

    proxy = urllib2.ProxyHandler({'http': 'http://' + ip})
    http_opener = urllib2.build_opener(proxy)
    urllib2.install_opener(http_opener)

    req = urllib2.Request(url)
    for key in header:
        req.add_header(key, header[key])

    html = urllib2.urlopen(req).read()
    print html
    suggestion = re.findall('"(.*?)"', html)
    print "***********************************"
    for item in suggestion:
        print item
    print "***********************************"
time.sleep(random.uniform(1, 2))



