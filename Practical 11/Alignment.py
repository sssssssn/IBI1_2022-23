def global_ali(val1,val2):
    BLOSUM62 = open('/Users/shennuo/IBI1_2022-23/Practical 11/BLOSUM.txt')
    BLOSUM62_read = BLOSUM62.readlines()
    blosum62 =[]
    for i in range(0,len(BLOSUM62_read)):
        blosum62.append(BLOSUM62_read[i].split(","))
    for j in range(0,len(blosum62)):
        blosum62[j][-1]=blosum62[j][-1][0] #用来除去每行末尾的换行符
    keys=blosum62[0]
    index1=keys.index(val1)
    index2=keys.index(val2)
    score=int(blosum62[index1][index2])
    return score
    
def compare(seq1,seq2):
    score_total=0
    same = 0
    seq1_name = seq1[0]
    seq2_name = seq2[0]
    effseq1 = seq1[1]
    effseq2 = seq2[1]
    for i in range(0,len(effseq1)):
        score_total += global_ali(effseq1[i], effseq2[i])
        if effseq1[i] == effseq2[i]:
            same = same + 1
    per = same / len(effseq1) * 100
    print(seq1_name,effseq1)
    print(seq2_name,effseq2)
    print("Alignment Score:",score_total)
    print("the percentage of identical amino acids:",per)
    return score_total

cat = open('/Users/shennuo/IBI1_2022-23/Practical 11/ACE2_cat.fa')
cat_seq = cat.readlines()
mouse = open('/Users/shennuo/IBI1_2022-23/Practical 11/ACE2_mouse.fa')
mouse_seq = mouse.readlines()
human = open('/Users/shennuo/IBI1_2022-23/Practical 11/ACE2_human.fa')
human_seq = human.readlines()

hc = compare(human_seq,cat_seq)
hm = compare(human_seq,mouse_seq)
cm = compare(cat_seq,mouse_seq)

cat.close()
mouse.close()
human.close()
       