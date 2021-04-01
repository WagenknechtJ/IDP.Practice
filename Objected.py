import json
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy
from collections import Counter

# TODO - ADD MORE COMMENTS;
# SPLIT FUNCTIONS INTO... WELL... FUNCTIONS;
# MAKE IT LESS HARD CODED (EX. TITLE GRAPHS WITH ORGANISM NAME FROM FILE)
# GET ERROR BARS WORKING?

file = open('C:\\Users\\koprekj\\github\\IDP.Practice\\data\\eColiDisorderedProteome.json', encoding='utf8')
file2 = open('C:\\Users\\koprekj\\github\\IDP.Practice\\data\\eColiProteome.fasta',)

data = json.load(file)
organism = str(data['data'][0]['organism'])

print("All disordered proteins or protein segments for "+organism+", and their ID tag:\n")
ScrollingSeq = ""
Allaa = dict.fromkeys(['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'])

class Protein:
    def __init__(self, ID, seq, order):
        self.sequence = seq
        self.ID = ID
        self.order = order
    def __str__(self):
        return self.ID + ", " + self.sequence

#gather all disordered protein segments
for i in data['data']:
    sequence = ''
    for j in i['disprot_consensus']['structural_state']:
        name = "PR"+str(i['disprot_id'])
        sequence = sequence + i['sequence'][j['start']: j['end']]
    ScrollingSeq += sequence
    name = Protein(i['disprot_id'], sequence, "disordered")
    print(name)

aaDict = Counter(ScrollingSeq)
Length = len(ScrollingSeq)
print("\nThe total number of amino acids is " + str(Length))

#gather all other protein segments
Sequence2 = ""
line = file2.readline()
while (line):
    if ">" not in line:
        Sequence2 += str(line.strip())
    line = file2.readline()

aaDict2 = Counter(Sequence2)
Length2 = len(Sequence2)
print("\nThe total number of amino acids in the full proteome is " + str(Length2))

file.close()
file2.close()
