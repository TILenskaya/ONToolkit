
"""
@author: Tatiana Lenskaia, lensk010@umn.edu
"""


import core_methods as cm


pref = ""

res1 = cm.GetDictFromFile("res_list.txt", sep= '\t', header=1)
d_list = res1[1]
t_list = res1[0]

'''
print(len(d_list))
for it in d_list:
    print(it, len(d_list[it]))
'''

fStat = open(pref+'all_stat.txt',"w")
print("FastQ", "Ref_len", "Cons_len","Ns", file = fStat, sep = "\t")

for it in t_list:
    print(it)
    if it in d_list:
        #fRefName = '(21093_2019)MZ423536.1.fasta'
        fRefName = d_list[it][0]
        refgen = cm.GetText(fRefName)
        #print(len(refgen))
        n_refgen = len(refgen)
        
        
        
        #fInName = 'FAQ02720_barcode01_all_sorted_cns.fasta'
        fInName = d_list[it][1]
        cons = cm.GetText(fInName)
        #print(len(cons))
        n_cons = len(cons)
        
        
        
        #fInCov = 'FAQ02720_barcode01_all_coverage.txt'
        fInCov = d_list[it][2]
        res = cm.GetDictFromFile(fInCov, "\t", header=0, unique_col = 1)
        #print(res[1])
        
        d = res[1]
        
        
        if n_refgen >= n_cons:
            
            fOutName = pref+fInName.rsplit('.')[0]+"_res.txt"
            fOut = open(fOutName, "w")
            print("Consensus","Refgen", "Pos","Refgen_base","Cons_base", "mpileup_base","#reads","bases", "qscores", file = fOut, sep ="\t")
         
            for i in range(n_refgen):
                refbase = '-'
                nreads = '-'
                bases = '-'
                quals = '-'
                
                ind = str(i+1)
                if ind in d:
                    refbase = d[ind][1]
                    nreads = d[ind][2]
                    bases = d[ind][3]
                    quals = d[ind][4]
                if i >= n_cons:
                    cons_i = "_"
                else:
                    cons_i = cons[i]
                
                print(fInName, fRefName, ind, refgen[i], cons_i, refbase, nreads, bases, quals, file = fOut, sep = "\t")
            fOut.close()
        else:
            print("Consensus is longer than reference!")
        c = 0
        for i in range(n_cons):
            if (cons[i] == "N") or (cons[i] == "n"):
                c += 1
        print(it, n_refgen, n_cons, c, file = fStat, sep = "\t")
    
    
    #break
fStat.close() 

    
"""
fRefName = '(21093_2019)MZ423536.1.fasta'
refgen = cm.GetText(fRefName)
print(len(refgen))
n_refgen = len(refgen)



fInName = 'FAQ02720_barcode01_all_sorted_cns.fasta'
cons = cm.GetText(fInName)
print(len(cons))
n_cons = len(cons)



fInCov = 'FAQ02720_barcode01_all_coverage.txt'
res = cm.GetDictFromFile(fInCov, "\t", header=0, unique_col = 1)
print(res[1])

d = res[1]


fOutName = fInName.rsplit('.')[0]+"_res.txt"
fOut = open(fOutName, "w")
print("Consensus","Refgen", "Pos","Refgen_base","Cons_base", "Ref_base_again","#reads","bases", "qscores", file = fOut, sep ="\t")
if n_refgen == n_cons:

    for i in range(n_refgen):
        refbase = '-'
        nreads = '-'
        bases = '-'
        quals = '-'
        
        ind = str(i+1)
        if ind in d:
            refbase = d[ind][1]
            nreads = d[ind][2]
            bases = d[ind][3]
            quals = d[ind][4]
            
        print(fInName, fRefName, ind, refgen[i], cons[i], refbase, nreads, bases, quals, file = fOut, sep = "\t")
fOut.close()
    

"""