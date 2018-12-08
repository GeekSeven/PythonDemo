#coding=utf-8
from classdemo import Student


#打印
print ('hello world')

#for循环
for i in range(50,60+1):
    print (i)

#一个简单的函数
def add_function(a,b):
    c=a+b
    return c
    
d=add_function(2,3)
print (d)

#for循环 字符串长度
word="hello world"
length=0
for i in word:
    length=length+1
print("字符长度："+str(length))

#if 判断用户

USENAME='zhenghaoran'
PASSWORD='51304170'

print('input your name')
name_account=input()
print ('input your password')
pass_account=input()

if name_account==USENAME and pass_account==PASSWORD:
    print('ture')
else: print ('false')

#elif 用法

a=51304170

if a==1:
    print ('1')
elif a==51304170:
    print ('51304170')

student=Student()
student.printstudent()
