import sys


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    board = [[0] * 100 for _ in range(100)]
    for _ in range(N):
        li, lj, ri, rj = map(lambda x: int(x)-1, input().split())
        for i in range(li, ri+1):
            for j in range(lj, rj+1):
                board[i][j] += 1
    ans = 0
    for i in range(100):
        for j in range(100):
            if board[i][j] > M:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()