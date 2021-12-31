## 그래프 - 가장 먼 노드 (구현)

from collections import deque, defaultdict

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

def solution(n, vertex):
  
    def BFS(start, edge) :
        visited = [False] * (n+1)
        distance = defaultdict(list)
        level = 0
        visited[start] = True
        queue = deque([(start, level)])
        distance[level].append(start)
        while queue :
            v, level = queue.popleft()
            for e in edge[v] :
                if not visited[e] :
                    visited[e] = True
                    queue.append((e, level+1))
                    distance[level+1].append(e)
        return len(distance[level])

    edge = [[] for _ in range(n+1)]
    for ver in vertex :
        v1, v2 = ver
        edge[v1].append(v2)
        edge[v2].append(v1)
    return BFS(1, edge)

print(solution(n, vertex))