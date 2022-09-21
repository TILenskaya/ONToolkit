"""
@author: Tatiana Lenskaia, lensk010@umn.edu
"""


def Parse_bases(s, n):
    '''
    s = "AaAaAaaAAAaAaaAaAaaAAaAAaAAAAaAAAAAAAAAAAAAAAAAAAaAAAAAAAAAAAAAAAAAAaAaAaAAaaaaaaaAAAAAaAAaaaAaaaaaaaaaaAAAaaaaaaaaaaaaAaaaaAaAAAaaaaAaaAaAAa"
    n = 141
    
    
    
    s = "..,CC,.,..C,...CCC.C...C,.........C..,CC,.C,.C.C.CC....C............,.....,.,C...,......C....C.C,C..C...C.C.C......C..CC..CC...,."
    n = 129
    
    
    n =102	
    s = "TTtTTttTttTtt.$tTtTTtTTTTTTTTTTTTTTTTt.+3CCTtTtTtTTTtTTtTtTTTTTTtttTTTTTtTTtTTTtT.T.TtT,,tTTTTT..T,,,,,...,,"
    '''
    i = 0
    d_b={}
    
    while i < len(s):
        #print(i, s[i])
        if s[i] == "^":
            i = i+2
        if (i == (len(s) -1)) or (s[i+1] not in "+-$"):
            ch = s[i]
            if ch not in d_b:
                d_b[ch] = 1
            else:
                d_b[ch] += 1
                #print(d_b)
        else:
            if s[i+1] in "$":
                ch = s[i]
                if ch not in d_b:
                    d_b[ch] = 1
                else:
                    d_b[ch] += 1

                i = i+1
            else:  
                ch_sign = s[i+1]
                i = i+2
                n_ch = s[i]
                st_num = ""
                while n_ch in "0123456789":
                    st_num = st_num+n_ch
                    i = i+1
                    n_ch = s[i]
                num_st = int(st_num)
                #print(n_ch)
                
                st = ch_sign+st_num
                for j in range(num_st):
                    #print(st,i,j, s[i+j])
                    st = st+s[i+j]
                #print(st)
                if st not in d_b:
                    d_b[st] = 1
                else:
                    d_b[st] += 1
                i = i+j
        i = i+1
            
    #print(d_b)
    
    nn = 0
    for it in d_b:
        #print(it, d_b[it])
        nn += d_b[it]
    #print(n,nn)
    flag = 0
    if n != nn:
        flag = 1
    
    return [flag, d_b,nn]

n =102	
s = "TTtTTttTttTtt.$tTtTTtTTTTTTTTTTTTTTTTt.+3CCTtTtTtTTTtTTtTtTTTTTTtttTTTTTtTTtTTTtT.T.TtT,,tTTTTT..T,,,,,...,,"

n = 152	
s = "..,,..,.,.,...,.,.,..,,..,........,,,..,.,...........C.......................,,....,,..,...,..,,,..,.,.,....,,......,..,..,,,,..,,....,..,.....,....,..^-,"


n = 11	
s = ",.+1C..-14CCCCTCTTCTACTC.....-2CC.."


#print(Parse_bases(s,n))    