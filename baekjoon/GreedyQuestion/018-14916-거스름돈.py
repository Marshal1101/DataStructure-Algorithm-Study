def main():
    N = int(input())
    if N < 6:
        if N == 2 or N == 5:
            print(1)
        elif N == 4:
            print(2)
        else:
            print(-1)
        return

    dp = [N] * (N+1)
    dp[2] = dp[5] = 1
    for i in range(2, N-1):
        dp[i+2] = min(dp[i] + 1, dp[i+2])
    for i in range(5, N-4):
        dp[i+5] = min(dp[i] + 1, dp[i+5])

    if dp[-1] != N:
        print(dp[-1])
    else:
        print(-1)

if __name__ == '__main__':
    main()