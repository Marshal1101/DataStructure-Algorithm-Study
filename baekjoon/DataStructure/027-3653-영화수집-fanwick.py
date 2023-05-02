T = int(input())

def update(idx, diff, fenwick_tree):
    while idx < len(fenwick_tree):
        fenwick_tree[idx] += diff
        idx += idx & (~idx + 1)
    return 0

def sum(idx, fenwick_tree):
    res = 0
    while idx > 0:
        res += fenwick_tree[idx]
        idx -= idx & (~idx + 1)
    return res

for _ in range(T):
    n, m = map(int, input().split())
    dvds = list(map(int, input().split()))

    position = [-1] + [m+i for i in range(1, n+1)]
    arr = [-1] + [0]*(n+m)
    fenwick_tree = [-1] + [0]*(n+m)
    for p in position[1:]:
        update(p, 1 - arr[p], fenwick_tree)
        arr[p] = 1
        
    first_idx = m
    for dvd in dvds:
        idx = position[dvd]
        position[dvd] = first_idx
        print(sum(idx-1, fenwick_tree), end=' ')
        update(idx, -arr[idx], fenwick_tree)
        update(first_idx, 1-arr[first_idx], fenwick_tree)
        arr[idx] = 0
        arr[first_idx] = 1
        first_idx -= 1
    
    print()