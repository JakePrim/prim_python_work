#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("包含中文的str")

print(ord('A'));

print(ord("中"))

print(chr(66))

print(chr(25991))

print('\u4e2d\u6587')



# 将str 转换为 byte 用于网络传输 和 保存到磁盘
print(b'abc')

print('ABC'.encode('ascii'))

print('中文'.encode('utf-8'))

# 从网络或磁盘上读取字节流

print(b'ABC'.decode('ascii'))

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 如果bytes中包含无法解码的字节，decode()方法会报错
# print(b'\xe4\xb8\xad\xff'.decode('utf-8'))

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore'))

# 要计算str包含多少个字符，可以用len()函数
print(len('ABC'))

print(len('中文'))

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数

print(len(b'abc'))

print(len(b'\xe4\xb8\xad\xe6\x96\x87'))

print(len('中文'.encode('utf-8')))

# 1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节

##　格式化字符串 %运算符就是用来格式化字符串的。在字符串内部，
# %s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好

print('hello, %s'%'word')

print('hi,%s,you have $%d'%('prim',1000))

# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数

print('%2d - %02d'%(3,1))

print('%.2f'%3.1415926)

# 不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串

print('Age:%s , Gendder:%s'%(25,True))

# %%来表示一个%

print('grawth: %d %%'%7)

# 另一种格式化字符串的方法是使用字符串的format()方法，
# 它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多

print('hello,{0} ,成绩提升{1}%'.format('小明',17.568))

s1 = 72
s2 = 85

r = (s2 - s1) * 100 / s1

print('hello %s , 你的成绩提升了： %.1f %%'%('小明',r))


