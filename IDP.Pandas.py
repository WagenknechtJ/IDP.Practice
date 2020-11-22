import json
import pandas as pd
import numpy as np
import pprint

#file = open('C:\\Users\\koprekj\\github\\PracticeandLearning\\DP00613.json',)
file = open('C:\\Users\\koprekj\\github\\PracticeandLearning\\GeneFilePP.json',)

data = pd.read_json('C:\\Users\\koprekj\\github\\PracticeandLearning\\GeneFilePP.json', orient='records',)
type(data)

pd.set_option("display.max.columns", None)
pd.set_option("display.precision", 2)
print(data.head())
print(data.info())

#print(data.describe(include = np.object))

print(data[sequence])
