import sys

input = sys.stdin.readline

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
turned = [
    (3, 1, 0, 5, 4, 2),
    (1, 5, 2, 3, 0, 4),
    (2, 1, 5, 0, 4, 3),
    (4, 0, 2, 3, 5, 1)
]

def solution():
    N, M, K = map(int, input().split())
    board = [tuple(map(int, input().split())) for _ in range(N)]
    scores = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if scores[i][j] == 0:
                scores[i][j] = 1
                queue = [(i, j)]
                temp = [(i, j)]
                while queue:
                    r, c = queue.pop(0)
                    for dr, dc in delta:
                        nr, nc = r+dr, c+dc
                        if N > nr >= 0 and M > nc >= 0:
                            if scores[nr][nc] == 0 and board[nr][nc] == board[r][c]:
                                scores[nr][nc] = 1
                                queue.append((nr, nc))
                                temp.append((nr, nc))
                score = board[i][j]*len(temp)
                for r, c in temp:
                    scores[r][c] = score
    dice = [1, 2, 3, 4, 5, 6]
    res = d = r = c = 0
    for _ in range(K):
        dr, dc = delta[d]
        nr, nc = r+dr, c+dc
        if N > nr >= 0 and M > nc >= 0:
            r, c = nr, nc
        else:
            d = (d+2)%4
            dr, dc = delta[d]
            r, c = r+dr, c+dc
        res += scores[r][c]
        temp = [0]*6
        for i in range(6):
            temp[i] = dice[turned[d][i]]
        dice = temp
        if dice[5] > board[r][c]:
            d = (d+1)%4
        elif dice[5] < board[r][c]:
            d = (d+3)%4
    print(res)

solution()