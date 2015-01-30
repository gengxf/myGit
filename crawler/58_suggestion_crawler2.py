# -*- coding: utf-8 -*-
import urllib2
import urllib
import re
import random

iplist = ["58.23.15.20:8080"]
# file_in = open('C:\\Users\\gengxiaofeng\\Desktop\\word.txt',"r")
# file_out = open('C:\\Users\\gengxiaofeng\\Desktop\\output.txt',"w")

def wuba_crawler():
    # list_word = []
    # for line in file_in.readlines():
    #     list_word.append(line.split("\t")[0])




    list_word = ['iphone', '英语']
    for kw in list_word:
        # file_out.write(kw+'@@@'+'\n')
        keyword = urllib.quote(kw)
        url = "http://suggest.58.com.cn/searchsuggest_14.do?inputbox=" + keyword + '&cityid=1&catid=0&callback=callback' + str(
            random.randint(11, 777))
        ip = random.choice(iplist)
        header = {
            "GET": url,
            "Host": "suggest.58.com.cn",
            "Referer": "http://bj.58.com/",
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
            # print html
        except Exception, e:
            print e
        finally:

            suggestion = re.search(r'"des":\s"(.*?)"', html)
            suggestion2 = re.search(r'"desk":\s"(.*?)"', html)
            if suggestion != None:
                print suggestion.group(1)
            elif suggestion2 != None:
                print suggestion2.group(1)


            # for item in suggestion:
            #     print item
            #     file_out.write(item+"\n")
            # file_out.write("*****************************************"+"\n")
            print "success"
            print "***********************************"
            # print html
            # time.sleep(random.uniform(1, 2))


wuba_crawler()




#"k": "管庄"
