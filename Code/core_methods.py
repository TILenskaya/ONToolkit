"""
@author: Tatiana Lenskaia, lensk010@umn.edu
"""


def GetListFromFile(fInName):
    t = []
    fIn = open(fInName, "r")
    for line in fIn:
        line = line.strip()
        if line != "":
            if line not in t:
                t.append(line)
    #print(len(t))
    fIn.close()
    return t


def GetDictFromFile(fInName, sep, header, unique_col = 0):
    fIn = open(fInName,"r")
    lines = fIn.readlines()
    
    header_line = ""
    
    if header == 1:
        header_line = lines[0]
        lines = lines[1:]
    
    
    d = {}
    t = []
    
    n = len(lines[0].split(sep))
    
    for line in lines:
        line = line.strip()
        if line != "":
            t_line = line.split(sep)
            if len(t_line) != n:
                print("Check format!", line, t_line)
                if t_line[0] not in d:
                    t.append(t_line[0])
                    d[t_line[0]] = t_line[1:]
                
            else:
                
                col_id = t_line[unique_col]
                tt = t_line[0:unique_col]+t_line[unique_col+1:]
                
                if col_id not in d:
                    t.append(col_id)
                    d[col_id] = tt
                else:
                    print("First colum has non-unique values!")
    fIn.close()
    return [t,d, header_line]
