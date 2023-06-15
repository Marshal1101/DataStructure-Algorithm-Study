import sys

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        graph = [set() for _ in range(N+1)]
        indegree = [0] * (N+1)
        rank = [*map(int, input().split())]
        for i in range(N):
            adj_list = rank[i+1:]
            for ele in adj_list:
                indegree[ele] += 1
            graph[rank[i]].update(adj_list)

        # print(graph)
        M = int(input())
        for _ in range(M):
            t1, t2 = map(int, input().split())
            if t1 in graph[t2]:
                graph[t2].remove(t1)
                indegree[t1] -= 1
                graph[t1].add(t2)
                indegree[t2] += 1
            elif t2 in graph[t1]:
                graph[t1].remove(t2)
                indegree[t2] -= 1
                graph[t2].add(t1)
                indegree[t1] += 1
        
        stack = []
        for i in range(1, N+1):
            if indegree[i] == 0:
                stack.append(i)

        result = []
        while stack:
            if len(stack) > 2:
                print("?")
                return
            cur_t = stack.pop()
            result.append(cur_t)
            for adj_t in graph[cur_t]:
                indegree[adj_t] -= 1
                if indegree[adj_t] == 0:
                    stack.append(adj_t)
        if len(result) == N:
            print(*result)
        else:
            print("IMPOSSIBLE")

if __name__ == '__main__':
    main()