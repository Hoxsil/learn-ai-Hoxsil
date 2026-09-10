# 组合数运算
def c(n, m):
    if n == 0:
        return 1
    num = m
    for x in range(1, n):
        num *= m-x
    for x in range(1, n+1):
        num /= x
    return int(num)


# 杨辉三角generator
def triangles():
    n = 0
    while True:
        list1 = []
        for x in range(n+1):
            list1.append(c(x,n))
        yield list1
        n += 1

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
# 获取triangles前十个返回数据（list类）
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

#输出
for t in results:
    print(t)

#测试
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
