import re
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
#import DNA sequence
count = 0
#store the number of possible coding sequences
if re.search('ATG',seq):
#find the start codon
    a = re.findall(r'TAA',seq)
    count = count + len(a)
    b = re.findall(r'TAG',seq)
    count = count+len(b)
    c = re.findall(r'TGA',seq)
    count = count+len(c)
#find the stop codons and counting
print('The total number of possible coding sequences is', count)

