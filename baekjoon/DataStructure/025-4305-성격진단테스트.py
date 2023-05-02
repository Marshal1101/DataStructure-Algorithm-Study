import sys
from collections import defaultdict


def dfs(cur, node_id, graph, stk, on_stk, ret):
    global id
    id += 1
    node_id[cur] = id
    stk.append(cur)
    on_stk[cur] = True

    asc_id = node_id[cur]
    for adj in graph[cur]:
        if not node_id[adj]:
            asc_id = min(asc_id, dfs(adj, node_id, graph, stk, on_stk, ret))
        elif on_stk[adj]:
            asc_id = min(asc_id, node_id[adj])

    if asc_id == node_id[cur]:
        scc = []
        while stk:
            node = stk.pop()
            scc.append(node)
            on_stk[node] = False
            if node == cur:
                break
        scc.sort()
        ret.append(scc)
    
    return asc_id


def main():
    input = sys.stdin.readline
    while (N := int(input())) != 0:
        all_node = set()
        indegree = set()
        graph = defaultdict(list)
        for _ in range(N):
            line = input().split()
            for node in line:
                if node == line[-1]:
                    continue
                graph[line[-1]].append(node)
                indegree.add(node)
            all_node.update(line)

        global id
        id = 0
        stk = []
        on_stk = defaultdict(bool)
        node_id = defaultdict(int)
        ret = []
        for node in all_node:
            if not node_id[node]:
                dfs(node, node_id, graph, stk, on_stk, ret)
                # print(node, ret)
        
        ret.sort()
        for r in ret:
            print(*r)
        print()


if __name__ == '__main__':
    main()