import sys

input = sys.stdin.readline
INF = sys.maxsize

def main():
    N, M = map(int, input().split())
    edges = []
    dist = [INF] * (N + 1)
    for _ in range(M):
        sv, ev, cost = map(int, input().split())
        edges.append((sv, ev, cost))
    if bellman_ford(1, N, M, edges, dist):
        for i in range(2, N+1):
            if dist[i] != INF:
                print(dist[i])
            else:
                print(-1)
    else:
        print(-1)

def bellman_ford(start, N, M, edges, dist):
    dist[start] = 0
    for i in range(N):      ## 횟수 정점N-1인데, N번차는 무한체크 
        for j in range(M):  ## 간선 체크
            cnode, adj, cost = edges[j]
            if dist[cnode] != INF and dist[cnode] + cost < dist[adj]:
                dist[adj] = dist[cnode] + cost
                if i == N-1:    ## 마지막 N번차에 변하면 무한
                    return False
                
    return True


if __name__ == '__main__':
    main()