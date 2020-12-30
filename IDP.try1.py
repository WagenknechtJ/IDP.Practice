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

pprint.pprint(IDs)
print(ScrollingSeq)

totalAA = 0
# AADict = dict.fromkeys(['ACount', 'RCount', 'NCount', 'DCount', 'CCount', 'QCount', 'ECount', 'GCount', 'HCount', 'ICount', 'LCount', 'KCount', 'MCount', 'FCount', 'PCount', 'SCount', 'TCount', 'WCount', 'YCount', 'VCount'])
ACount, RCount, NCount, DCount, CCount, QCount, ECount, GCount, HCount, ICount, LCount, KCount, MCount, FCount, PCount, SCount, TCount, WCount, YCount, VCount  = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

for j in ScrollingSeq:
    totalAA += 1
    if j == 'A':
        ACount += 1
    if j == 'R':
        RCount += 1
    if j == 'N':
        NCount += 1
    if j == 'D':
        DCount += 1
    if j == 'C':
        CCount += 1
    if j == 'Q':
        QCount += 1
    if j == 'E':
        ECount += 1
    if j == 'G':
        GCount += 1
    if j == 'H':
        HCount += 1
    if j == 'I':
        ICount += 1
    if j == 'L':
        LCount += 1
    if j == 'K':
        KCount += 1
    if j == 'M':
        MCount += 1
    if j == 'F':
        FCount += 1
    if j == 'P':
        PCount += 1
    if j == 'S':
        SCount += 1
    if j == 'T':
        TCount += 1
    if j == 'W':
        WCount += 1
    if j == 'Y':
        YCount += 1
    if j == 'V':
        VCount += 1

print("\n\nTotal AA's = \t" + str(totalAA))
print("Cystines = \t" + str(CCount) + "\tFraction of AA's that are cystine = \t" + str(CCount/totalAA))
print("Basic AA's = \t" + str(KCount + RCount) + "\tFraction of AA's that are basic = \t" + str((KCount + RCount)/totalAA))
print("Acidic AA's = \t" + str(DCount + QCount) + "\tFraction of AA's that are acidic = \t" + str((DCount + QCount)/totalAA))



file.close()
