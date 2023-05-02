import sys
sys.setrecursionlimit(10**9)

def scc_dfs(cur, node_id, graph, stk, on_stk, ret):
    global id, ans
    id += 1
    node_id[cur] = id
    stk.append(cur)
    on_stk[cur] = True

    asc_id = node_id[cur]
    for adj in graph[cur]:
        if not node_id[adj]:
            asc_id = min(asc_id, scc_dfs(adj, node_id, graph, stk, on_stk, ret))
        elif on_stk[adj]:
            asc_id = min(asc_id, node_id[adj])
        elif node_id[adj] in ans:
            ans.remove(node_id[adj])


    if asc_id == node_id[cur]:
        while stk:
            node = stk.pop()
            node_id[node] = asc_id
            on_stk[node] = False
            if node == cur:
                break
        ret.append(asc_id)

    return asc_id


def main():
    global id, ans
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        graph = [[] for _ in range(N+1)]
        for _ in range(M):
            a, b = map(int, input().split())
            graph[a].append(b)

        id = 0
        ans = set()
        ret = []
        stk = []
        on_stk = [False] * (N+1)
        node_id = [0] * (N+1)
        for i in range(1, N+1):
            if not node_id[i]:
                scc_dfs(i, node_id, graph, stk, on_stk, ret)
                ans.add(ret[-1])
                ret.clear()
        
        print(len(ans))


if __name__ == '__main__':
    main()