import sys; input = sys.stdin.readline

def dfs(si, sj):
    visited.add((si, sj))
    stk = [(si, sj)]
    while stk:
        i, j = stk.pop()
        for di, dj in delta:
            ni = i + di
            nj = j + dj
            if (ni, nj) in visited:
                continue
            if ni < 0 or ni >= H or nj < 0 or nj >= W or graph[ni][nj] == 0:
                continue 
            stk.append((ni, nj))
            visited.add((ni, nj))

while True:
    W, H = map(int, input().split())
    if W == 0: break
    graph = [list(map(int, input().split())) for _ in range(H)]
    delta = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    visited = set()
    ans = 0
    for i in range(H):
        for j in range(W):
            if graph[i][j] == 1 and (i, j) not in visited:
                dfs(i, j)
                ans += 1

    print(ans)