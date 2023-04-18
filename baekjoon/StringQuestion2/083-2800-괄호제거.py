string = input().rstrip()
cnt = 0
ans = set()
def bf(idx, res, open, bit):
    global cnt
    if open > cnt:
        cnt = open
    if idx == len(string):
        if open < cnt:
            ans.add(res)
        return
    
    if string[idx] == '(':
        bit = bit << 1
        tbit = bit + 1
        tres = res + string[idx]
        bf(idx+1, tres, open+1, tbit)
        bf(idx+1, res, open, bit)

    elif string[idx] == ')':
        if bit & 1 << 0:
            res += ')'
            bf(idx+1, res, open, bit >> 1)
        else:
            bf(idx+1, res, open, bit >> 1)
    else:
        bf(idx+1, res+string[idx], open, bit)

bf(0, "", 0, 0)
print('\n'.join(sorted(list(ans))))