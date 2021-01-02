THE PROJECT:

This project, intended as bioinformatics practice for myself, aims to explore the cause of disorder in the proteome of C. elegans, a roundworm with extensive data behind it. 

_________________________________________________________

DISCLAIMER:

disordered protein sequence data is from https://www.disprot.org/;
Codon Use Table is from https://www.genscript.com/tools/codon-frequency-table;
I do not claim any right to this data, nor do I intend to profit from this project, rather I just want to use it purely for an educational purpose, for practice coding.

_________________________________________________________

WHERE WE'RE AT:

IDPtry1.py -> currently, pulls data from JSON file, gathers the disordered sequence for each ID in a dictionary, then creates one long string combining all disordered regions into one big sequence. finds occurrences and frequency of each amino acid in the disordered sections, then compares that to codon use for C. elegans in graphical form.

IDP.Pandas.py -> struggling, currently paused and may abandon as it's easier to manage the data without converting to pandas (there's just too much buried).

____________________________________________________________

NOTES TO MYSELF:


GeneFilePP.json (PP stands for pretty print) JSON Structure:

data - object with a nested array of objects for each sample
    "disprot_consensus" object has the arrays:
      "disorder_function"
      "full"
      "interaction_partner"
      "structural_state"
      "structural_transition" (which contain "end", "start", and "type" string value pairs which describe where that specific sequence starts and ends, and what it is)
    "disprot_id" - string value pair (svp), unique to each sample?
    "length" - svp
    "organism" - svp
    "regions" - array with objects for each region. This also contains start and end of each region of the full sequence
    "sequence" - string value pair with FULL SEQUENCE

That seems to be the structure of the data most important to me?
