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
        count = count+1
        file.write(DNA[:7]+'\n'+DNA[c:]+'\n')
file.write(str(count))
file.flush()
        
