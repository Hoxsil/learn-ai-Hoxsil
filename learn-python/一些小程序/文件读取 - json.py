import json
import os

dict1 = {"a":{"attack":1,"defend":1}}

# 获得绝对路径
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_PATH, "文件存储.json")

# 存储文件
with open(FILE_PATH, "w", encoding="utf-8") as f:
    json.dump(dict1, f, ensure_ascii=False, indent=2)

# 读取文件
with open(FILE_PATH, "r", encoding="utf-8") as f:
    dict2 = json.load(f)

print(dict2)