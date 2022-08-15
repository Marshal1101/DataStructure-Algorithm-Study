import sys; input = sys.stdin.readline
from collections import deque


def main():
    N, M = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]
    print(bfs(N, M, board))


def get_next_pos(dir, si, sj, N, M, board):
    if dir == 'l':
        while (sj > 1 and board[si][sj] == '.'):
            sj -= 1
        if board[si][sj] != '#': return (si, sj)
        else: return (si, sj+1)
    elif dir == 'r':
        while (sj < M-1 and board[si][sj] == '.'):
            sj += 1
        if board[si][sj] != '#': return (si, sj)
        else: return (si, sj-1)
    elif dir == 'u':
        while (si > 1 and board[si][sj] == '.'):
            si -= 1
        if board[si][sj] != '#': return (si, sj)
        else: return (si+1, sj)
    elif dir == 'd':
        while (si < N-1 and board[si][sj] == '.'):
            si += 1
        if board[si][sj] != '#': return (si, sj)
        else: return (si-1, sj)


def bfs(N, M, board):
    for i in range(N):
        for j in range(M):
            if board[i][j] != '#' and board[i][j] != '.':
                if board[i][j] == 'R':
                    Ri, Rj = i, j
                    board[i][j] = '.'
                elif board[i][j] == 'B':
                    Bi, Bj = i, j
                    board[i][j] = '.'
                else: goal = (i, j)

    print('goal:', goal, 'R:', Ri, Rj, 'B:', Bi, Bj)
    try_cnt = 0
    que = deque([(Ri, Rj, Bi, Bj)])
    while que:
        print('que:', que)
        length = len(que)
        try_cnt += 1
        for _ in range(length):
            ri, rj, bi, bj = que.popleft()

            # 위
            nbi, nbj = get_next_pos('u', bi, bj, N, M, board)
            if (nbi, nbj) != goal and ri > 1 and board[ri-1][rj] != '#':
                nri, nrj = get_next_pos('u', ri-1, rj, N, M, board)
                if (nri, nrj) == goal: return try_cnt
                elif nri != ri or nrj != rj:
                    que.append((nri, nrj, nbi, nbj))
            # 아래
            nbi, nbj = get_next_pos('d', bi, bj, N, M, board)
            if (nbi, nbj) != goal and ri < N-1 and board[ri+1][rj] != '#':
                nri, nrj = get_next_pos('d', ri+1, rj, N, M, board)
                if (nri, nrj) == goal: return try_cnt
                elif nri != ri or nrj != rj:
                    que.append((nri, nrj, nbi, nbj))
            # 자
            nbi, nbj = get_next_pos('l', bi, bj, N, M, board)
            if (nbi, nbj) != goal and rj > 1 and board[ri][rj-1] != '#':
                nri, nrj = get_next_pos('l', ri, rj-1, N, M, board)
                if (nri, nrj) == goal: return try_cnt
                elif nri != ri or nrj != rj:
                    que.append((nri, nrj, nbi, nbj))
            # 우
            nbi, nbj = get_next_pos('r', bi, bj, N, M, board)
            if (nbi, nbj) != goal and rj < M-1 and board[ri][rj+1] != '#':
                nri, nrj = get_next_pos('r', ri, rj+1, N, M, board)
                if (nri, nrj) == goal: return try_cnt
                elif nri != ri or nrj != rj:
                    que.append((nri, nrj, nbi, nbj))

    return -1


if __name__ == '__main__':
    main()