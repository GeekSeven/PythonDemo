#coding=utf-8

#打印
print ('hello world');

#for循环
for i in range(50,60+1):
    print (i);

#一个简单的函数
def add_function(a,b):
    c=a+b
    return c;
    
d=add_function(2,3)
print (d);

#for循环 字符串长度
word="hello world"
length=0
for i in word:
    length=length+1
print("字符长度："+str(length))

