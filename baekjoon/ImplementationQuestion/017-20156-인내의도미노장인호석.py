import sys



def dir_to_delta(dir: str) -> tuple:
    if dir == 'E': return (0, 1)
    elif dir == 'W': return (0, -1)
    elif dir == 'S': return (1, 0)
    elif dir == 'N': return (-1, 0)


def renew_dest(dir: str, old_d: tuple, new_d: tuple):
    if dir == 'E':
        if old_d[1] < new_d[1]: return new_d
        else: return old_d
    elif dir == 'W':
        if old_d[1] > new_d[1]: return new_d
        else: return old_d
    elif dir == 'S':
        if old_d[0] < new_d[0]: return new_d
        else: return old_d
    elif dir == 'N':
        if old_d[0] > new_d[0]: return new_d
        else: return old_d


def check_dest(si, sj, dir: str, N, M, board) -> tuple:
    if dir == 'E':
        ei = si
        ej = sj + board[si][sj]
        if ej > M: ej = M
    elif dir == 'W':
        ei = si
        ej = sj - board[si][sj]
        if ej < 0: sj = -1
    elif dir == 'S':
        ei = si + board[si][sj]
        ej = sj
        if ei > N: ei = N
    elif dir == 'N':
        ei = si - board[si][sj]
        ej = sj
        if ei < 0: ei = -1
    return (ei, ej)


def domino_down(i, j, dest, dir, N, M, board, state):
    if 0 <= i < N and 0 <= j < M and (i != dest[0] or j != dest[1]):
        global point
        if state[i][j] == "S":
            state[i][j] = "F"
            point += 1
            dest = renew_dest(dir, dest, check_dest(i, j, dir, N, M, board))
        di, dj = dir_to_delta(dir)
        domino_down(i+di, j+dj, dest, dir, N, M, board, state)


def domino_attck(i, j, dir, N, M, board, state):
    global point
    if state[i][j] == "S":
        state[i][j] = "F"
        point += 1
        di, dj = dir_to_delta(dir)
        dest = check_dest(i, j, dir, N, M, board)
        domino_down(i+di, j+dj, dest, dir, N, M, board, state)


def domino_defence(i, j, N, M, state):
    if 0 <= i < N and 0 <= j < M:
        state[i][j] = "S"


def play_game(N, M, R, board, command):
    global point
    point = 0
    state = [["S"] * M for _ in range(N)]
    for r in range(0, 2*R, 2):
        fi, fj, dir = command[r]
        di, dj = command[r+1]
        domino_attck(int(fi)-1, int(fj)-1, dir, N, M, board, state)
        domino_defence(int(di)-1, int(dj)-1, N, M, state)
    print(point)
    for i in range(N):
        print(" ".join(state[i]))

def main():
    input = sys.stdin.readline
    N, M, R = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    command = [input().split() for _ in range(2*R)]
    play_game(N, M, R, board, command)


if __name__=='__main__':
    main()