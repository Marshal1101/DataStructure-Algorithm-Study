import sys
sys.setrecursionlimit(10**9)


def bf(N, nums, stk, ans: set):
    if len(stk) == N:
        tot = 0
        for i in stk:
            tot += nums[i]
        ans.add(tot)
        return

    for i in range(4):
        if not stk or i <= stk[-1]:
            stk.append(i)
            bf(N, nums, stk, ans)
            stk.pop()

N = int(input())
nums = [1, 5, 10, 50]
ans = set()
bf(N, nums, [], ans)    
print(len(ans))