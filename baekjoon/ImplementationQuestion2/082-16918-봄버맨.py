import sys


def explode_bomb(time: int, board: list[list]):
    ret = [b[:] for b in board]
    r = len(board)
    c = len(board[0])
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] < time - 2:
                ret[i][j] = -1
                if i > 0: ret[i-1][j] = -1
                if i < r-1: ret[i+1][j] = -1
                if j > 0: ret[i][j-1] = -1
                if j < c-1: ret[i][j+1] = -1
    return ret

def set_bomb(time: int, board: list[list]):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == -1:
                board[i][j] = time
    return board

def print_full_bomb(R, C):
    print(('O' * C + '\n') * R, end="")

def print_board(board):
    for line in board:
        for b in line:
            if b == -1:
                print(".", end="")
            else:
                print("O", end="")
        print()


def main():
    input = sys.stdin.readline
    R, C, N = map(int, input().split())
    if N % 2 == 0:
        print_full_bomb(R, C)
        return

    board = [[-1] * C for _ in range(R)]
    for i in range(R):
        line = input().rstrip()
        for j in range(C):
            if line[j] == 'O':
                board[i][j] = 0

    if N == 1:
        print_board(board)
        return

    time = 1
    while time < N and time < 5:
        time += 1
        set_bomb(time, board)
        time += 1
        board = explode_bomb(time, board)
    mod1 = [b[:] for b in board]
    while time < N and time < 7:
        time += 1
        set_bomb(time, board)
        time += 1
        board = explode_bomb(time, board)
    mod3 = board

    if N % 4 == 1:
        print_board(mod1)
    elif N % 4 == 3:
        print_board(mod3)

if __name__ == '__main__':
    main()