# kruskal, union-find

def solution(n, costs):
    parent = [i for i in range(n)]

    def find(island):
        if parent[island] != island:
            parent[island] = find(parent[island])
        return parent[island]
    
    def union(island1, island2):
        root1 = find(island1)
        root2 = find(island2)

        parent[root1] = root2
    
    costs.sort(key = lambda x:x[2])
    result = 0

    for road in costs:
        island1, island2, cost = road
        if find(island1) != find(island2):
            union(island1, island2)
            result += cost

    return result