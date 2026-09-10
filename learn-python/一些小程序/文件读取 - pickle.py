import pickle
import os

dict1 = {"a":{"attack":1,"defend":1}}

# 获得绝对路径
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_PATH, "文件存储.pkl")

# 存储文件
with open(FILE_PATH, "wb") as f:
    pickle.dump(dict1, f)

# 读取文件
with open(FILE_PATH, "rb") as f:
    dict2 = pickle.load(f)

print(dict2)