import time


start_time = time.time()
for i in range(100000):
    print(i)
time.sleep(2)
end_time = time.time()
print("运行时间：", end_time - start_time, "s")