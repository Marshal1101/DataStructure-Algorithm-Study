import sys
from collections import deque
from itertools import permutations

def bfs(si, sj, N, M, board, dist):
    board[si][sj] = 0
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque([(si, sj, 0)])
    while queue:
        i, j, time = queue.popleft()
        for d in range(4):
            ni = i + delta[d][0]
            nj = j + delta[d][1]
            if ni < 0 or ni >= N or nj < 0 or nj >= M or board[ni][nj] == '#': continue
            if board[ni][nj] != 0:
                if board[ni][nj] == '.':
                    queue.append((ni, nj, time+1))
                elif board[ni][nj] == 'E':
                    dist[-1] = time + 1
                elif board[ni][nj] == 'S':
                    dist[0] = time + 1
                    queue.append((ni, nj, time+1))
                else:
                    dist[board[ni][nj]] = time + 1
                    queue.append((ni, nj, time+1))
                board[ni][nj] = 0


def main():
    input = sys.stdin.readline
    M, N = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]
    cnt = 0
    s_arr = []
    si = sj = ei = ej = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == '#' or board[i][j] == '.':
                continue

            if board[i][j] == 'X':
                cnt += 1
                board[i][j] = cnt
                s_arr.append((i, j))

            elif board[i][j] == 'S': 
                si = i
                sj = j

            elif board[i][j] == 'E':
                ei = i
                ej = j

    dist = [[0] * (cnt+2) for _ in range(cnt+2)]
    bfs(si, sj, N, M, [b[:] for b in board], dist[0])
    bfs(ei, ej, N, M, [b[:] for b in board], dist[cnt+1])
    for i, j in s_arr:
        bfs(i, j, N, M, [b[:] for b in board], dist[board[i][j]])

    min_d = sys.maxsize
    if cnt > 0:
        for order in permutations(range(1, cnt+1), cnt):
            d = 0
            for k in range(1, cnt):
                d += dist[order[k]][order[k-1]]
            d += dist[0][order[0]]
            d += dist[cnt+1][order[-1]]
            if d < min_d:
                min_d = d
    else:
        min_d = dist[0][1]

    print(min_d)


if __name__ == '__main__':
    main()