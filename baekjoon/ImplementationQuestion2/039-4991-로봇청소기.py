import sys
from collections import deque
from itertools import permutations

def bfs(si, sj, N, M, board, dist):
    if board[si][sj] == 'o': idx = 0
    else: idx = board[si][sj]
    board[si][sj] = 0
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque([(si, sj, 0)])
    while queue:
        i, j, time = queue.popleft()
        for d in range(4):
            ni = i + delta[d][0]
            nj = j + delta[d][1]
            if ni < 0 or ni >= N or nj < 0 or nj >= M or board[ni][nj] == 'x': continue
            if board[ni][nj] != 0:
                if board[ni][nj] == '.':
                    queue.append((ni, nj, time+1))
                elif board[ni][nj] == 'o':
                    dist[0] = time + 1
                    queue.append((ni, nj, time+1))
                else:
                    dist[board[ni][nj]] = time + 1
                    queue.append((ni, nj, time+1))
                board[ni][nj] = 0

    for i in range(len(dist)):
        if i != idx and dist[i] == 0:
            return False
    
    return True


def main():
    input = sys.stdin.readline
    while (temp := list(map(int, input().split()))) != [0, 0]:
        M, N = temp
        board = [list(input().rstrip()) for _ in range(N)]
        cnt = 0
        s_arr = []
        si = sj = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 'x' or board[i][j] == '.':
                    continue

                if board[i][j] == '*':
                    cnt += 1
                    board[i][j] = cnt
                    s_arr.append((i, j))

                elif board[i][j] == 'o': 
                    si = i
                    sj = j

        dist = [[0] * (cnt+1) for _ in range(cnt+1)]
        if not bfs(si, sj, N, M, [b[:] for b in board], dist[0]):
            print(-1)
        else:
            for i, j in s_arr:
                bfs(i, j, N, M, [b[:] for b in board], dist[board[i][j]])

            min_d = sys.maxsize
            if cnt > 0:
                for order in permutations(range(1, cnt+1), cnt):
                    d = 0
                    for k in range(1, cnt):
                        d += dist[order[k]][order[k-1]]
                    d += dist[0][order[0]]
                    if d < min_d:
                        min_d = d
            else:
                min_d = 0

            print(min_d)


if __name__ == '__main__':
    main()