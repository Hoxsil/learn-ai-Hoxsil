from functools import reduce


# 合并两个数成一个数，例：1，2-->12
def fn(a,b):
    return a*10+b


# 正常请使用自带的float(s)函数
def str2float(s):
    num = -1
    for x in range(len(s)-1, 0, -1):
        if s[x] == '.':
            num = len(s)-x-1
            break
    print(num)
    s = list(map(int, [x for x in s if x != '.']))
    s = reduce(fn, s)
    s /= 10**num
    return s

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
