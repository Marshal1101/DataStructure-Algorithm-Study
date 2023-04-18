def rome_to_ara(rome:str) -> int:
    ret = 0
    table = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    flag49 = False
    for i in range(len(rome)-1):
        if flag49:
            flag49 = False
            continue
        else:
            a = table[rome[i]]
            b = table[rome[i+1]]
            if  a < b:
                ret += b - a
                flag49 = True
            else:
                ret += a
    if not flag49:
        ret += table[rome[-1]]

    return ret


def ara_to_rome(ara:int) -> str:
    ret = ""
    table = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
        0: '',
    }
    
    d = 1000
    while d != 0:
        c, ara = divmod(ara, d)
        if c < 5:
            if c == 4:
                ret += table[c*d]
            else:
                ret += table[d] * c
        else:
            if c == 9:
                ret += table[c*d]
            else:
                ret += table[5*d]
                ret += table[d] * (c-5)
        d //= 10

    return ret


rome1 = input().rstrip()
rome2 = input().rstrip()
ara1 = rome_to_ara(rome1)
ara2 = rome_to_ara(rome2)
print(ara1+ara2)
print(ara_to_rome(ara1+ara2))