import sys
sys.setrecursionlimit(10**9)


def scc_dfs(cur, node_id, graph, stk, on_stk):
    global ans, id
    id += 1
    node_id[cur] = id
    stk.append(cur)
    on_stk[cur] = True

    asc_id = node_id[cur]
    for adj in graph[cur]:
        if not node_id[adj]:
            asc_id = min(asc_id, scc_dfs(adj, node_id, graph, stk, on_stk))
        elif on_stk[adj]:
            asc_id = min(asc_id, node_id[adj])

    if asc_id == node_id[cur]:
        cnt = 0
        while stk:
            node = stk.pop()
            on_stk[node] = False
            cnt += 1
            if node == cur:
                break
        if cnt > ans:
            ans = cnt

    return asc_id


def main():
    input = sys.stdin.readline
    D = int(input())
    L = int(input())
    graph = [[] for _ in range(D+1)]
    for _ in range(L):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)

    global ans, id
    ans = 0
    id = 0
    stk = []
    on_stk = [False] * (D+1)
    node_id = [0] * (D+1)
    for i in range(1, D+1):
        if not node_id[i]:
            scc_dfs(i, node_id, graph, stk, on_stk)

    print(ans)


if __name__ == '__main__':
    main()