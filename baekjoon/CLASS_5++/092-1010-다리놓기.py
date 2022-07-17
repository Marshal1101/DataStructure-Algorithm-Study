import sys

def permentation(a, b, dp) :
    if dp[a][b] != 0 :
        return dp[a][b]

    ret = 1
    n = a
    i = 0
    while i < b :
        ret *= n
        i += 1
        dp[a][i] = ret
        n -= 1
    return ret

def combination(a, b, dp) :
    return permentation(a, b, dp) // permentation(b, b, dp)

def main() :
    input = sys.stdin.readline
    T = int(input())
    dp = [[0] * 31 for _ in range(31)]
    # print(dp)
    for _ in range(T) :
        N, M = map(int, input().split())
        print(combination(M, N, dp))


if __name__ == '__main__' :
    main()