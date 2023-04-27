import sys


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for i, node in enumerate(map(int, input().split())):
        graph[i+1].append(node)
        graph[node].append(i+1)

    level = [0] * (N+1)
    parent = [0] * (N+1)
    set_tree(0, 0, graph, parent, level)

    arr = list(map(int, input().split()))
    c = LCA(arr[0], arr[1], parent, level)
    for i in range(2, M):
        c = LCA(c, arr[i], parent, level)
    print(c)


def LCA(a, b, parent, level):
    # a를 레벨이 더 높은 정점으로 맞춘다.
    if level[a] < level[b]:
        temp = a
        a = b
        b = temp

    # a의 레벨이 b와 같아질 때까지 a가 올라간다.
    while level[a] != level[b]:
        a = parent[a]

    # a, b의 정점이 같아질 때까지 올라간다.
    while a != b:
        a = parent[a]
        b = parent[b]

    return a


def set_tree(node, p_node, graph, parent, level):
    parent[node] = p_node
    level[node] = level[p_node] + 1
    stack = [node]
    while stack:
        node = stack.pop()
        for adj in graph[node]:
            if adj != parent[node]:
                parent[adj] = node
                level[adj] = level[node] + 1
                stack.append(adj)


if __name__ == '__main__':
    main()