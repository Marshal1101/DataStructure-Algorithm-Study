import sys; input = sys.stdin.readline
sys.setrecursionlimit(200001)
from bisect import bisect_right as bil


n = int(input())
a = [0] + [int(input()) for _ in range(n)]
e = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v,w = map(int,input().split())
    e[u] += (w,v),
    e[v] += (w,u),
    
res = [0] * (n+1)
s = []
def dfs(r, d):
    global s; s += (d,r),
    i = bil(s,(d-a[r],0))
    res[r] = s[i][1]
    for w,v in e[r]:
        if not res[v]: dfs(v,d+w)
    s.pop()
dfs(1,0)
for i in range(1,n+1): print(res[i])