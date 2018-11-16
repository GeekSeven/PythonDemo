# 跨同级文件夹访问

import sys
import os

o_path=os.getcwd()
sys.path.append(o_path)

from second.second01 import a
print (a)

#获取系统时间 
#获取日期差
import time
import datetime
def Getnowtime():
    #return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    return time.strftime("%Y%m%d",time.localtime(time.time()))
systime=str.format(Getnowtime())
print(systime)

a=datetime.datetime.strptime(Getnowtime(),'%Y%m%d')
print (type(a))
b=datetime.datetime.strptime('2018728','%Y%m%d')

days=(a-b).days
print (days)

