import sys; 


def find(parent_list, x):
    if parent_list[x] != x:
        parent_list[x] = find(parent_list, parent_list[x])
    return parent_list[x]

def union(parent_list, a, b):
    a = find(parent_list, a)
    b = find(parent_list, b)
    if a < b: parent_list[b] = a
    else: parent_list[a] = b

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, M, P, Q = map(int, input().split())
        adj_list = []
        for _ in range(M):
            u, v, w = map(int, input().split())
            adj_list.append((w, u, v))
        adj_list.sort()
        
        parent_list = [i for i in range(N+1)]
        is_found = False
        for i in range(M):
            w, u, v = adj_list[i]
            if find(parent_list, u) != find(parent_list, v):
                union(parent_list, u, v)
                if (P == u and Q == v) or (P == v and Q ==u):
                    is_found = True
                    break
        
        if is_found: print("YES")
        else: print("NO")


if __name__ == '__main__':
    main()