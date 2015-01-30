__author__ = 'gengxiaofeng'
# -*- coding: utf-8 -*-
import urllib2
import urllib
import re
import time
import random


iplist = ["1.63.18.22:8080", "14.17.110.50:8080", "14.18.17.98:80"]

list_word = ['一居室']
for kw in list_word:
    keyword = urllib.quote(kw)
    url = "http://bj.ganji.com/ajax.php?module=suggestion2&domain=bj&keyword=" + keyword
    ip = random.choice(iplist)
    header = {
        "GET": url,
        "Host": "bj.ganji.com",
        "Referer": "http://bj.ganji.com/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36"
    }

    proxy = urllib2.ProxyHandler({'http': 'http://' + ip})
    http_opener = urllib2.build_opener(proxy)
    urllib2.install_opener(http_opener)

    req = urllib2.Request(url)
    for key in header:
        req.add_header(key, header[key])

    html = urllib2.urlopen(req).read()
    suggestion = re.findall(r'"text":"(.*?)"', html)
    for item in suggestion:
        print item
    print "***********************************"
    print html

time.sleep(random.uniform(1, 2))


#"k": "管庄"
