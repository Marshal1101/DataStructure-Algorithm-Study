import sys


def flip(si:int, sj:int, N:int, M:int, board:list[list]):
    if si + 3 > N or sj + 3 > M:
        return False
    for i in range(si, si+3):
        for j in range(sj, sj+3):
            board[i][j] = 1 - board[i][j]    
    return True


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = [list(map(int, input().rstrip())) for _ in range(N)]
    B = [list(map(int, input().rstrip())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(M):
            if A[i][j] == B[i][j]:
                continue
            if flip(i, j, N, M, A):
                ans += 1
            else:
                print(-1)
                return

    print(ans)


if __name__ == '__main__':
    main()