import time


def sum(a, b):
    print a + b


def callBack(c, sum):
    sum(5, c)


callBack(3, sum)