import sys


def try_attach(si, sj, stkr, board) -> bool:
    R = len(stkr)
    C = len(stkr[0])
    for i in range(R):
        for j in range(C):
            if stkr[i][j] == 1 and board[si+i][sj+j] == 1:
                return False
    return True

def check(stkr, board) -> tuple:
    N = len(board)
    M = len(board[0])
    R = len(stkr)
    C = len(stkr[0])
    for i in range(N+1-R):
        for j in range(M+1-C):
            if try_attach(i, j, stkr, board):
                return i, j
    return (-1, -1)

def attach(si, sj, stkr, board) -> None:
    R = len(stkr)
    C = len(stkr[0])
    for i in range(R):
        for j in range(C):
            if stkr[i][j]:
                board[si+i][sj+j] = 1

def rotate_clockwise(strk: list[list]):
    ret = []
    for s in zip(*strk):
        s = list(s)
        s.reverse()
        ret.append(s)
    return ret

def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    for k in range(K):
        R, C = map(int, input().split())
        stkr = [list(map(int, input().split())) for _ in range(R)]
        rot = 0
        while True:
            pi, pj = check(stkr, board)
            if pi != -1 and pj != -1:
                attach(pi, pj, stkr, board)
                break
            if (rot == 3): break
            stkr = rotate_clockwise(stkr)
            rot += 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                cnt += 1

    print(cnt)
    # for b in board:
    #     print(b)


if __name__ == '__main__':
    main()