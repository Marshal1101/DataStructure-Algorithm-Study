import sys, math
from collections import defaultdict


def LCA2(a, b, k, level, max_level, lca, dist):
    na = a
    nb = b
    if level[na] < level[nb]:
        temp = na
        na = nb
        nb = temp


    if level[na] != level[nb]:
        for i in range(max_level-1, -1, -1):
            if level[lca[na][i]] >= level[nb]:
                na = lca[na][i]
    if na == nb:
        anc = na
    else:
        for i in range(max_level-1, -1, -1):
            if lca[na][i] != lca[nb][i]:
                na = lca[na][i]
                nb = lca[nb][i]
            anc = lca[na][i]

    if k <= level[a] - level[anc]:
        diff = k - 1
        for i in range(max_level):
            if diff & 1 << i:
                a = lca[a][i]
        return a
    else:
        diff = level[a] + level[b] - 2 * level[anc] - k + 1
        for i in range(max_level):
            if diff & 1 << i:
                b = lca[b][i]
        return b



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
    max_level = math.ceil(math.log2(N)) + 1
    lca = [[0] * max_level for _ in range(N+1)]

    dfs(1, 0, graph, parent, level, max_level, lca, dist)

    M = int(input())
    for _ in range(M):
        query = list(map(int, input().split()))
        if query[0] == 1:
            print(LCA(query[1], query[2], level, max_level, lca, dist))
        else:
            print(LCA2(query[1], query[2], query[3], level, max_level, lca, dist))


if __name__ == '__main__':
    main()