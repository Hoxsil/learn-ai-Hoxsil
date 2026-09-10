def normalize(name):
    name = name.lower()
    name_n = name[0].upper()
    name_n += name[1:]
    return name_n

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
