__author__ = 'gengxiaofeng'
# -*- coding: utf-8 -*-
import cookielib
import urllib2
import urllib
import re
import time
import random

iplist = ["14.18.16.66:80", "14.18.16.68:80"]
file_in = open('/Users/gengxiaofeng/Downloads/query_2000.txt', "r")
file_out = open('/Users/gengxiaofeng/Downloads/58_w2_2000.txt', "w")


def wuba_site_crawler(file_in, file_out):
    list_word = []
    for line in file_in.readlines():
        list_word.append(line.split("\t")[0])

    count = 0
    #list_word = ['一居室']
    for kw in list_word:
        #file_out.write(kw+'@@@'+'\n')
        keyword = urllib.quote(kw)
        url = "http://bj.58.com/house/?key=" + keyword
        ip = random.choice(iplist)
        header = {
            "GET": url,
            "Host": "bj.58.com",
            #"Referer": "http://bj.58.com/",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36"
        }

        proxy = urllib2.ProxyHandler({'http': 'http://' + ip})
        cj = cookielib.CookieJar();
        http_opener = urllib2.build_opener(proxy, urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(http_opener)

        req = urllib2.Request(url)
        for key in header:
            req.add_header(key, header[key])
        try:
            html = urllib2.urlopen(req).read()
            query_result = re.search(r"highlight\.init\(\$\(\"#infolist a\.t\"\), '(.*)'\)", html)
            # print query_result.group(1)
            if query_result != None:
                file_out.write(kw + "\t" + query_result.group(1) + "\n")
                count = count + 1
                print count
            else:
                print kw
        except Exception, kw:
            print kw
        #finally:


        time.sleep(random.uniform(1, 2))


wuba_site_crawler(file_in, file_out)



