import sys


def scc_dfs(cur, node_id, graph, prob, stk, on_stk, ret):
    global id, ans
    id += 1
    node_id[cur] = id
    stk.append(cur)
    on_stk[cur] = True

    asc_id = node_id[cur]
    for adj in graph[cur]:
        if not node_id[adj]:
            asc_id = min(asc_id, scc_dfs(adj, node_id, graph, prob, stk, on_stk, ret))
        elif on_stk[adj]:
            asc_id = min(asc_id, node_id[adj])
        elif node_id[adj] in ans:
            del ans[node_id[adj]]

    if asc_id == node_id[cur]:
        scc_prob = 1
        while stk:
            node = stk.pop()
            node_id[node] = asc_id
            scc_prob *= prob[node]
            on_stk[node] = False
            if node == cur:
                break
        ret.append((asc_id, 1-scc_prob))


    return asc_id


def main():
    global id, ans
    input = sys.stdin.readline
    while (N := int(input())) != 0:
        id = 0
        ret = []
        stk = []
        on_stk = [False] * (N+1)
        node_id = [0] * (N+1)
        graph = [[] for _ in range(N+1)]
        prob = [None] * (N+1)
        for n1 in range(1, N+1):
            line = input().split()
            prob[n1] = float(line[0])
            adj_cnt = int(line[1])
            if adj_cnt > 0:
                for i in range(adj_cnt):
                    n2 = int(line[2+i])
                    graph[n1].append(n2)

        ans = dict()
        for i in range(1, N+1):
            if not node_id[i]:
                scc_dfs(i, node_id, graph, prob, stk, on_stk, ret)
                key_id, p = ret[-1][0], ret[-1][1]
                ans[key_id] = p
                ret.clear()
        
        mul = 1
        for p in ans.values():
            mul *= p
        print(round(mul, 9))


if __name__ == '__main__':
    main()