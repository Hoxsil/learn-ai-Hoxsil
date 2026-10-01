import pandas
import os


FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(FOLDER_PATH, "福大教务处消息.txt")

data = pandas.read_json(FILE_PATH)
print(data[:100])