import sys, math
from collections import defaultdict

def LCA(a, b, level, max_level, lca, dist):
    if level[a] < level[b]:
        temp = a
        a = b
        b = temp

    na = a
    nb = b

    d = 0
    if level[na] != level[nb]:
        for i in range(max_level-1, -1, -1):
            if level[lca[na][i]] >= level[nb]:
                d += dist[na][lca[na][i]]
                na = lca[na][i]
    if na == nb:
        return d

    for i in range(max_level-1, -1, -1):
        if lca[na][i] != lca[nb][i]:
            d += dist[na][lca[na][i]]
            na = lca[na][i]
            d += dist[nb][lca[nb][i]]
            nb = lca[nb][i]
    
    d += dist[na][lca[na][0]]
    d += dist[nb][lca[nb][0]]

    return d


def dfs(node, p_node, graph, parent, level, max_level, lca, dist):
    parent[node] = p_node
    level[node] = level[p_node] + 1
    lca[node][0] = p_node
    stack = [node]
    while stack:
        node = stack.pop()
        for v in graph[node]:
            if v != parent[node]:
                parent[v] = node
                level[v] = level[node] + 1
                lca[v][0] = node
                for i in range(1, max_level):
                    lca[v][i] = lca[lca[v][i-1]][i-1]
                    dist[lca[v][i]][v] += dist[lca[v][i-1]][v] + dist[lca[v][i-1]][lca[v][i]]
                    dist[v][lca[v][i]] += dist[lca[v][i-1]][v] + dist[lca[v][i-1]][lca[v][i]]
                stack.append(v)

def main():
    input = sys.stdin.readline
    N = int(input())
    graph = [[] for _ in range(N+1)]
    dist = [defaultdict(int) for _ in range(N+1)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        dist[u][v] = w
        dist[v][u] = w
        graph[u].append(v)
        graph[v].append(u)

    parent = [0] * (N+1)
    level = [0] * (N+1)
    max_level = math.ceil(math.log2(N))
    lca = [[0] * max_level for _ in range(N+1)]

    dfs(1, 0, graph, parent, level, max_level, lca, dist)

    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        print(LCA(a, b, level, max_level, lca, dist))


if __name__ == '__main__':
    main()