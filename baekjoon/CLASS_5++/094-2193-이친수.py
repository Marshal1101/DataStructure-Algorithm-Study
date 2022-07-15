## https://www.acmicpc.net/problem/2193


import sys


def pinary_number(n, dp) :
    if n == 1 :
        dp[1][1] = 1
        return 0, 1
    
    elif dp[n][0] != 0 or dp[n][1] != 0 :
        return dp[n][0], dp[n][1]
        
    else :
        zero, one = pinary_number(n-1, dp)
        dp[n][1] = zero
        dp[n][0] = zero + one
        return dp[n][0], dp[n][1]


def main() :
    N = int(sys.stdin.readline())
    dp = [[0, 0] for _ in range(N+1)]
    print(sum(pinary_number(N, dp)))


if __name__ == '__main__' :
    main()