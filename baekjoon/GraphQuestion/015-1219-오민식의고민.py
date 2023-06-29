import sys

input = sys.stdin.readline
INF = sys.maxsize

def main():
    edges = []
    N, start, end, M = map(int, input().split())
    for _ in range(M):
        v, u, cost = map(int, input().split())
        edges.append((v, u, cost))
    earn = [*map(int, input().split())]
    total = [-INF] * N
    bellman_ford(start, N, M, edges, earn, total)
    if total[end] == -INF:
        print("gg")
    elif total[end] == INF:
        print("Gee")
    else:
        print(total[end])


def bellman_ford(start, N, M, edges, earn, dist):
    dist[start] = earn[start]
    for i in range(N+100):      
        for j in range(M):  
            cnode, adj, cost = edges[j]
            if dist[cnode] == INF: dist[adj] = INF
            elif dist[cnode] != -INF and dist[cnode] - cost + earn[adj] > dist[adj]:
                dist[adj] = dist[cnode] - cost + earn[adj]
                if i >= N-1:    
                    dist[adj] = INF


if __name__ == '__main__':
    main()