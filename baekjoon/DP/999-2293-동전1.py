import sys


input = sys.stdin.readline
N, K = map(int, input().split())
dp = [[0] * N for _ in range(K+1)]
coin = sorted([int(input()) for _ in range(N)])
for i in range(N):
    c = coin[i]
    dp[c][i] = 1

for i in range(1, K+1):
    for j in range(N):
        c = coin[j]
        if i - c <= 0:
            continue
        dp[i][j] = dp[i-c][j]
        for u in range(j+1, N):
            if dp[i-c][u] > 0:
                dp[i][j] += 1

print(sum(dp[K]))