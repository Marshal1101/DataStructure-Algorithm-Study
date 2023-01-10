# https://www.acmicpc.net/source/48046899

def sol():
    pnumber=0
    a=0
    np='NP'
    for i in input():
        if i=='P':
            if a:
                pnumber-=1
                a=0
            else:
                pnumber+=1
        elif pnumber<2:
            return np
        else:
            a=1
    if pnumber==1:
        return 'PPAP'
    return np
print(sol())