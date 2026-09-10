def fib():
    n, a, b = 0, 0, 1
    while True:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


a= fib()
for x in range(20):
    print(next(a))