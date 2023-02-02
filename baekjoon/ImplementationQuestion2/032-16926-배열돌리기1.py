import sys


def main():
    input = sys.stdin.readline
    N, M, R = map(int, input().split())
    board = [input().split() for _ in range(N)]
    table = [[0] * M for _ in range(N)]
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    rot_dim = min(N, M) // 2

    for t in range(rot_dim):
        length = 2 * (N + M - 4*t) - 4
        k = R % length
        
        i = j = t
        bd = 0
        di, dj = delta[bd]
        for _ in range(k):
            if i+di >= N or i+di < 0 or j+dj >= M or j+dj < 0 or board[i+di][j+dj] == 0:
                bd = (bd + 1) % 4
                di, dj = delta[bd]
            i = i + di
            j = j + dj

        r = c = t
        td = 0
        dr, dc = delta[td]
        for _ in range(length):
            table[r][c] = board[i][j]
            board[i][j] = 0

            if i+di >= N or i+di < 0 or j+dj >= M or j+dj < 0 or board[i+di][j+dj] == 0:
                bd = (bd + 1) % 4
                di, dj = delta[bd]
            i = i + di
            j = j + dj

            if r+dr >= N or r+dr < 0 or c+dc >= M or c+dc < 0 or table[r+dr][c+dc]:
                td = (td + 1) % 4
                dr, dc = delta[td]
            r = r + dr
            c = c + dc

    for t in table:
        print(*t)


if __name__ == '__main__':
    main()