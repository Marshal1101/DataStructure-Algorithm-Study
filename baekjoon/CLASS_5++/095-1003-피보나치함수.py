## https://www.acmicpc.net/problem/1003


import sys


def fibonacci(n, dp) :
    if n == 0 :
        return 1, 0
    elif n == 1 :
        return 0, 1
    else :
        if dp[n-1][1] > 0 and dp[n-2][0] > 0 :
            dp[n][0] = dp[n-1][0] + dp[n-2][0]
            dp[n][1] = dp[n-1][1] + dp[n-2][1]
            return dp[n][0], dp[n][1]

        else :
            zero1, one1 = fibonacci(n-1, dp)
            dp[n-1][0] = zero1
            dp[n-1][1] = one1
            zero2, one2 = fibonacci(n-2, dp)
            dp[n-2][0] = zero2
            dp[n-2][1] = one2
            return zero1 + zero2, one1 + one2

def main() :
    input = sys.stdin.readline

    dp = [[0, 0] for _ in range(41)] 
    dp[0][0] = 1
    dp[1][1] = 1
    T = int(input())
    for _ in range(T) :
        N = int(input())
        print(*fibonacci(N, dp))


if __name__ == '__main__' :
    main()