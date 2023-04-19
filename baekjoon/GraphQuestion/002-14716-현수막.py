import sys; input = sys.stdin.readline

def dfs(si, sj, graph, delta, visited):
    visited.add((si, sj))
    stk = [(si, sj)]
    while stk:
        i, j = stk.pop()
        for di, dj in delta:
            ni = i + di
            nj = j + dj
            if (ni, nj) in visited:
                continue
            if ni < 0 or ni >= M or nj < 0 or nj >= N or graph[ni][nj] == 0:
                continue 
            stk.append((ni, nj))
            visited.add((ni, nj))


M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
delta = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
visited = set()
ans = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1 and (i, j) not in visited:
            dfs(i, j, graph, delta, visited)
            ans += 1

print(ans)