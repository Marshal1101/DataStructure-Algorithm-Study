import sys


def sec_max(si, sj, board):
    twobytwo = [
        board[si][sj],
        board[si][sj+1],
        board[si+1][sj],
        board[si+1][sj+1]
    ]
    twobytwo.sort(reverse=True)
    return twobytwo[1]


def pooling(N, board):
    if N == 1:
        return board[0][0]

    new_board = []
    for i in range(0, N, 2):
        line = []
        for j in range(0, N, 2):
            line.append(sec_max(i, j, board))
        new_board.append(line)
    ret = pooling(N//2, new_board)
    return ret


def main():
    input = sys.stdin.readline
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(pooling(N, board))


if __name__ == '__main__':
    main()