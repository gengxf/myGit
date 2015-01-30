# -*- coding: utf-8 -*-
import urllib2
import urllib
import httplib
import json


class BaiduMap:
    def __init__(self, key='VdpUi7HXMoHqWQ4fu72KmWsP'):
        self.host = 'http://api.map.baidu.com'
        self.path = '/geocoder?'
        self.param = {'address': None, 'output': 'json', 'key': key, 'location': None, 'city': None}

    def getLocation(self, address, city=None):
        rlt = self.geocoding('address', address, city)
        if rlt != None:
            l = rlt['result']
            if isinstance(l, list):
                return None
            return l['location']['lat'], l['location']['lng']

    def getAddress(self, lat, lng):
        rlt = self.geocoding('location', "{0},{1}".format(lat, lng))
        if rlt != None:
            l = rlt['result']
            return l['formatted_address'].encode('utf8')
        #Here you can get more details about the location with 'addressComponent' key
        #ld=rlt['result']['addressComponent']
        #print(ld['city']+';'+ld['street'])


    def getaddressComponents(self, lat, lng):
        rlt = self.geocoding('location', "{0},{1}".format(lat, lng))
        return rlt


    # url:http://api.map.baidu.com/geocoder?output=json&location=30.631495%2C104.073265&key=VdpUi7HXMoHqWQ4fu72KmWsP
    def geocoding(self, key, value, city=None):
        if key == 'location':
            if 'city' in self.param:
                del self.param['city']
            if 'address' in self.param:
                del self.param['address']

        elif key == 'address':
            if 'location' in self.param:
                del self.param['location']
            if city == None and 'city' in self.param:
                del self.param['city']
            else:
                self.param['city'] = city
        self.param[key] = value
        html = self.host + self.path + urllib.urlencode(self.param)
        r = urllib2.urlopen(html)
        rlt = json.loads(r.read())
        if rlt['status'] == 'OK':
            return rlt
        else:
            print "Decoding Failed"
            return None


if __name__ == '__main__':
    bm = BaiduMap()
    print bm.getLocation("江边城外•巫山烤全鱼亚运村店", '北京')
    print bm.getLocation("人民南路", '成都')
    print bm.getAddress(40.005253, 116.412558)
    temp = bm.getaddressComponents(30.631495, 104.073265)
    print temp['status']
    print temp['result']