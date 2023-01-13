# https://www.acmicpc.net/source/53812646

import sys
input = sys.stdin.readline

answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def max_eat(x, y):
    cnt_x, cnt_y = 1, 1
    for k in range(4):
        xx, yy = x+dx[k], y+dy[k]
        while 0 <= xx < N and 0 <= yy < N and board[x][y] == board[xx][yy]:
            if k < 2:
                cnt_x += 1
            else:
                cnt_y += 1
            xx += dx[k]
            yy += dy[k]
    return max(cnt_x, cnt_y)


if __name__ == "__main__":
    N = int(input())
    board = [list(map(str, input().rstrip())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            answer = max(answer, max_eat(i, j))
            if j+1 < N and board[i][j] != board[i][j+1]:
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                answer = max(answer, max_eat(i, j))
                answer = max(answer, max_eat(i, j+1))
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            if i+1 < N and board[i][j] != board[i+1][j]:
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                answer = max(answer, max_eat(i, j))
                answer = max(answer, max_eat(i+1, j))
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
    print(answer)
