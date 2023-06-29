import sys
import math
input = sys.stdin.readline
INF = math.inf

for _ in range(int(input())):
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    knapsack = [[INF]*(M+1) for _ in range(N+1)]
    knapsack[1][0] = 0 # 출발 노드의 최단 시간 값 0으로 초기화
    
    for _ in range(K):
        u, v, c, d = map(int, input().split())
        graph[u].append((v, c, d))
    
    # 비용 0부터 시작하여 1씩 올리면서, 비용 K를 사용했을 때(column)
    # 어떤 노드(row)까지 도달하는 최단 시간 값이 존재하고 있다면(not INF),
    # 그 노드의 인접 노드들의 최단 시간 값을 비교&갱신해준다.
    for cost in range(M+1):
        for city in range(1, N+1):
            if knapsack[city][cost] != INF:
                for adjacency_city, c, d in graph[city]:
                    cal_d = knapsack[city][cost] + d
                    cal_c = cost + c
                    
                    # 인접 노드로 이동하고 난 비용이 M 이하여야함.
                    if cal_c <= M and cal_d < knapsack[adjacency_city][cal_c]:
                        knapsack[adjacency_city][cal_c] = cal_d
    
    # 비용 0을 사용하여 N으로 가는 최단 시간, 비용 1을 사용하여, ..., 이들 중
    # 최소인 값을 채택하여 답으로 확정
    result = min(knapsack[N])
    
    if result == INF:
        print("Poor KCM")
    else:
        print(result)