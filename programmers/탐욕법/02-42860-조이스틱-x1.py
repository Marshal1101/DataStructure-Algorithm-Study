## 3, 19, 21 X

def solution(name):

    def updown(a) :
        # ascii A 65 ~ Z 90, N 78
        res = 0; _a = ord(a)
        if _a < 78 : res = _a - 65
        elif _a > 78 : res = 91 - _a
        else : res = 13
        # print(a, res)
        return res
    
    answer = updown(name[0])
    length = len(name)
    lend = 0; ls = 0
    rend = 0; rs = 0
    is_middle = False
    even = False
    odd = False
    # 길이가 홀수이면, 길이-1 // 2 + 1
    if length % 2 :
        end = (length - 1) // 2 + 1
        odd = True
    # 길이가 짝수이면, 길이 // 2
    else :
        end = (length // 2)
        even = True
        if name[end] != "A" :
            answer += updown(name[end])
            is_middle = True
            mid = end
    for i in range(1, end) :
        if name[i] != "A" :
            rend = i
            if not rs : rs = i
            answer += updown(name[i])
        if name[length-i] != "A" :
            lend = i
            if not ls : ls = i
            answer += updown(name[length-i])
    
    # print('odd:', odd, 'even:', even, 'mid:', is_middle, 'len', length)
    # print('r:', rend, 'rs:', rs, 'l:', lend, 'ls:', ls)
    
    if rend or lend :
        if not lend :
            if not is_middle : answer += rend
            else : answer += mid
        if not rend :
            if not is_middle : answer += lend
            else : answer += mid
        else :
            if is_middle :
                answer += min(length-ls, length-rs)
            else :
                answer += min(2*lend + rend, lend + 2*rend, length-ls, length-rs)
        
    return answer