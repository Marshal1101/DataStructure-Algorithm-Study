def solution(n, s, a, b, fares):
    # 대각선의 값이 0인 행렬 만들기
    graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        graph[i][i] = 0     

    # 요금 추가한 행렬 만들기
    for fare in fares:
        nodeA, nodeB, taxi_fare = fare
        graph[nodeA][nodeB] = graph[nodeB][nodeA] = taxi_fare
    for i in graph:
        print(i)
    
    # 행렬 갱신하기
    for k in range(1, n + 1):          
        for i in range(1, n + 1):      
            for j in range(1, n + 1):  
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    print()
    for i in graph:
        print(i)
        
    # 출발점을 기준으로 어떤 지점 k를 거쳐 각각 a와 b로 가는 최소 비용을 탐색
    ans = float('inf')
    for k in range(n + 1):
        ans = min(ans, graph[s][k] + graph[k][a] + graph[k][b])

    return ans

########################################################

from collections import defaultdict
import heapq

def solution(n, s, a, b, fares):
    # 그래프를 만든다.
    graph = defaultdict(list)
    for nodeA, nodeB, fare in fares :
        graph[nodeA].append([nodeB, fare])
        graph[nodeB].append([nodeA, fare])
    # print(graph) : ({4: [[1, 10], [6, 50], [2, 66]]})
    
    # n개의 node 별 요금을 확인한다.
    taxi_fares = [[] for _ in range(n + 1)]
    for node in range(1, n + 1):
        taxi_fares[node] = DIJKSTRA(graph, node, n)
    # print(taxi_fares) : 1번의 경우 [inf, 0, 63, 41, 10, 24, 25]
    
    # 최소 택시 요금을 갱신한다.
    min_taxi_fare = float('inf')
    for i in range(1, n + 1) :
        new_taxi_fare = taxi_fares[s][i] + taxi_fares[i][a] + taxi_fares[i][b]
        min_taxi_fare = min(min_taxi_fare, new_taxi_fare)
    return min_taxi_fare


def DIJKSTRA(graph, node, n):
    # print(start, n) : 1, 6
    cost = [float('inf')] * (n + 1)
    cost[node] = 0

    heap = []
    heapq.heappush(heap, [0, node])
    while heap:
        cur_cost, cur_node = heapq.heappop(heap)
        # 0, 1
        if cost[cur_node] < cur_cost:
            continue

        cost[cur_node] = cur_cost
        for adj_node, adj_cost in graph[cur_node]:
            if cost[adj_node] > cost[cur_node] + adj_cost:
                cost[adj_node] = cost[cur_node] + adj_cost
                heapq.heappush(heap, [cost[adj_node], adj_node])
    
    return cost