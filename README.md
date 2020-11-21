DISCLAIMER: data is from https://www.disprot.org/ - I do not claim any right to it, but use it purely for an educational purpose

_________________________________________________________

Where we're at?

IDPtry1.py -> currently, pulls data from JSON file, gathers the disordered sequence for each ID in a library??, then creates one long string combining all disordered regions into one big sequence

IDP.Pandas.py -> currently converts JSON data into python?, prints the first 5 objects

____________________________________________________________

GeneFilePP.json (PP stands for pretty print) JSON Structure:

data - array?
  each sample is an object within an array
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
