import sys
from heapq import heappop, heappush


def main():
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    hq = [(0, 1)]
    visited = [False] * (N+1)
    total = cnt = 0
    while cnt < N:
        dist, node = heappop(hq)
        if not visited[node]:
            visited[node] = True
            total += dist
            cnt += 1
            for adj, dist in graph[node]:
                if not visited[adj]:
                    heappush(hq, (dist, adj))
    print(total)


if __name__ == '__main__':
    main()