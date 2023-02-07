# https://www.acmicpc.net/source/48203123

import sys

input = sys.stdin.readline
INF = 10 ** 9


def sol4991():
    answer = []

    def bfs(sr, sc):
        nonlocal n
        nonlocal m

        visited = [[False] * m for _ in range(n)]
        q = [(sr, sc)]
        visited[sr][sc] = True
        dst = 0
        start = board[sr][sc]
        while q:
            dst += 1
            nq = []
            for r, c in q:
                if r > 0:
                    nr, nc = r - 1, c
                    if board[nr][nc] != 'x' and not visited[nr][nc]:
                        visited[nr][nc] = True
                        if board[nr][nc] != '.':
                            g[start].append((board[nr][nc], dst))
                        nq.append((nr, nc))
                if r < n - 1:
                    nr, nc = r + 1, c
                    if board[nr][nc] != 'x' and not visited[nr][nc]:
                        visited[nr][nc] = True
                        if board[nr][nc] != '.':
                            g[start].append((board[nr][nc], dst))
                        nq.append((nr, nc))
                if c > 0:
                    nr, nc = r, c - 1
                    if board[nr][nc] != 'x' and not visited[nr][nc]:
                        visited[nr][nc] = True
                        if board[nr][nc] != '.':
                            g[start].append((board[nr][nc], dst))
                        nq.append((nr, nc))
                if c < m - 1:
                    nr, nc = r, c + 1
                    if board[nr][nc] != 'x' and not visited[nr][nc]:
                        visited[nr][nc] = True
                        if board[nr][nc] != '.':
                            g[start].append((board[nr][nc], dst))
                        nq.append((nr, nc))
            q = nq

    def dfs(cur, state):
        nonlocal full_visit
        nonlocal dn
        if state == full_visit:
            return 0

        if dp[cur][state] == -1:
            res = INF
            for nxt, dst in g[cur]:
                if state & (1 << nxt):
                    continue
                dist = dfs(nxt, state | (1 << nxt)) + dst
                if dist != -1:
                    res = min(res, dist)
            dp[cur][state] = res if res != INF else -1

        return dp[cur][state]

    while True:
        m, n = map(int, input().split())
        if n == m == 0:
            break
        board = [list(input().rstrip()) for _ in range(n)]
        cr, cc = 0, 0
        dusts = []
        dn = 1
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'o':
                    cr, cc = i, j
                    board[i][j] = 0
                elif board[i][j] == '*':
                    dusts.append((i, j))
                    board[i][j] = dn
                    dn += 1
        g = [[] for _ in range(dn)]
        bfs(cr, cc)
        for dr, dc in dusts:
            bfs(dr, dc)

        if len(g[0]) != len(dusts):
            answer.append(-1)
            continue

        full_visit = (1 << dn) - 1
        dp = [[-1] * full_visit for _ in range(dn)]
        answer.append(dfs(0, 1))

    return '\n'.join(map(str, answer))


if __name__ == '__main__':
    print(sol4991())