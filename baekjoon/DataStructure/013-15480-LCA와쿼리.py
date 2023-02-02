import sys, math


def LCA(n1, n2, level, max_level, lca):

    if level[n1] < level[n2]:
        n1, n2 = n2, n1

    if level[n1] != level[n2]:
        for i in range(max_level-1, -1, -1):
            if level[lca[n1][i]] >= level[n2]:
                n1 = lca[n1][i]

    if n1 == n2: return n1

    for i in range(max_level-1, -1, -1):
        if lca[n1][i] != lca[n2][i]:
            n1 = lca[n1][i]
            n2 = lca[n2][i]

    return lca[n1][0]


def dfs(node, p_node, adj, level, max_level, lca):
    lca[node][0] = p_node
    level[node] = level[p_node] + 1

    stack = [node]
    while stack:
        node = stack.pop()
        for child in adj[node]:
            if child != lca[node][0]:
                level[child] = level[node] + 1
                lca[child][0] = node
                for i in range(1, max_level):
                    lca[child][i] = lca[lca[child][i-1]][i-1]
                stack.append(child)


def main():
    input = sys.stdin.readline
    N = int(input())
    max_level = math.ceil(math.log2(N))
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        n1, n2 = map(int, input().split())
        adj[n1].append(n2)
        adj[n2].append(n1)

    level = [0] * (N+1)
    lca = [[0] * max_level for _ in range(N+1)]


    dfs(1, 0, adj, level, max_level, lca)
    
    M = int(input())
    for _ in range(M):
        r, u, v = map(int, input().split())
        ru = LCA(r, u, level, max_level, lca)
        rv = LCA(r, v, level, max_level, lca)
        uv = LCA(u, v, level, max_level, lca)

        if level[ru] > level[rv]: ans = ru
        else: ans = rv
        if level[ans] < level[uv]: ans = uv

        print(ans)


if __name__ == '__main__':
    main()