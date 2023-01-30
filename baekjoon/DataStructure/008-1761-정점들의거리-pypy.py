import sys


def LCS(a, b, parent, level):
    dist = 0

    if level[a] < level[b]:
        temp = a
        a = b
        b = temp

    while level[a] != level[b]:
        dist += parent[a][1]
        a = parent[a][0]

    while a != b:
        dist += parent[a][1]
        a = parent[a][0]
        dist += parent[b][1]
        b = parent[b][0]

    return dist


def init_tree(node, p_node, graph, parent, level):
    parent[node][0] = p_node
    level[node] = level[p_node] + 1
    stack = [node]
    while stack:
        n = stack.pop()
        for adj, d in graph[n]:
            if adj != parent[n][0]:
                parent[adj][0] = n
                parent[adj][1] = d
                level[adj] = level[n] + 1
                stack.append(adj)


def main():
    input = sys.stdin.readline
    N = int(input())
    graph = [[] for _ in range(N+1)]
    parent = [[0, 0] for _ in range(N+1)]
    level = [0] * (N+1)
    for _ in range(N-1):
        v1, v2, d = map(int, input().split())
        graph[v1].append((v2, d))
        graph[v2].append((v1, d))
    init_tree(1, 0, graph, parent, level)
    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        print(LCS(a, b, parent, level))


if __name__ == '__main__':
    main()