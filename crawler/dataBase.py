# -*- coding: utf-8 -*-
import sys

import MySQLdb


# 连接数据库　
try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='xxxx', db='test1')
except Exception, e:
    print e
    sys.exit()

# 获取cursor对象来进行操作

cursor = conn.cursor()
# 创建表
sql = "create table if not exists test1(name varchar(128) primary key, age int(4))"
cursor.execute(sql)
# 插入数据
sql = "insert into test1(name, age) values ('%s', %d)" % ("zhaowei", 23)
try:
    cursor.execute(sql)
except Exception, e:
    print e

sql = "insert into test1(name, age) values ('%s', %d)" % ("张三", 21)
try:
    cursor.execute(sql)
except Exception, e:
    print e
# 插入多条

sql = "insert into test1(name, age) values (%s, %s)"
val = (("李四", 24), ("王五", 25), ("洪六", 26))
try:
    cursor.executemany(sql, val)
except Exception, e:
    print e

# 查询出数据
sql = "select * from test1"
cursor.execute(sql)
alldata = cursor.fetchall()
# 如果有数据返回，就循环输出, alldata是有个二维的列表
if alldata:
    for rec in alldata:
        print rec[0], rec[1]

cursor.close()
