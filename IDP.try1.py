import json
import matplotlib.pyplot as plt
import numpy as np

# TO DO NEXT: Capture aa dist. of full c. elegans proteome,
#   compare aa dist. between each protein.
#   what else can be looked into? repeating aas? sections very rich in any aa?

# file = open('C:\\Users\\koprekj\\github\\PracticeandLearning\\DP00613.json',)
file = open('C:\\Users\\koprekj\\github\\IDP.Practice\\GeneFilePP.json',)

data = json.load(file)

# create dictionary of species and disordered sequence
# by using a variable(s) to store the start and end of the sequence, then grab the sequence

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

print("\n\nTotal aa's = \t" + str(totalAA))

# counts how often each aa shows up in long sequence string
Aminos = {}
for key in AADict:
    counts = 0
    stringed = str(key)
    for j in ScrollingSeq:
        if j == stringed:
            counts += 1
    AADict[key] = counts
    fraction = round(int(AADict[key])/totalAA, 3)
    Aminos.update({key: fraction})
    print("Total " + stringed + " =\t" + str(counts) + "\tFraction of aa's that are " + stringed + " = \t\t" + str(fraction))

basics = int(AADict['R']) + int(AADict['H']) + int(AADict['K'])
print("\nBasic aa's = \t" + str(basics) + "\tFraction of aa's that are basic = \t" + str(round(basics/totalAA, 3)))
acidics = int(AADict['D']) + int(AADict['E'])
print("Acidic aa's = \t" + str(acidics) + "\tFraction of aa's that are acidic = \t" + str(round(acidics/totalAA, 3)))

# codon transcription frequency, taken from internet
CodonUse = {'F': (23.9+24)/1000,
            'L': (10.2+20.1+21.1+14.9+7.9+12.1)/1000,
            'S': (16.8+10.7+20.4+12.1+12.1+8.3)/1000,
            'Y': (17.6+13.7)/1000,
            'C': (11.2+9.1)/1000,
            'W': 11/1000,
            'P': (8.9+4.5+25.9+9.6)/1000,
            'H': (14.1+9.2)/1000,
            'Q': (27.2+14.2)/1000,
            'R': (11.3+5.2+11.9+4.7+15.5+4)/1000,
            'I': (32.4+18.9+9.6)/1000,
            'M': 25.9/1000,
            'T': (18.9+10.5+19.8+8.9)/1000,
            'N': (30.3+18.4)/1000,
            'K': (37.9+26)/1000,
            'V': (24+13.6+9.9+14.3)/1000,
            'A': (22.3+12.6+19.6+8.2)/1000,
            'D': (35.5+17.1)/1000,
            'E': (40.6+24.4)/1000,
            'G': (11+6.7+31.5+4.5)/1000, }

# graphs!
plt.bar(AADict.keys(), AADict.values(), 0.33, color='b', align='edge', label = 'Disordered')
plt.title("Amino acid distribution, disordered sections of C. elegans proteome")
plt.xlabel("Amino acid")
plt.ylabel("How many occurances")
plt.show()

plt.bar(Aminos.keys(), Aminos.values(), 0.33, color='b', align='edge', label = 'Disordered')
plt.bar(CodonUse.keys(), CodonUse.values(), -0.33, color='g', align='edge', label = 'Codon Use')
plt.title("Disordered sections of C. elegans AA distribution vs Codon Use")
plt.xlabel("Amino acid")
plt.ylabel("Fraction of Occcurances")
plt.legend()
plt.show()

# counts how often each aa shows up in each protein - makes list of the proteins (as dictionaries) and dictionaries for each protein containing each aa and occurances of them
colorList = ['brown','peru','darkorange','gold','lawngreen','forestgreen','turquoise','deepskyblue','b','mediumslateblue','blueviolet','violet','magenta','crimson']
labels = AADict.keys()
x = np.arange(len(labels))
Proteins = []
incrementor = 0
start = -0.5

for protein in IDs:
    dict = {}
    for keys in AADict:
        r = 0
        for j in str(IDs[protein]):
            if j == str(keys):
                r += 1
        dict.update({keys: r})
    Proteins.append(dict)
    plt.bar(x+start, dict.values(), 0.06, color=colorList[incrementor], align='edge', label = protein)
    incrementor += 1
    start += .07
    # TO DO - continue to make numbers right to line up well

plt.title("Disordered sections of C. elegans aa distribution by protein")
plt.xlabel("Amino acid")
plt.ylabel("Number of Occcurances")
plt.legend()
plt.show()

print("\nProteins list of dictionaries is")
print(Proteins)

# TO DO - use frequency instead of occurances to level graph!

# WHATS NEXT - find average AA distribution in proteins in roundworm, compare to AA distribution here
# look further into other areas of difference or comparison

file.close()
