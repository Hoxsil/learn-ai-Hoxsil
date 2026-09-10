import time, functools


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*arg, **wkargs):
        start_time = time.time()
        x = fn(*arg, **wkargs)
        end_time = time.time()
        print('%s executed in %f ms' % (fn.__name__, (end_time - start_time)*1000))
        return x
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
