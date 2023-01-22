import sys


input = sys.stdin.readline
N = int(input())
K = int(input())

board = [[0] * N for _ in range(N)]
num = N**2
rd_end = N
lu_end = 0
i = 0
j = 0
phase = 1
ans = (-1, -1)
while num > 0:
    #1
    if phase == 1:
        while num > 0 and i < rd_end:
            board[i][j] = num
            if num == K: ans = (i+1, j+1)
            i += 1
            num -= 1
        i -= 1
        j += 1
        phase = 2
    #2
    elif phase == 2:
        while j < rd_end:
            board[i][j] = num
            if num == K: ans = (i+1, j+1)
            j += 1
            num -= 1
        j -= 1
        i -= 1
        phase = 3
    # 3
    elif phase == 3:
        while i >= lu_end:
            board[i][j] = num
            if num == K: ans = (i+1, j+1)
            i -= 1
            num -= 1
        i += 1
        j -= 1
        phase = 4
    #4
    elif phase == 4:
        while j > lu_end:
            board[i][j] = num
            if num == K: ans = (i+1, j+1)
            j -= 1
            num -= 1
        j += 1
        i += 1
        phase = 1
        rd_end -= 1
        lu_end += 1

for b in board:
    print(*b)
print(*ans)