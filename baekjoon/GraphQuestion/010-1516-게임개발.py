import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N + 1)
    cost = [0] * (N + 1)
    min_cost = [0] * (N + 1)
    for i in range(1, N+1):
        line = list(map(int, input().split()))
        cost[i] += line[0]
        j = 1
        while (line[j] != -1):
            indegree[i] += 1
            graph[line[j]].append(i)
            j += 1
    
    stack = []
    for i in range(1, N+1):
        if indegree[i] == 0:
            stack.append(i)
    while stack:
        cwork = stack.pop()
        min_cost[cwork] += cost[cwork]
        for adj in graph[cwork]:
            if min_cost[adj] < min_cost[cwork]:
                min_cost[adj] = min_cost[cwork]
            indegree[adj] -= 1
            if indegree[adj] == 0:
                stack.append(adj)
    
    print(*min_cost[1:], sep='\n')


if __name__ == '__main__':
    main()
