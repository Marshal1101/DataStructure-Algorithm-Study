# https://www.acmicpc.net/problem/1417


import sys, heapq as hq


input = sys.stdin.readline
N = int(input())
no1 = _no1 = int(input())
comp = [-int(input()) for _ in range(N-1)]
hq.heapify(comp)
while comp and no1 <= -comp[0]:
    c = -hq.heappop(comp)
    no1 += 1
    c -= 1
    hq.heappush(comp, -c)

print(no1 - _no1)