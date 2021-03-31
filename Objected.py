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
    def __init__(self, ID, seq):
        self.sequence = seq
        self.ID = ID
    def __str__(self):
        return self.ID + ", " + self.sequence

for i in data['data']:
    sequence = ''
    for j in i['disprot_consensus']['structural_state']:
        name = "PR"+str(i['disprot_id'])
        sequence = sequence + i['sequence'][j['start']: j['end']]
    ScrollingSeq += sequence
    name = Protein(i['disprot_id'], sequence)
    print(name)

AADict = Counter(ScrollingSeq)

print("\nThe total number of amino acids is " + str(len(ScrollingSeq)))

file.close()
file2.close()
