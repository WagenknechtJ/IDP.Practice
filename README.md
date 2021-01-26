THE PROJECT:

This project, intended as bioinformatics practice for myself, aims to explore the cause of disorder in the proteome of C. elegans, a roundworm with extensive data behind it. 

_________________________________________________________

DISCLAIMER:

disordered protein sequence data is from https://www.disprot.org/ (see citations below)
Codon Use Table is from https://www.genscript.com/tools/codon-frequency-table;
I do not claim any right to this data, nor do I intend to profit from this project, rather I just want to use it purely for an educational purpose, for practice coding.

_________________________________________________________

WHERE WE'RE AT:


IDPtry1.py -> currently, pulls data from JSON file, gathers the disordered sequence for each ID in a dictionary, then creates one long string combining all disordered regions into one big sequence. finds occurrences and frequency of each amino acid in the disordered sections, then compares that to codon use for C. elegans in graphical form.

IDP.Pandas.py -> struggling, currently paused and may abandon as it's easier to manage the data without converting to pandas (there's just too much buried).

_________________________________________________________

CITATIONS:


DisProt: Intrinsic protein disorder annotation in 2020
Hatos, A., Hajdu-Soltész, B., Monzon, A.M., Palopoli, N., Álvarez, L., Aykac-Fas, B., Bassot, C., Benítez, G.I., Bevilacqua, M., Chasapi, A., Chemes, L., Davey, N.E., Davidović, R., Dunker, A.K., Elofsson, A., Gobeill, J., Foutel, N.S.G., Sudha, G., Guharoy, M., Horvath, T., Iglesias, V., Kajava, A.V., Kovacs, O.P., Lamb, J., Lambrughi, M., Lazar, T., Leclercq, J.Y., Leonardi, E., Macedo-Ribeiro, S., Macossay-Castillo, M., Maiani, E., Manso, J.A., Marino-Buslje, C., Martínez-Pérez, E., Mészáros, B., Mičetić, I., Minervini, G., Murvai, N., Necci, M., Ouzounis, C.A., Pajkos, M., Paladin, L., Pancsa, R., Papaleo, E., Parisi, G., Pasche, E., Barbosa Pereira, P.J., Promponas, V.J., Pujols, J., Quaglia, F., Ruch, P., Salvatore, M., Schad, E., Szabo, B., Szaniszló, T., Tamana, S., Tantos, A., Veljkovic, N., Ventura, S., Vranken, W., Dosztányi, Z., Tompa, P., Tosatto, S.C.E., Piovesan, D.
(2020) Nucleic Acids Research, 48 (D1), pp. D269-D276.
PubMed: 31713636
DOI: 10.1093/nar/gkz975

DisProt 7.0: A major update of the database of disordered proteins
Piovesan, D., Tabaro, F., Mičetić, I., Necci, M., Quaglia, F., Oldfield, C.J., Aspromonte, M.C., Davey, N.E., Davidović, R., Dosztányi, Z., Elofsson, A., Gasparini, A., Hatos, A., Kajava, A.V., Kalmar, L., Leonardi, E., Lazar, T., Macedo-Ribeiro, S., Macossay-Castillo, M., Meszaros, A., Minervini, G., Murvai, N., Pujols, J., Roche, D.B., Salladini, E., Schad, E., Schramm, A., Szabo, B., Tantos, A., Tonello, F., Tsirigos, K.D., Veljković, N., Ventura, S., Vranken, W., Warholm, P., Uversky, V.N., Dunker, A.K., Longhi, S., Tompa, P., Tosatto, S.C.E.
(2017) Nucleic Acids Research, 45 (D1), pp. D219-D227.
PubMed: 27899601
DOI: 10.1093/nar/gkw1056

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
