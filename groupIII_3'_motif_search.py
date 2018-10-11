################################################################################
#
#                   Search for Group III twinton 3' motifs
#                   ______________________________________
#
# A program to to find 3' motifs for group III twintrons, given the external 
#   intron in FASTA format.
#
# ** Program must be in same location as fasta file. **
# 
# Assumption: only one sequence submitted in fasta file.
# 
#   by: Matthew Bennett, Michigan State University
#
################################################################################

# Function to complement a sequence
def complement(sequence):
    complement = ""
    for i in sequence:
        if i == "A":
            complement += "T"
        elif i == "T":
            complement += "A"
        elif i == "C":
            complement += "G"
        elif i == "G":
            complement += "C"

    return complement

matches = [] #Blank list for potential 3' matches.

while True:
    try:
        file_nm = input("FASTA file containg your external intron: ")
        file = open(file_nm, "r")
        break
    except FileNotFoundError:
        print ("\n", "FASTA file not found", "\n", sep = "")
        
#First line in FASTA is sequence name, strip of white space and get rid of ">"  
seq_name = file.readline().strip()[1:]
# Second fasta line is sequence, strip of white space  
seq = file.readline().strip()
# Strip the first 5 bases and last 5 bases, they only apply to external intron
seq = seq[5:-5]
# Reverse the sequence
rev_seq = seq[::-1]

# iterate through sequence and find an "A" to look for pattern:
#    abcdef (3–8 nucleotides) f'e'd' A c'b'a' (four nucleotides)
for i, base in enumerate(rev_seq):
    if base == "A":
        index = i
        search_seq_rev = rev_seq[(index-3):index] + rev_seq[(index+1):(index+4)]
        search_area_rev = rev_seq[(index+7):(index + 18)]
        search_seq_rc = complement(search_seq_rev)


        if len(search_seq_rev) == 6:
            search_area = search_area_rev[::-1]
            check = search_area.find(search_seq_rc)

            if check != -1:
                total_area_rev = rev_seq[(index-3):(index + 18)] 
                total_area = total_area_rev[::-1]
                match_area = total_area[check:] 
                match = (match_area)
                matches.append(match)

print ("\n", len(matches), " potential 3' motif(s) found in ",\
        file_nm, ":", "\n", sep = "")

for i in matches:
    print (i)

if len(matches) > 0:
    print ("\n", "*** Remember to add 4 bases to the end of any accepted\
 matching sequence ***", "\n", sep = "")