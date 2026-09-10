from functools import reduce

def prod(list1):
    num = reduce(lambda a,b: a*b, list1)
    return num

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')