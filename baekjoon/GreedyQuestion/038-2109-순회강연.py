import sys; input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

N = int(input())
stk = sorted([tuple(map(int, input().split())) for _ in range(N)])
parent = [i for i in range(10001)]
checked = set()
ans = 0
while stk:
    p, d = stk.pop()
    x = find(parent, d)
    if x < 1:
        continue
    if x not in checked:
        ans += p
        checked.add(x)
        union(parent, x-1, x)

print(ans)