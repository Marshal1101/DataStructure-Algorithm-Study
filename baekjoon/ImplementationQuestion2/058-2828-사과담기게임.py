# https://www.acmicpc.net/problem/2828

import sys


input = sys.stdin.readline
N, M = map(int, input().split())
J = int(input())

ans = 0
p = 0
for _ in range(J):
    a = int(input())
    if a > p:
        if (tmp := p + M) < a:
            step = a - tmp
            p += step
            ans += step
    else:
        step = p+1 - a
        p -= step
        ans += step

print(ans)