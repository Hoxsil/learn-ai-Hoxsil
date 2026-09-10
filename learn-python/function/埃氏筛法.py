
def _odd_item():
    n = 1
    while True:
        yield n
        n += 2


def _not_divisible(n):
    return lambda x: x % n > 0


#所有质数的iterator
def primes():
    yield 2
    primes_gen = _odd_item()
    x = next(primes_gen)
    while True:
        x = next(primes_gen)
        yield x
        primes_gen = filter(_not_divisible(x), primes_gen)
    

primes1 = primes()
for x in range(100):
    print(next(primes1))