import sys
sys.setrecursionlimit(10**6)

def main() :
    input = sys.stdin.readline
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]
    
    for _ in range(m) :
        order, a, b = map(int, input().split())
        if order :
            if find(parent, a) == find(parent, b) : print("YES")
            else : print("NO")
        else :
            union(parent, a, b)
    
def union(parent, a, b) :
    a = find(parent, a)
    b = find(parent, b)
    if a < b : parent[b] = a
    else : parent[a] = b
        
def find(parent, x) :
    if parent[x] != x :
        parent[x] = find(parent, parent[x])
    return parent[x]

if __name__ == '__main__' :
    main()