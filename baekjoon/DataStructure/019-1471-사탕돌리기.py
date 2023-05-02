import sys
sys.setrecursionlimit(10**9)


def dfs(cur, family_id, stk, on_stk, dist):
    global N, id, ans
    id += 1
    family_id[cur] = id
    stk.append(cur)
    on_stk[cur] = True

    asc = family_id[cur]

    adj = cur + sum(map(int, str(cur)))
    adj %= N
    adj = adj if adj != 0 else N

    if not family_id[adj]:
        asc = min(asc, dfs(adj, family_id, stk, on_stk, dist))
    elif on_stk[adj]:
        asc = min(asc, family_id[adj])
    elif dist[adj]:
        dist[cur] = dist[adj] + 1
        if dist[cur] > ans:
            ans = dist[cur]

    if asc == family_id[cur]:
        scc = []
        while stk:
            node = stk.pop()
            on_stk[node] = False
            scc.append(node)
            if node == cur:
                break
        
        cnt = max(dist[cur], len(scc))
        for node in scc:
            dist[node] = cnt

        prev = cur
        while stk:
            node = stk.pop()
            on_stk[node] = False
            dist[node] = dist[prev] + 1
            prev = node
    
    return asc


def main():
    global N, id, ans
    N = int(sys.stdin.readline())
    id = ans = 0
    stk = []
    on_stk = [False] * (N+1)
    node_id = [0] * (N+1)
    dist = [0] * (N+1)
    for i in range(1, N+1):
        if not node_id[i]:
            dfs(i, node_id, stk, on_stk, dist)
    print(max(dist))


if __name__ == '__main__':
    main()