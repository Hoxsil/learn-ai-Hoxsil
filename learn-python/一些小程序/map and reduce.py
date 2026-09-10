from functools import reduce


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = map(lambda x: x*x, list)
for y in x:
    print(y)

x = reduce(lambda a,b: a+b, list)
print(x)