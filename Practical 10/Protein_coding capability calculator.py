def function(DNA):
    """
    find the opening ‘ATG’ codon and the final stop ‘TGA’ codon
    calculate the length of the coding sequnence
    if > 50% protein-coding
    if < 10% non-coding
    else unclear
    
    """
    a = DNA
    b = ''
    count = 0
    for i in a:
        b = b+i.upper()
    start = b.index('ATG')
    stop = b.index('TGA')
    count = stop-start+2
    c = count/len(b)
    c=c*100
    if c > 0.5:
        print('the percentage of this sequencec is',c,'%','protein-coding')
    elif c < 0.1:
        print('the percentage of this sequencec is',c,'%','non-coding')
    else:
        print('the percentage of this sequencec is',c,'%','unclear')
    count = 0
    return(DNA)
DNA = input('DNA:')
DNA = function(DNA)
