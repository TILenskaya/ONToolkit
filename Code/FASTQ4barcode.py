"""
@author: Tatiana Lenskaia, lensk010@umn.edu
"""


def GetSingleFastQ(fOutName,t_list):
    fOut = open(fOutName,"w")
    
    
    
    for it in t_list:
        fIn = open(it,"r")
        for s in fIn:
            fOut.write(s)
        fIn.close()
        
    fOut.close()
    
def ReadFastQ(fInName):
    seqs = []
    quals = []
    tags = []
    with open(fInName) as fIn:
        while True:
            
            tag = fIn.readline().rstrip()
            #print(tag)
            #fIn.readline()
            seq = fIn.readline().rstrip()
            fIn.readline()
            qual = fIn.readline().rstrip()
            if len(seq) == 0:
                break

            #tag = tag.split(" ")[4][11:(-1)].split("T")
            #tag_date = tag[0]
            #tag_time = tag[1]

            seqs.append(seq)
            quals.append(qual)
            #tags.append([tag_date,tag_time])
            tags.append(tag)
    return seqs, quals, tags  
    
def GetSingleFastA(fOutName,t_list):
    fOut = open(fOutName,"w")
    
    
    
    for it in t_list:
        fInName = it
        seqs, quals, tags = ReadFastQ(fInName)
        
        n = len(seqs)
        for i in range(n):
            print(tags[i], file = fOut)
            print(seqs[i], file = fOut)
    fOut.close()



import core_methods as cm


label = "ID2"

fListName = "flist_filter_" + label+".txt" 

t_barcodes = cm.GetListFromFile(fListName)


fOutName = label+"_barcodes.fastq"
GetSingleFastQ(fOutName, t_barcodes)




