import sys


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    M, K = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(M)]

    ans = [[0 for _ in range(K)] for _ in range(N)]
    for i in range(N):
        for k in range(K):
            tmp = 0
            for j in range(M):
                tmp += A[i][j] * B[j][k]
            ans[i][k] = str(tmp)
    
    for a in ans:
        print(" ".join(a))


if __name__ == '__main__':
    main()