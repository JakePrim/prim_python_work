#!/usr/bin/env python3
# -*- coding: utf-8 -*-

age = 2
if age >= 18:
    print("your is age", age)
    print('adult')
elif age >= 1:
    print("your age is", age)
    print('kid')
else:
    print("your age is", age)
    print('teenager')

# 它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('kid')
else:
    print('adult')

if True:
    print('True')
# int()函数 将字符串转为数字


height = input('身高:')
weight = input('体重:')
r = float(height) ** 2
bim = (float(weight) / r)
print('你的bmi值为 %.f %%' % bim)
if bim < 18.5:
    print('过轻')
elif 18.5 < bim < 25:
    print('正常')
elif 25 < bim < 28:
    print('过重')
elif 28 < bim < 32:
    print('肥胖')
elif bim > 32:
    print('严重肥胖')
