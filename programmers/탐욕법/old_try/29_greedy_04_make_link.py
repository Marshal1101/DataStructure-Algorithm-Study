## 그리디 - 섬 연결하기()


from collections import defaultdict, deque

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

def solution(n, costs):
    graph = [[float('inf') for _ in range(n)] for _ in range(n)]
    for case in costs :
        v1, v2, cost = case
        graph[v1][v2] = cost
        graph[v2][v1] = cost
    
    def BFS(start) :
        min_cost = float('inf')
        visited = [False] * n
        visited[start] = True
        level = 0
        tot_cost = 0
        queue = deque([(start, level, tot_cost)])
        while queue :
            vertex, level, tot_cost = queue.popleft()
            if level == n :
                return tot_cost
                min(graph[vertex])
            for edge, cost in graph[vertex] :
                tot_cost += cost
                if not visited[edge] :
                    visited[edge] = True
                    queue.append((edge, level+1, tot_cost))
        
        return tot_cost

    min_cost = float('inf')
    for i in range(n) :
        tot_cost = BFS(i)
        if min_cost > tot_cost :
            min_cost = tot_cost

    return min_cost

print(solution(n, costs))



# def solution(n, costs):
#     graph = [[-1 for _ in range(n)] for _ in range(n)]
#     print(graph)
#     for case in costs :
#         v1, v2, cost = case
#         graph[v1][v2] = cost
#         graph[v2][v1] = cost
    
#     def BFS(start) :
#         graph[start][start] = 0
#         queue = deque([start])

#         while queue :
#             vertex = queue.popleft()
#             for i in range(vertex, n) :
#                 graph[vertex][i]



#     answer = 0

#     return answer

# solution(n, costs)