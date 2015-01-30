# -*- coding: utf-8 -*-
#Author = yyobin@gmail.com
#Create = 20120517

import cookielib
import urllib2
import urllib
import os
import sys
import socket
import re


#解析有多少页博客
pageStr = """var PagerInfo = {allCount : '(\d+)',pageSize : '(\d+)',curPage : '\d+'};"""
pageObj = re.compile(pageStr, re.DOTALL)

#获取登陆token
login_tokenStr = '''bdPass.api.params.login_token='(.*?)';'''
login_tokenObj = re.compile(login_tokenStr, re.DOTALL)

#获取博客标题和url
blogStr = r'''<div class="hide q-username"><a href=".*?" class=a-normal target=_blank>.*?</a></div><a href="(.*?)" class="a-incontent a-title" target=_blank>(.*?)</a></div><div class=item-content>'''
blogObj = re.compile(blogStr, re.DOTALL)


class Baidu(object):
    def __init__(self, user='', psw='', blog=''):
        self.user = user  #暂未考虑中文ID
        self.psw = psw
        self.blog = blog

        if not user or not psw or not blog:
            print "Plz enter enter 3 params:user,psw,blog"
            sys.exit(0)

        if not os.path.exists(self.user):
            os.mkdir(self.user)

        self.cookiename = 'baidu%s.coockie' % (self.user)
        self.token = ''

        self.allCount = 0
        self.pageSize = 10
        self.totalpage = 0

        self.logined = False
        self.cj = cookielib.LWPCookieJar()
        try:
            self.cj.revert(self.cookiename)
            self.logined = True
            print "OK"
        except Exception, e:
            print e

        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        self.opener.addheaders = [('User-agent', 'Opera/9.23')]
        urllib2.install_opener(self.opener)

        socket.setdefaulttimeout(30)

    #登陆百度
    def login(self):
        #如果没有获取到cookie，就模拟登陆一下
        if not self.logined:
            print "need logon"
            #第一次访问一下，目的是为了先保存一个cookie下来
            qurl = '''https://passport.baidu.com/v2/api/?getapi&class=login&tpl=mn&tangram=false'''
            r = self.opener.open(qurl)
            self.cj.save(self.cookiename)

            #第二次访问，目的是为了获取token
            qurl = '''https://passport.baidu.com/v2/api/?getapi&class=login&tpl=mn&tangram=false'''
            r = self.opener.open(qurl)
            rsp = r.read()
            self.cj.save(self.cookiename)

            #通过正则表达式获取token
            matched_objs = login_tokenObj.findall(rsp)
            if matched_objs:
                self.token = matched_objs[0]
                print self.token
                #然后用token模拟登陆
                post_data = urllib.urlencode({'username': self.user,
                                              'password': self.psw,
                                              'token': self.token,
                                              'charset': 'UTF-8',
                                              'callback': 'parent.bd12Pass.api.login._postCallback',
                                              'index': '0',
                                              'isPhone': 'false',
                                              'mem_pass': 'on',
                                              'loginType': '1',
                                              'safeflg': '0',
                                              'staticpage': 'https://passport.baidu.com/v2Jump.html',
                                              'tpl': 'mn',
                                              'u': 'http://www.baidu.com/',
                                              'verifycode': '',
                })
                #path = 'http://passport.baidu.com/?login'
                path = 'http://passport.baidu.com/v2/api/?login'
                self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
                self.opener.addheaders = [('User-agent', 'Opera/9.23')]
                urllib2.install_opener(self.opener)
                headers = {
                    "Accept": "image/gif, */*",
                    "Referer": "https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F",
                    "Accept-Language": "zh-cn",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Accept-Encoding": "gzip, deflate",
                    "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
                    "Host": "passport.baidu.com",
                    "Connection": "Keep-Alive",
                    "Cache-Control": "no-cache"
                }
                req = urllib2.Request(path,
                                      post_data,
                                      headers=headers,
                )
                rsp = self.opener.open(req).read()
                #如果觉得有必要的话，在这里自己读一下rsp判断一下是否登陆OK，我打印过登陆没问题
                self.cj.save(self.cookiename)
            else:
                print "Login Fail"
                sys.exit(0)

    #获取博客一共有多少页，如果有私有博客的话，登陆和不登陆获取的是不一样的
    def getTotalPage(self):
        #获取博客的总页数
        req2 = urllib2.Request(self.blog)
        rsp = urllib2.urlopen(req2).read()
        if rsp:
            rsp = rsp.replace('\r', '').replace('\n', '').replace('\t', '')
            matched_objs = pageObj.findall(rsp)
            if matched_objs:
                obj0, obj1 = matched_objs[0]
                self.allCount = int(obj0)
                self.pageSize = int(obj1)
                self.totalpage = (self.allCount / self.pageSize) + 1
                print self.allCount, self.pageSize, self.totalpage

    #获取每一页里的博客链接
    def fetchPage(self, url):
        req = urllib2.Request(url)
        rsp = urllib2.urlopen(req).read()
        if rsp:
            rsp = rsp.replace('\r', '').replace('\n', '').replace('\t', '')
            matched_objs = blogObj.findall(rsp)
            if matched_objs:
                for obj in matched_objs:
                    #这里可以用多线程改写一下,单线程太慢
                    self.download(obj[0], obj[1])

    def downloadBywinget(self, url, title):
        pass  #比如使用wget之类的第三方工具，自己填参数写

    #下载博客
    def download(self, url, title):
        path = '%s/%s.html' % (self.user, title.decode('utf-8'))

        url = 'http://hi.baidu.com%s' % (url)
        print "Download url %s" % (url)

        nFail = 0
        while nFail < 5:
            try:
                sock = urllib.urlopen(url)
                htmlSource = sock.read()
                myfile = file(path, 'w')
                myfile.write(htmlSource)
                myfile.close()
                sock.close()
                return
            except:
                nFail += 1
        print 'download blog fail:%s' % (url)

    def dlownloadall(self):
        for page in range(1, self.totalpage + 1):
            url = "%s?page=%d" % (self.blog, page)
            #这里可以用多线程改写一下,单线程太慢
            self.fetchPage(url)


def main():
    user = 'gxfantasy@163.com'  #你的百度登录名
    psw = 'gxf11111!'  #你的百度登陆密码,不输入用户名和密码，得不到私有的文章
    blog = "http://hi.baidu.com/new/yobin"  #你自己的百度博客链接

    baidu = Baidu(user, psw, blog)
    baidu.login()
    baidu.getTotalPage()
    baidu.dlownloadall()


if __name__ == '__main__':
    main()
	


