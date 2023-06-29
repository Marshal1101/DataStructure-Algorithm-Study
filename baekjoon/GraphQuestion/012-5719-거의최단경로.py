import sys
from heapq import heappush, heappop


def dijkstra_2nd(start, end):
    INF = sys.maxsize
    min_w = [INF] * (N)
    from_v = [set() for _ in range(N)]
    min_w[start] = 0
    hq = [(0, start)]
    while hq:
        pre_w, node = heappop(hq)
        if pre_w > min_w[node]:
            continue
        for adj in graph[node]:
            exp_w = pre_w + graph[node][adj]
            if exp_w < min_w[adj]:
                min_w[adj] = exp_w
                from_v[adj] = {node}
                heappush(hq, (exp_w, adj))
            elif exp_w == min_w[adj]:
                from_v[adj].add(node)

    stk = [end]
    while stk:
        new_stk = []
        while stk:
            node = stk.pop()
            for prev in from_v[node]:
                if node in graph[prev]:
                    del graph[prev][node]
                else:
                    break
                new_stk.append(prev)
            stk = new_stk

    min_w = [INF] * (N)
    min_w[start] = 0
    hq = [(0, start)]
    while hq:
        pre_w, node = heappop(hq)
        if pre_w > min_w[node]:
            continue
        for adj in graph[node]:
            exp_w = pre_w + graph[node][adj]
            if exp_w < min_w[adj]:
                min_w[adj] = exp_w
                heappush(hq, (exp_w, adj))

    print(min_w[end] if min_w[end] < INF else -1)


input = sys.stdin.readline
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0: break
    S, E = map(int, input().split())
    graph = [dict() for _ in range(N)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u][v] = w
    dijkstra_2nd(S, E)
