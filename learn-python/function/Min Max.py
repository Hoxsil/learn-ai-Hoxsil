def findMinAndMax(L):
    if L == []:
        return (None, None)
    min_, max_ = L[0], L[0]
    for x in L:
        if max_ < x:
            max_ = x
        if min_ > x:
            min_ = x
    print(min_, max_)
    return (min_, max_)
        
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败1!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!')
else:
    print('测试成功!')