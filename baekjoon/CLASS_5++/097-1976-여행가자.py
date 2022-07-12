import sys

def find(parent, x) :
    if parent[x] != x :
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b) :
    a = find(parent, a)
    b = find(parent, b)
    if a < b : parent[b] = a
    else : parent[a] = b
    

def main() :
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    graph = []
    for _ in range(N) :
        graph.append(list(map(int, input().split())))
    
    travel = list(map(int, input().split()))
    parent = [i for i in range(N+1)]
    for i in range(N) :
        for j in range(N) :
            if graph[i][j] :
                if find(parent, i+1) != find(parent, j+1) :
                    union(parent, i+1, j+1)
    
    before = find(parent, travel[0])
    for city in travel :
        if before != find(parent, city) :
            return "NO"
    
    return "YES"

    
if __name__ == '__main__' :
    print(main())