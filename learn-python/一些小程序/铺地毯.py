def is_blanket(L):
    a = x_ >= L[0] and x_ <= L[0] + L[2]
    b = y_ >= L[1] and y_ <= L[1] + L[3]
    return a and b


n = int(input())
a = []
for x in range(n):
    a.append(list(map(int, input().split())))
x_, y_ = tuple(tuple(map(int, input().split())))


num = -1
for x in range(n):
    if is_blanket(a[x]):
        num = x+1
print(num)