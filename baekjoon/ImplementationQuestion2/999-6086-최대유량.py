import sys


def recur(node, graph):
    if node == 25:
        return 1001

    fluid = -1
    for d, adj in graph[node]:
        ret = recur(adj, graph)
        if ret != 0:
            fluid += min(d, ret)
    return fluid + 1


def main():
    input = sys.stdin.readline
    N = int(input())
    graph = [[] for _ in range(52)]
    for _ in range(N):
        v1, v2, d = input().split()
        v1 = ord(v1) - 65
        v2 = ord(v2) - 65
        if v1 > 25:
            v1 = v1 - 6
        if v2 > 25:
            v2 = v2 - 6
        for _, v in graph[v2]:
            if v == v1:
                break
        else:
            graph[v1].append((int(d), v2))

    print(recur(0, graph))


if __name__ == '__main__':
    main()