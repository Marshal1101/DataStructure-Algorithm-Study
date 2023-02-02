import sys, math


def dfs(node, p_node, adj, level, max_level, lca):
    lca[node][0] = p_node
    level[node] = level[p_node] + 1
    stack = [node]
    while stack:
        node = stack.pop()
        for child in adj[node]:
            if child != lca[node][0]:
                lca[child][0] = node
                level[child] = level[node] + 1
                for i in range(1, max_level):
                    lca[child][i] = lca[lca[child][i-1]][i-1]
                stack.append(child)



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


def main():
    input = sys.stdin.readline
    N = int(input())
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    max_level = math.ceil(math.log2(N))
    lca = [[0] * (max_level + 1) for _ in range(N+1)]
    level = [0] * (N+1)

    dfs(1, 0, adj, level, max_level, lca)

    M = int(input())
    ans = 0
    start = 1
    for _ in range(M):
        end = int(input())
        sc = LCA(start, end, level, max_level, lca)
        ans += level[start] + level[end] - 2*level[sc]
        start = end

    print(ans)



if __name__ == '__main__':
    main()