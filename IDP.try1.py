import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#file = open('C:\\Users\\koprekj\\github\\PracticeandLearning\\DP00613.json',)
file = open('C:\\Users\\koprekj\\github\\IDP.Practice\\GeneFilePP.json',)

#seaborn's distplot function??

data = json.load(file)

#create dictionary of species and disordered sequence
#by using a variable(s) to store the start and end of the sequence, then grab the sequence

IDs = {}
ScrollingSeq = ""
for i in data['data']:
    for j in i['regions']:
        start = j['start']
        end = j['end']
        IDs.update({i['disprot_id']: i['sequence'][start: end]})
        ScrollingSeq += i['sequence'][start: end]

totalAA = 0
AADict = dict.fromkeys(['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'])

for j in ScrollingSeq:
    totalAA += 1

print("\n\nTotal AA's = \t" + str(totalAA))

Aminos = {}
for key in AADict:
    counts = 0
    stringed = str(key)
    for j in ScrollingSeq:
        if j == stringed:
            counts += 1
    AADict[key] = counts
    fraction = round(int(AADict[key])/totalAA, 3)
    print("Total " + stringed + " =\t" + str(counts) + "\tFraction of AA's that are " + stringed + " = \t\t" + str(fraction))

basics = int(AADict['R']) + int(AADict['H']) + int(AADict['K'])
print("\nBasic AA's = \t" + str(basics) + "\tFraction of AA's that are basic = \t" + str(round(basics/totalAA, 3)))
acidics = int(AADict['D']) + int(AADict['E'])
print("Acidic AA's = \t" + str(acidics) + "\tFraction of AA's that are acidic = \t" + str(round(acidics/totalAA, 3)))

plt.bar(dict.keys(AADict), dict.values(AADict))
plt.title("Amino Acid Distribution of Caenorhabditis elegans")
plt.xlabel("Amino Acid")
plt.ylabel("How many occurances")
plt.show()

# WHATS NEXT - find average AA distribution in proteins in roundworm, compare to AA distribution here
# look further into other areas of difference or comparison

file.close()
