import sys

def dfs(cur, d, graph, on_stk, stk, ans):
    global id
    id += 1
    d[cur] = id
    stk.append(cur)
    on_stk[cur] = True
    
    parent = d[cur]
    for adj in graph[cur]:
        if not d[adj]:
            parent = min(parent, dfs(adj, d, graph, on_stk, stk, ans))
        elif on_stk[adj]:
            parent = min(parent, d[adj])

    if parent == d[cur]:
        scc = []
        while True:
            node = stk.pop()
            on_stk[node] = False
            scc.append(node)
            if cur == node:
                break
        ans.append((*sorted(scc), -1))
    return parent

def main():
    input = sys.stdin.readline
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
    
    ans = []
    global id
    id = 1
    d = [0 for _ in range(V+1)]
    stk = []
    on_stk = [0] * (V+1)
    for i in range(1, V+1):
        if not d[i]:
            dfs(i, d, graph, on_stk, stk, ans)
    
    print(len(ans))

if __name__ == '__main__':
    main()