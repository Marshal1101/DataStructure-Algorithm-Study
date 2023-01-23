import sys


def combination(arr, K, k=0):
    N = len(arr)
    ans = []

    def dfs(si, k):
        if k == K:
            print(" ".join(ans))
            return

        for i in range(si, N):
            ans.append(arr[i])
            dfs(i+1, k+1)
            ans.pop()
            
    dfs(0, k)


input = sys.stdin.readline
while (pot := input().split())[0] != "0":
    N = pot.pop(0)
    combination(pot, 6)
    print()