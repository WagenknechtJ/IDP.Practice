import json
import pandas as pd
import numpy as np
import pprint

# READ - current;y trying to figure out how to access things in objects.

# file = open('C:\\Users\\koprekj\\github\\PracticeandLearning\\DP00613.json',)
file = open('C:\\Users\\koprekj\\github\\IDP.Practice\\GeneFilePP.json')

data = pd.read_json('C:\\Users\\koprekj\\github\\IDP.Practice\\GeneFilePP.json', orient='split')
type(data)

pd.set_option("display.max.columns", None)
pd.set_option("display.precision", 2)

# print("head is \n")
# print(data.head())
# print("info is\n")
# print(data.info())

IDs = {}
ScrollingSeq = ""

print(data.regions["curator_id"])

# to do next - look at AAs for how common things are (like on the standard genetic code);
# and count by properties (sulfides for disulfide bonds, hydrophobic and hydrophilic, etc)

# print("\nAA counts below:\n"+sequenceData.value_counts())
