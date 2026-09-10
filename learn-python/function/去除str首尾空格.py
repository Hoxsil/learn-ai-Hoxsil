def trim(s):
    a, b = 0, len(s)-1
    for x in range(len(s)):
        if s[x] != ' ':
            a = x
            break
        if x == len(s)-1:
            return ''
    for x in range(len(s)-1, -1, -1):
        if s[x] != ' ':
            b = x
            break
    return s[a:b+1]

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
