# -*- coding: utf-8 -*-
import urllib2
import urllib
import re
import time
import random

iplist = ["58.215.52.159:8080"]
file_in = open('/Users/gengxiaofeng/Downloads/word_4000.txt', "r")
file_out = open('/Users/gengxiaofeng/Downloads/output_4000.txt', "w")


def wuba_crawler():
    count = 0
    list_word = []
    for line in file_in.readlines():
        list_word.append(line.strip().split("\t")[0])




    # list_word = ['戴尔中国授权','英语教育培训']
    for kw in list_word:
        count = count + 1
        print count
        keyword = urllib.quote(kw)
        url = "http://www.orthm.com/seg?query=" + keyword
        ip = random.choice(iplist)
        header = {
            "GET": url,
            "Host": "www.orthm.com",
            "Referer": "http://www.baidu.com/",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36"
        }

        proxy = urllib2.ProxyHandler({'http': 'http://' + ip})
        http_opener = urllib2.build_opener(proxy)
        urllib2.install_opener(http_opener)

        req = urllib2.Request(url)
        for key in header:
            req.add_header(key, header[key])
        try:
            html = urllib2.urlopen(req).read()
            html2 = html.replace('"', '')

        except Exception, e:
            print e
        finally:
            query_result = re.search(r'normal:\[(.*?)\],small:\[(.*?)\]', html2)
            if query_result != None:
                file_out.write(kw + '\t' + query_result.group(1) + '\t' + query_result.group(2) + '\n')
        time.sleep(random.uniform(2, 3))


wuba_crawler()




#"k": "管庄"
