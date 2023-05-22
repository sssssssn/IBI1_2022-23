#Count the number of coding sequences
#import the module
import re
#open and read the file
data = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r' )
readdata=data.read()

b = readdata.split('>')#used to split the genes
a = input('input a stop codon')
name=a+'_stop_genes.fa'#find the specific file
file = open(name,'w')
count = 0
for DNA in b:
    if DNA[-4:-1]==a:#Determine whether the terminator is consistent
        c = DNA.index('ATG')
        sequencelist=DNA[c:].split('\n')
        sequence=''.join(sequencelist)#read out the specific gene with the name of the gene
        number=re.findall(a,DNA)
        count = count+ len(number) #count the number of coding sequences made in this gene
        file.write('>'+ DNA[:7]+'\n'+str(count)+'\n'+sequence+'\n')
        count=0
file.flush()
        

