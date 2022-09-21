"""
@author: Tatiana Lenskaia, lensk010@umn.edu
"""
import core_methods as cm

fListName = "cg_flist.txt"
flist = cm.GetListFromFile(fListName)

print(len(flist))

for fInName in flist:
    fIn = open(fInName, "r")
    t_name = fInName.split("_")
    fOut = open(t_name[0]+"_"+t_name[1]+"_consensus.fasta","w")
    for line in fIn:
        if line[0] != ">":
            line = line.upper()
        fOut.write(line)
    fOut.close()
    fIn.close()