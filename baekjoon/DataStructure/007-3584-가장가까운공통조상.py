import sys, math


def LCS(a, b, level, parent):
    if level[a] < level[b]:
        temp = a
        a = b
        b = temp

    while level[a] != level[b]:
        a = parent[a]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a


def dfs(parent, child, adj, level):
    level[child] = level[parent] + 1
    for ch in adj[child]:
        level[ch] = level[child] + 1
        dfs(child, ch, adj, level)


def main():
    input = sys.stdin.readline
    T = int(input())
    for t in range(T):
        N = int(input())
        # max_h = math.ceil(math.log2(N))
        adj = [[] for _ in range(N+1)]
        level = [0] * (N+1)
        parent = [0] * (N+1)
        for _ in range(N-1):
            A, B = map(int, input().split())
            parent[B] = A
            adj[A].append(B)
            dfs(A, B, adj, level)
        a, b = map(int, input().split())
        print(LCS(a, b, level, parent))


if __name__ == '__main__':
    main()