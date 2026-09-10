import json, pickle, os, random, time, copy
from typing import Any
import skill
from pokemon import Pokemon
from skill import SKILL_FUNCTION_DICT
from buff import BUFF_ROUND_DICT, BUFF_FUNCTOIN_DICT

BASE_PATH:str = os.path.dirname(os.path.abspath(__file__))
FILE_PATH_pickle:str = os.path.join(BASE_PATH, "Pokemon_Repository.pkl")
FILE_PATH_json:str = os.path.join(BASE_PATH, "Pokemon_Repository.json")
# 打开所有宝可梦的列表
with open(FILE_PATH_pickle, "rb") as f:
    all_pokemon_list:list = pickle.load(f)

self = all_pokemon_list[0]
list1 = ["", "", "water", "thunder"]

list2 = [x for x in self.buff if BUFF_ROUND_DICT[x] == 1]

print(list2)