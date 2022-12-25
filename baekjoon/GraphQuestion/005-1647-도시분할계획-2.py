import sys; 
from heapq import heappop, heappush


def prim_MST(s_node, N, graph):
    total_d = 0
    max_d = 0

    INF = sys.maxsize
    min_dist = [INF] * (N+1)
    min_dist[s_node] = 0

    spanning_tree = set()
    adj_heapq = [(0, s_node)]
    while len(spanning_tree) < N:
        cur_d, cur_node = heappop(adj_heapq)
        if cur_d > min_dist[cur_node]:
            continue
        if cur_d > max_d:
            max_d = cur_d
        
        total_d += cur_d
        spanning_tree.add(cur_node)
        for dist, adj in graph[cur_node]:
            if dist < min_dist[adj] and not adj in spanning_tree:
                min_dist[adj] = dist
                heappush(adj_heapq, (dist, adj))

    return (total_d, max_d)

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, M, P, Q = map(int, input().split())
        graph = [[] for _ in range(N)]
        hq = []
        for _ in range(M):
            u, v, w = map(int, input().split())
            graph[u].append((w, v))
            graph[v].append((w, u))

        total_dist, max_dist = prim_MST(1, N, graph)
        print(total_dist - max_dist)