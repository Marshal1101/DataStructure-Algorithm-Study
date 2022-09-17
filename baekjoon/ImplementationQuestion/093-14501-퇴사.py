import sys


def main() :
    input = sys.stdin.readline
    N = int(input())
    dp = [0] * (N+6)

    for i in range(1, N+1) :
        T, P = map(int, input().split())
        dp[i] = dp[i] if dp[i] > dp[i-1] else dp[i-1]
        dp[i+T] = dp[i+T] if dp[i+T] > dp[i] + P else dp[i] + P
    
    dp[N+1] = dp[N+1] if dp[N+1] > dp[N] else dp[N]
    print(dp[N+1])


if __name__ == "__main__" :
    main()