# for...in循环
names = ['ls', 'pr', 'jk']
for name in names:
    print(name)
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x

print(sum)

# range()函数，可以生成一个整数序列
# 再通过list()函数可以转换为list
print(list(range(5)))

# 计算 1- 100 的和
count = 0
for x in list(range(101)):
    count = count + x

print(count)

# 第二种循环是while循环
num = 0
n = 99

while n > 0:
    num = num + n;
    n = n - 2

print(num)

L = ['Bart', 'Lisa', 'Adam']

for x in L:
    print('Hello,%s!' % x)



# break
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1

print('END')

#continue
m = 0
while m < 10:
    m = m + 1
    if m % 2 == 0:
        continue
    print('打印基数',m)