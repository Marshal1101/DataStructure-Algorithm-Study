import sys
sys.setrecursionlimit(10**9)


def dfs(cur, node_id, graph, stk, on_stk):
    # 현재 아이디 부여, 스택 저장
    global id, is_scc
    id += 1
    node_id[cur] = id
    stk.append(cur)
    on_stk[cur] = True
    
    # 조상 아이디 찾아가기
    asc_id = node_id[cur]
    for adj in graph[cur]:
        # 인접노드가 최초 방문 시
        if not node_id[adj]:
            # 새로운 노드 탐색, 조상노드의 아이디와 비교
            asc_id = min(asc_id, dfs(adj, node_id, graph, stk, on_stk))
        # 방문했었고, 현 스택에 있으면
        elif on_stk[adj]:
            # 현재 노드와 스택에 있던 노드의 조상노드의 아이디와 비교
            asc_id = min(asc_id, node_id[adj])
    
    # 현재노드 아이디가 시작한 조상노드 아이디와 같으면
    if asc_id == node_id[cur]:
        if not is_scc:
            while True:
                node = stk.pop()
                on_stk[node] = False
                if node == cur:
                    break
            is_scc = True
        else:
            print("No")
            sys.exit(0)
    return asc_id


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)

    global id, is_scc
    id = 0
    is_scc = False
    node_id = [0] * (N+1)
    stk = []
    on_stk = [False] * (N+1)
    for i in range(1, N+1):
        if not node_id[i]:
            dfs(i, node_id, graph, stk, on_stk)
    print("Yes")


if __name__ == '__main__':
    main()