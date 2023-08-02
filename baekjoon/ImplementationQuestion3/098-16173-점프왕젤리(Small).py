def main():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    if jump(N, board):
        print("HaruHaru")
    else:
        print("Hing")
    
def jump(N, board):
    stk = [(0, 0)]
    while stk:
        i, j = stk.pop()
        if board[i][j] == 0:
            continue
        nj = j + board[i][j]
        ni = i + board[i][j]
        if nj < N:
            if i == N-1 and nj == N-1:
                return True
            stk.append((i, nj))
        if ni < N:
            if ni == N-1 and j == N-1:
                return True
            stk.append((ni, j))
    return False


if __name__ == '__main__':
    main()