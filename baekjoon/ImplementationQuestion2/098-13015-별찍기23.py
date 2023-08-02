N = int(input())
R = 2*N - 1
C = 4*N - 3
board = [[' '] * C for _ in range(R)]
for j in range(N):
    board[0][j] = board[R-1][j] = '*'

for j in range(C-1, C-1-N, -1):
    board[0][j] = board[R-1][j] = '*'

for j in range(1, N):
    board[j][j] = board[j][j+N-1] = '*'
    board[j][C-1-j] = board[j][C-j-N] = '*'
    board[R-1-j][j] = board[R-1-j][j+N-1] = '*'
    board[R-1-j][C-1-j] = board[R-1-j][C-j-N] = '*'

for i in range(R):
    for j in range(C-1, -1, -1):
        if board[i][j] == ' ':
            board[i][j] = ''
        else:
            break

for b in board:
    print(*b, sep='')