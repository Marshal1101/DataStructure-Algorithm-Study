import sys


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    board = [input().rstrip() for _ in range(N)]
    ans = 0
    for i in range(N):
        is_prev_dash = False
        for j in range(M):
            if board[i][j] == '-':
                if not is_prev_dash:
                    ans += 1
                    is_prev_dash = True
            elif board[i][j] == '|':
                if i == 0:
                    ans += 1
                elif board[i-1][j] != '|':
                    ans += 1
                is_prev_dash = False

    print(ans)


if __name__ == '__main__':
    main()