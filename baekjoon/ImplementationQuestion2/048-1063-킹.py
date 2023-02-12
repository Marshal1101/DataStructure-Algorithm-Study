import sys


def simulate(kpos: str, spos: str, order: list, board: list[list[int]]):
    delta = {
        'R': (0, 1), 'L': (0, -1), 'B': (-1, 0), 'T': (1, 0),
        'RT': (1, 1), 'LT': (1, -1), 'RB': (-1, 1), 'LB': (-1, -1), 
    }
    pos_ij = lambda p: (int(p[1]), ord(p[0])-64)
    move = lambda i, j, d: (i+delta[d][0], j+delta[d][1])
    i, j = pos_ij(kpos)
    r, c = pos_ij(spos)
    board[r][c] = 2  
    for o in order:
        ni, nj = move(i, j, o)
        if board[ni][nj] == 1:
            continue
        elif board[ni][nj] == 0:
            i, j = ni, nj
        else:
            nr, nc = move(r, c, o)
            if board[nr][nc] != 1:
                board[nr][nc] = 2
                board[r][c] = 0
                r, c = nr, nc
                i, j = ni, nj

    ij_pos = lambda i, j: (chr(j+64) + str(i))
    return ij_pos(i, j), ij_pos(r, c)


def main():
    input = sys.stdin.readline
    board = [[1] * 10] + [[1] + [0] * 8 + [1] for _ in range(8)] + [[1] * 10]
    kpos, spos, N = input().split()
    order = [input().rstrip() for _ in range(int(N))]
    ans1, ans2 = simulate(kpos, spos, order, board)
    print(ans1)
    print(ans2)


if __name__ == '__main__':
    main()