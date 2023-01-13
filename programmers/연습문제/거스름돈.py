# Lv. 3
# https://school.programmers.co.kr/learn/courses/30/lessons/12907

def solution(n, money):
    answer = 0
    money.sort()
    if money[0] == 1: dp = [1 for _ in range(100001)]
    else: dp = [0 for _ in range(100001)]
    
    dp[0] = 1
    for m in money:
        if m == 1: continue
        for i in range(1, n+1):
            if i - m >= 0:
                dp[i] += dp[i-m] % 1000000007

    answer = dp[n]
    
    return answer