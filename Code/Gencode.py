"""
@author: Tatiana Lenskaia, lensk010@umn.edu
"""


d_alt_bases = {'R':['G','A'], 'Y':['C','T'], 'K':['G','T'], 'M':['A','C'], 'S':['G','C'],'W':['A','T'] }
  #'B':'GTC',  'D':'DAT', 'H':'ACT','V':'GCA'  
  


def nt2aa_codon(seq):
       
    gc_table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'
    }

    
    aa = ""
    if seq in gc_table:
        aa = gc_table[seq]
    return aa

def GetVar(c_ref, c_con):
    
    d_bases = {
    'R':['G','A'], 'Y':['C','T'], 'K':['G','T'], 'M':['A','C'], 'S':['G','C'],'W':['A','T'] }
    #'B':'GTC',  'D':'DAT', 'H':'ACT','V':'GCA'  
    
    
    #print(c_ref,c_con)
    
    base0 = c_con[0]
    base1 = c_con[1]
    base2 = c_con[2]
    
    if (c_ref[0] in 'ACGT') and (c_con[0] in 'RYKMSW'):
        if c_ref[0] in d_bases[c_con[0]]:
            d_bases[c_con[0]].remove(c_ref[0])
            base0 = d_bases[c_con[0]][0]

    if (c_ref[1] in 'ACGT') and (c_con[1] in 'RYKMSW'):
        if c_ref[1] in d_bases[c_con[1]]:
            d_bases[c_con[1]].remove(c_ref[1])
            base1 = d_bases[c_con[1]][0]
    
    if (c_ref[2] in 'ACGT') and (c_con[2] in 'RYKMSW'):
        if c_ref[2] in d_bases[c_con[2]]:
            d_bases[c_con[2]].remove(c_ref[2])
            base2 = d_bases[c_con[2]][0]
    return base0+base1+base2



def GetVariantType(codon_ref, codon_con):
    var_type = "-"    
             
    codon_ref = codon_ref.upper()
    codon_con = codon_con.upper()
    
    if codon_ref == codon_con:
        return "unchanged"
    
    
    if ("N" in codon_con) or ("N" in codon_ref):
        var_type = "unknown"
    
    else:
        if (codon_ref[0] in d_alt_bases) or (codon_ref[1] in d_alt_bases) or (codon_ref[2] in d_alt_bases):
            var_type = "ambiguity in a reference"
        else:
            c_alt = 0
            t_fl = [0,0,0]
            
            for ii in range(3):
                if codon_con[ii] in d_alt_bases:
                    c_alt += 1
                    t_fl[ii] = 1
                    
            if c_alt > 1:
                var_type = "ambiguity in a consensus"
            elif c_alt == 0:
    
                aa_ref = nt2aa_codon(codon_ref.upper())
                aa_con = nt2aa_codon(codon_con.upper())
                
                if aa_ref == aa_con:
                    var_type = "syn:"+aa_ref+"->"+aa_con
                else:
                    var_type = "non-syn:"+aa_ref+"->"+aa_con
            else:
                ind_1 = t_fl.index(1)
                aa_ref = nt2aa_codon(codon_ref.upper())
                codon_base = codon_con[ind_1]
                codon_con1 = codon_con[0:ind_1]+d_alt_bases[codon_base][0]+codon_con[(ind_1)+1:]
                codon_con2 = codon_con[0:ind_1]+d_alt_bases[codon_base][1]+codon_con[(ind_1)+1:]
                
                
                aa_con1 = nt2aa_codon(codon_con1.upper())
                aa_con2 = nt2aa_codon(codon_con2.upper())
                
                
            
                
                #codon_con = codon_con1 +"|"+codon_con2
                
                if aa_ref == aa_con1:
                    var_type1 = "syn:"+aa_ref+"->"+aa_con1
                else:
                    var_type1 = "non-syn:"+aa_ref+"->"+aa_con1
                if aa_ref == aa_con2:
                    var_type2 = "syn:"+aa_ref+"->"+aa_con2
                else:
                    var_type2 = "non-syn:"+aa_ref+"->"+aa_con2
                    
                if codon_con1 == codon_ref:
                    var_type = codon_con1 +"|"+ codon_con2+"," + var_type2
                else:
                    if codon_con2 == codon_ref:
                        var_type = codon_con2 +"|"+ codon_con1+"," + var_type1
                    else:
                        var_type = codon_con1+","+var_type1 + "|" +codon_con2+","+ var_type2
            
    return var_type
                        
'''                       
codon_ref = "GGG"
codon_con = "ggg"

var_type = GetVariantType(codon_ref,codon_con)

print(var_type)

'''
    

def nt2aa_seq(seq):
       
    gc_table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'
    }

    
    protein =""
    if len(seq)%3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            protein+= gc_table[codon]
    return protein