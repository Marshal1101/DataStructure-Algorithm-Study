import sys; input = sys.stdin.readline
from collections import deque


def main():
    N, M = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]
    print(bfs(N, M, board))

def get_east_pos(i, j, M, board):
    while (j < M and board[i][j] == '.'):
        j += 1
    return (i, j)

def get_west_pos(i, j, M, board):
    while (j > M and board[i][j] == '.'):
        j -= 1
    return (i, j)

def get_north_pos(i, j, N, board):
    while (i > N and board[i][j] == '.'):
        i -= 1
    return (i, j)

def get_south_pos(i, j, N, board):
    while (i < N and board[i][j] == '.'):
        i += 1
    return (i, j)

def check_move(pos, flag, queue, N, M, board, func_get_pos):
    nri, nrj = func_get_pos(pos[0], pos[1], M, board)
    if board[nri][nrj] != 'O':
        nrj -= 1
        flag[0] = False
    else: flag_R = True
    nbi, nbj = func_get_pos(pos[2], pos[3], N, M, board)
    if board[nbi][nrj] != 'O':
        nbj -= 1
        flag_B = False
    else: flag[1] = True
    if flag_R and not flag_B:
        return True
    else:
        queue.append([nri, nrj, nbj])


def bfs(N, M, board):
    pos = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                pos.append(i)
                pos.append(j)
                board[i][j] = '.'
            elif board[i][j] == 'B':
                pos.append(i)
                pos.append(j)
                board[i][j] = '.'
    
    count = 0
    flag_RB = [False, False]
    que = deque([pos])
    while que:
        count += 1
        length = len(que)
        for _ in range(length):
            rb_pos = que.popleft()
            check_move(rb_pos, flag_RB, que, N, M, board, get_east_pos)

            nri, nrj = get_east_pos(ri, rj, M, board)
            if board[nri][nrj] != 'O':
                nrj -= 1
                flag_R = False
            else: flag_R = True
            nbi, nbj = get_east_pos(bi, bj, M, board)
            if board[nbi][nrj] != 'O':
                nbj -= 1
                flag_B = False
            else: flag_B = True
            if flag_R and not flag_B:
                return count

if __name__ == '__main__':
    main()