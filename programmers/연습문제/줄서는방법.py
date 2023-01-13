# Lv. 2
# https://school.programmers.co.kr/learn/courses/30/lessons/12936

import math
def solution(n, k):
    answer = []
    nums = [i for i in range(1, n+1)]
    while nums:
        fac = 1
        for i in range(1, len(nums)):
            fac *= i
        
        idx = math.ceil(k/fac) - 1
        answer.append(nums[idx])
        del nums[idx]
        k = k - idx * fac
    
    return answer



import math
def solution(n, k):
    ans = [i for i in range(1, n+1)]
    k -= 1
    for i in range(n-1):
        q, r = divmod(k, math.factorial(n-i-1))
        ans[i], ans[i+q] = ans[i+q], ans[i]
        ans[i+1:] = sorted(ans[i+1:])
        k = r
    return ans