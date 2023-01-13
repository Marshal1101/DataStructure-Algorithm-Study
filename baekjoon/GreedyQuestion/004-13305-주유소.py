import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    dist = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    dp = [0 for _ in range(N)]
    dp[0] = 0
    min_cost = int(1e9)
    for i in range(1, N):
        if (new := dp[i-1] + dist[i-1] * cost[i-1]) \
            < (old := dp[i-1] + dist[i-1] * min_cost):
            dp[i] = new
            min_cost = cost[i-1]
        else:
            dp[i] = old

    print(dp[-1])

if __name__ == '__main__':
    main()