## 재귀 - 괄호 변환 (참조 https://hellominchan.tistory.com/352)

import sys
sys.setrecursionlimit(10**6)

def split_two_parts(s) :
    if not s :
        return

    n = len(s)
    lp = 0 ; rp = 0
    for i in range(n) :
        if s[i] == '(' : lp += 1
        else           : rp += 1

        if lp == rp :
            return s[:i+1], s[i+1:]

def isCorrect(u):
    stack = []
    for p in u:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()
            
    return True


def solution(w):
    # 과정 1
    if not w:
        return ""
    
    # 과정 2
    u, v = split_two_parts(w)
    
    # 과정 3
    if isCorrect(u):
        # 과정 3-1
        return u + solution(v)
    # 과정 4
    else:
        # 과정 4-1
        answer = '('
        # 과정 4-2
        answer += solution(v)
        # 과정 4-3
        answer += ')'
        
        # 과정 4-4
        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('
        
        # 과정 4-5
        return answer

print(solution("()))((()"))