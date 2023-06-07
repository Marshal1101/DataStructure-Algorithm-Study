import sys


def move_dir(N, board, dir) :
    if dir == 0 :
        for i in range(N) :
            set_up(i, N, board, i)
        
    elif dir == 1 :
        for i in range(N*N-1, N*N-N-1, -1) :
            set_down(i, N, board, i)

    elif dir == 2 :
        for i in range(0, N*N, N) :
            set_left(i, i+N, N, board, i)

    else :
        for i in range(N-1, N*N, N) :
            set_right(i, i-N, N, board, i)

    return board



def set_up(i, N, board, ptr) :
    ni = i + N
    while ni < N*N and board[ni] == 0 :
        ni += N

    if i >= N*(N-1) or ni >= N*N :
        board[ptr] = board[i]
        if ptr != i : board[i] = 0
        return

    if board[i] == board[ni] :
        board[ptr] = 2 * board[i]
        if ptr != i : board[i] = 0
        board[ni] = 0
        ptr += N
    elif board[i] != 0 :
        board[ptr] = board[i]
        if ptr != i : board[i] = 0
        ptr += N
            
    set_up(ni, N, board, ptr)


def set_down(i, N, board, ptr) :
    ni = i - N
    while ni >= 0 and board[ni] == 0 :
        ni -= N

    if i < N or ni < 0 :
        board[ptr] = board[i]
        if ptr != i : board[i] = 0
        return

    if board[i] == board[ni] :
        board[ptr] = 2 * board[i]
        if ptr != i : board[i] = 0
        board[ni] = 0
        ptr -= N
    elif board[i] != 0 :
        board[ptr] = board[i]
        if ptr != i : board[i] = 0
        ptr -= N
            
    set_down(ni, N, board, ptr)


def set_left(i, end, N, board, ptr) :
    ni = i + 1
    while ni < end and board[ni] == 0 :
        ni += 1

    if i >= end-1 or ni >= end :
        board[ptr] = board[i]
        if ptr != i : board[i] = 0
        return

    if board[i] == board[ni] :
        board[ptr] = 2 * board[i]
        if ptr != i : board[i] = 0
        board[ni] = 0
        ptr += 1
    elif board[i] != 0 :
        board[ptr] = board[i]
        if ptr != i : board[i] = 0
        ptr += 1
            
    set_left(ni, end, N, board, ptr)


def set_right(i, end, N, board, ptr) :
    ni = i - 1
    while ni >= 0 and board[ni] == 0 :
        ni -= 1

    if i <= end+1 or ni <= end :
        board[ptr] = board[i]
        if ptr != i : board[i] = 0
        return

    if board[i] == board[ni] :
        board[ptr] = 2 * board[i]
        if ptr != i : board[i] = 0
        board[ni] = 0
        ptr -= 1
    elif board[i] != 0 :
        board[ptr] = board[i]
        if ptr != i : board[i] = 0
        ptr -= 1
            
    set_right(ni, end, N, board, ptr)


def brute_force(max_num, pre_board, N, board, n) :
    if n == 10 :
        return
    # if n > 1 and pre_board == board:
        # return
    temp = max(board)
    if max_num[n] <= temp :
        max_num[n] = temp
    else:
        return

    brute_force(max_num, board, N, move_dir(N, board[:], 0), n+1)
    brute_force(max_num, board, N, move_dir(N, board[:], 1), n+1)
    brute_force(max_num, board, N, move_dir(N, board[:], 2), n+1)
    brute_force(max_num, board, N, move_dir(N, board[:], 3), n+1)


def main() :
    input = sys.stdin.readline
    N = int(input())
    T = N * N
    board = []
    for _ in range(N) :
        board += list(map(int, input().split()))

    max_num = [0] * 10
    brute_force(max_num, None, N, board, 0) 
    print(max(max_num))



if __name__ == '__main__' :
    main()