# https://www.acmicpc.net/source/53841751

import sys

input = sys.stdin.readline

def find(x, y):
    d = 0
    while x != y:
        if x < y:
            y = (y - 2) // K + 1
        else:
            x = (x - 2) // K + 1
        d += 1
    return d

N, K, Q = map(int, input().split())
if K == 1:
    for _ in range(Q):
        x, y = map(int, input().split())
        print(abs(y-x))
else:
    for _ in range(Q):
        x, y = map(int, input().split())
        print(find(x, y))