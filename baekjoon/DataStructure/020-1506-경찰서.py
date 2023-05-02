import sys


def dfs(cur, node_id, graph, cost, stk, on_stk):
    global id, ans
    id += 1
    node_id[cur] = id
    stk.append(cur)
    on_stk[cur] = True

    asc_id = node_id[cur]
    for adj in graph[cur]:
        if not node_id[adj]:
            asc_id = min(asc_id, dfs(adj, node_id, graph, cost, stk, on_stk))
        elif on_stk[adj]:
            asc_id = min(asc_id, node_id[adj])

    if asc_id == node_id[cur]:
        min_cost = 10**6 + 1
        while stk:
            node = stk.pop()
            on_stk[node] = False
            if cost[node] < min_cost:
                min_cost = cost[node]
            if node == cur:
                break
        ans += min_cost

    return asc_id


def main():
    input = sys.stdin.readline
    N = int(input())
    cost = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    for n1 in range(1, N+1):
        for i, v in enumerate(map(int, input().rstrip())):
            if v == 1:
                n2 = i+1
                graph[n1].append(n2)

    global id, ans
    id = ans = 0
    node_id = [0] * (N+1)
    stk = []
    on_stk = [False] * (N+1)
    for i in range(1, N+1):
        if not node_id[i]:
            dfs(i, node_id, graph, cost, stk, on_stk)

    print(ans)


if __name__ == '__main__':
    main()