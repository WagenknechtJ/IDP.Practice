import json
import pprint

#file = open('C:\\Users\\koprekj\\github\\PracticeandLearning\\DP00613.json',)
file = open('C:\\Users\\koprekj\\github\\PracticeandLearning\\GeneFilePP.json',)

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

pprint.pprint(IDs)
print(ScrollingSeq)

aCount, tCount, cCount, gCount = 0, 0, 0, 0

for j in ScrollingSeq:
    if j == 'A':
        aCount += 1
    if j == 'T':
        tCount += 1
    if j == 'C':
        cCount += 1
    if j == 'G':
        gCount += 1

print("Number of A's = " + aCount + "/n/tT's = " + tCount + "/n/tC's = " + cCount + "/n/tG's = " + gCount)
#START HERE: get this print statement working next time
# look at number of each amino acid in all sequences

file.close()
