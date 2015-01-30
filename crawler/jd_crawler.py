# -*- coding: utf-8 -*-
import urllib2

from bs4 import *


url = 'http://list.jd.com/670-671-672.html'
html_doc = urllib2.urlopen(url).read()
soup = BeautifulSoup(html_doc)
div_item = soup.find('div', id='sortlist')
div_li = div_item.find_all('li')
for item in div_li:
    #print item
    item_a = item.find('a')
#print item_a.get('href')

url2 = 'http://list.jd.com/670-671-672.html'
html_doc2 = urllib2.urlopen(url2).read()
soup2 = BeautifulSoup(html_doc2)
div2 = soup2.find('div', id='select')
dl_brand = div2.find('dl', id='select-brand')
div_content = dl_brand.select('[rel]')
for item in div_content:
    print item.get_text().encode('utf-8')

















