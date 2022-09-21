"""
@author: Tatiana Lenskaia, lensk010@umn.edu
"""


import numpy as np

def Phred33toQ(ch):
    return ord(ch)-33

def QtoPhred33(Q):
    return chr(int(round(Q))+33)



def CountACGT_GC(seq):
    seq = seq.lower();
    n = len(seq)
    
    n_a = seq.count("a");
    n_c = seq.count("c");
    n_g = seq.count("g");
    n_t = seq.count("t");
    
    n_other = n - (n_a + n_c + n_g + n_t);
    gc = round((n_c+n_g)/(n-n_other),4)*100
    
    #if n_other > 0:
        #print "Sequence has symbols other than a,c,g,t!!!"
    return [gc, n_a, n_c, n_g, n_t, n_other];


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

            tag = tag.split(" ")[4][11:(-1)].split("T")
            tag_date = tag[0]
            tag_time = tag[1]

            seqs.append(seq)
            quals.append(qual)
            tags.append([tag_date,tag_time])
    return seqs, quals, tags

def GetSampleStat(fInName, fResName):
    fRes = open(fResName, "a")
    #print("min_len","max_len", "avr_len", "len25","len50","len75", "time",file = fRes, sep = ",")
    
    
    #fInName = "FAP10569_pass_barcode01_2547abc6_1.fastq"
    
    
    seqs,quals, tags = ReadFastQ(fInName)
    
    n = len(seqs)
    print(fInName, n)
    
    
    #fOut = open("stat_med.csv","w")
    label = fInName.split(".")[0].split("_")[-1]
    fOutName = label +"_stat.csv"
    fOut = open(fOutName, "w")
    print("len","gc","q_min","q_max", "q_avr", "q25","q50","q75", "lc","lc_p","date","time",file = fOut, sep = ",")
    
    t_len = []
    t_mq = []
    min_len = 1000000
    max_len = -1000000
    total_len = 0
    
    for i in range(n):
        seq = seqs[i]
        qual = quals[i]
        tag = tags[i]
        
        gc = CountACGT_GC(seq)[0]
        
        nn = len(seq)
        
        q_min = 1000
        q_max = -1000
        lc_q = 20
        lc_ct = 0
        total = 0
        tt = []
       
        t_q = []
        for ii in range(nn):
            ch = qual[ii]
            q = Phred33toQ(ch)
            
            if q < q_min:
                q_min = q
            if q > q_max:
                q_max = q
            if q <= lc_q:
                lc_ct += 1
    
            tt.append(q)
            total = total+q
            t_q.append(q)
            
        q25, q50, q75 = np.percentile(t_q, [25, 50, 75])
        print(nn,round(gc,2),q_min,q_max, round(total/nn,2), q25, q50, q75, lc_ct, round(lc_ct/nn,2),tag[0],tag[1], file = fOut, sep = ",")
        t_len.append(nn)
        t_mq.append(q50)
        
        if nn < min_len:
            min_len = nn
        if nn > max_len:
            max_len = nn
        total_len = total_len+nn
    
    fOut.close()
    len25, len50, len75 = np.percentile(t_len, [25, 50, 75])
    
    #mq50 = np.percentile(t_mq,[50])
    avr_len = total_len/n
    q_avr = sum(t_mq)/n

    if tags[0][0] == tags[-1][0]:
        fl_date = 1
    else:
        fl_date = 0
    
    print(label,n, min_len, max_len, avr_len, len25,len50,len75, q_avr, fl_date, tags[0][1], tags[-1][1],file = fRes, sep = ",")
    

    
    fRes.close()




"""

name = "barcode03"
fListName = name+"_"+"flist.txt"




import os

arr = os.listdir()
 
print(arr)


fOut = open(fListName, "w")
for it in arr:
    fOut.write(it+"\n")
fOut.close()





"""

fListName = "list.txt"

fResName = "qc_info.csv"

fRes = open(fResName, "w")
print("tag","reads","min_len","max_len", "avr_len", "len25","len50","len75", "q_avr","same_date","first_time", "last_time",file = fRes, sep = ",")
fRes.close()


#fInName = "FAP10569_pass_barcode01_2547abc6_1.fastq"
#GetSampleStat(fInName, fResName)


fList = open(fListName,"r")
for fInName in fList:
    GetSampleStat(fInName.strip(), fResName)
fList.close()






