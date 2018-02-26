#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ['m', 'b', 'c']

print(classmates)

print(len(classmates))

# list 索引
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-2])
print(classmates[-3])
print("直接获取最后一个元素:" , classmates[-1])
# 追加元素
classmates.append('a')
print(classmates)
# 中间插入元素
classmates.insert(1, 'jack')
print(classmates)

# 删除最后一个元素
print("删除最后一个元素:", classmates.pop())
print(classmates)

# 删除指定位置的元素
print(classmates.pop(1))
print(classmates)

# 替换某个元素
classmates[1] = 'SSssarach'
print(classmates)

# list 里面的类型也可以是不同的类型
l = ['apple', 123, True]
print(l)

# list元素也可以是另一个list
p = ['assp', 'php']
s = ['python', 'java', p]

# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
ss = ('a', 'b', 'c')
print(ss)

# 可变的”tuple
t = ('a', 'b', ['A', 'B'])
print(t[2][0])
print(t[2][1])

print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print("apple:" + L[0][0])
print("python:" + L[1][1])
print("Lisa:" + L[2][2])
