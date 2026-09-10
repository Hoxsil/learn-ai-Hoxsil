dict1 = {"pig":5, 'dog':6}
dict2 = {"pig":4, "dog":4}
print("输出：", dict1.keys() == dict2.keys())
a = sum(dict1[x] for x in dict1)
print(sum(dict1[x] for x in dict1))