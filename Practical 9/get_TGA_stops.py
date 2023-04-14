file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r' )
readfile=file.read()
#read the file
a=readfile.split('>')
#split the DNA into a list
newfile=open('TGA_genes.fa', 'w')
#creat a new file
for DNA in a:
    if DNA[-4:-1]=='TGA':
       start=DNA.index('ATG')
       sequencelist=DNA[start:].split('\n')
       sequence=''.join(sequencelist)
       print(DNA[:7]+'\n')
       print(sequence+'\n')
       newfile.write(DNA[:7]+'\n'+sequence+'\n')
newfile.flush()
#put the name of gene with 'TGA' into a new file 
