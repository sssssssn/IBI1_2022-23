import re
data = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r' )
readdata=data.read()
b = readdata.split('>')
a = input('input a stop codon')
name=a+'_stop_genes.fa'
file = open(name,'w')
count = 0
for DNA in b:
    if DNA[-4:-1]==a:
        c = DNA.index('ATG')
        sequencelist=DNA[c:].split('\n')
        sequence=''.join(sequencelist)
        number=re.findall(a,DNA)
        count = count+ len(number) 
        file.write(DNA[:7]+'\n'+str(count)+'\n'+sequence+'\n')
        count=0
file.flush()
        
