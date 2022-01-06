## DP - 등굣길 ()

m = 5
n = 5
puddles = [[2, 3], [4, 3], [2, 5]]

def solution(m, n, puddles):
    div = 10**9 + 7
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for puddle in puddles :
        x, y = puddle
        dp[y][x] = -1

    dp[1][1] = 1
    for i in range(1, n+1) :
        for j in range(1, m+1) :
            if dp[i][j] == -1 :
                dp[i][j] = 0
                continue
            dp[i][j] += dp[i][j-1] + dp[i-1][j]
    
    return dp[n][m] % div

print(solution(m, n, puddles))

