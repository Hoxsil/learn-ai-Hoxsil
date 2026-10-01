import pandas


data = {'Name': ['Google', 'Runoob', 'Taobao'], 'Age': [25, 30, 35]}
df = pandas.DataFrame(data)
s = pandas.Series(data)
print("DataFrame:", df)
print("Series:", s)