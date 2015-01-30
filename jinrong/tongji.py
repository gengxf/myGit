# -*- coding: utf-8 -*-
import time
import datetime
import mysql.connector

# print time_struct
# print time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
# print time.mktime(time.localtime())

# m = time.mktime(time.localtime()) - 518400
# print time.localtime(m)

config = {
    'user': '',
    'password': '',
    'host': '',
    'port': '',
    'database': '',
    'raise_on_warnings': True,
}

SAME_YESTERDAY = 604800
YESTERDAY = 86400


def getNowDate():
    nowdate = time.mktime(time.localtime())
    return nowdate


def getBeginDate(mtime):
    stime = time.localtime(mtime)
    qtime = int(time.mktime(time.strptime(str(stime.tm_year) + '-' +
                                          str(stime.tm_mon) + '-' + str(stime.tm_mday) + ' 0:00:01', '%Y-%m-%d %H:%M:%S')))
    return str(qtime)


def getSql():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    yesterday = getNowDate() - YESTERDAY
    same_yesterday = getNowDate() - SAME_YESTERDAY

    sql_today = 'select source,count(distinct mobile) from case_apply where apply_time >= ' + \
        '\'' + getBeginDate(getNowDate()) + '\'' + 'and apply_time<= ' + \
        '\'' + str(getNowDate()) + '\'' + ' group by source;'

    sql_yesterday = 'select source,count(distinct mobile) from case_apply where apply_time >= ' + \
        '\'' + getBeginDate(yesterday) + '\'' + 'and apply_time<= ' + \
        '\'' + str(yesterday) + '\'' + ' group by source;'

    sql_same_yesterday = 'select source,count(distinct mobile) from case_apply where apply_time >= ' + \
        '\'' + getBeginDate(same_yesterday) + '\'' + 'and apply_time<= ' + \
        '\'' + str(same_yesterday) + '\'' + ' group by source;'

    now_count = 0
    yesterday_count = 0
    same_yesterday_count = 0
    cursor.execute(sql_today)

    print '今日金融申请数据:'
    for item in cursor:
        print item[0], item[1]
        now_count = now_count + item[1]
    print '申请总量: ', now_count
    print '-----------------------'
    cursor.execute(sql_yesterday)
    print '昨日金融同一时间申请数据:'
    for item in cursor:
        print item[0], item[1]
        yesterday_count = yesterday_count + item[1]
    print '昨日申请总量: ', yesterday_count
    print '-----------------------'
    cursor.execute(sql_same_yesterday)
    print '上周金融同时刻申请数据:'
    for item in cursor:
        print item[0], item[1]
        same_yesterday_count = same_yesterday_count + item[1]
    print '上周同时刻申请总量: ', same_yesterday_count


def test():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    

if __name__ == '__main__':
    print 'The programme is begging......'
    print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    # getSql()
