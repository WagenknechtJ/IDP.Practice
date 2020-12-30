import json
import pprint

#file = open('C:\\Users\\koprekj\\github\\PracticeandLearning\\DP00613.json',)
file = open('C:\\Users\\koprekj\\github\\IDP.Practice\\GeneFilePP.json',)

#seaborn's distplot function??

#USING JUST JSON AND PYTHON

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

#pprint.pprint(IDs)
#print(ScrollingSeq)

totalAA = 0
AADict = dict.fromkeys(['ACount', 'RCount', 'NCount', 'DCount', 'CCount', 'QCount', 'ECount', 'GCount', 'HCount', 'ICount', 'LCount', 'KCount', 'MCount', 'FCount', 'PCount', 'SCount', 'TCount', 'WCount', 'YCount', 'VCount'])

for j in ScrollingSeq:
    totalAA += 1

print("\n\nTotal AA's = \t" + str(totalAA))

for key in AADict:
    counts = 0
    stringed = str(key)
    seeking = stringed[0]
    for j in ScrollingSeq:
        if j == seeking:
            counts += 1
    AADict[key] = counts
    fraction = round(int(AADict[key])/totalAA, 3)
    print("Total " + seeking + " =\t" + str(counts) + "\tFraction of AA's that are " + seeking + " = \t\t" + str(fraction))

basics = int(AADict['RCount']) + int(AADict['HCount']) + int(AADict['KCount'])
print("\nBasic AA's = \t" + str(basics) + "\tFraction of AA's that are basic = \t" + str(round(basics/totalAA, 3)))
acidics = int(AADict['DCount']) + int(AADict['ECount'])
print("Acidic AA's = \t" + str(acidics) + "\tFraction of AA's that are acidic = \t" + str(round(acidics/totalAA, 3)))



file.close()
