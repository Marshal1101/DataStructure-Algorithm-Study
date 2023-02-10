# https://www.acmicpc.net/source/55582203

import sys
from heapq import heappop, heappush

input = lambda dtype=int: dtype(sys.stdin.readline().strip())
input_list = lambda dtype=int: [dtype(i) for i in sys.stdin.readline().strip().split()]

N, M, F = input_list()
W = [[1] * (N+2)] + [[1] + input_list() + [1] for _ in range(N)] + [[1] * (N+2)]
T = input_list()
C = {}
for _ in range(M):
    si, sj, di, dj = input_list()
    C[(si, sj)] = (di, dj)
    W[si][sj] = 2

def BFS(src, target_func):
    H = [(0, *src)]
    V = [[False] * (N+2) for _ in range(N+2)]
    V[src[0]][src[1]] = True
    
    while H:
        d, i, j = heappop(H)
        if target_func(i, j):
            return i, j, d 

        for _i, _j in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
            if not V[_i][_j] and W[_i][_j] != 1:
                V[_i][_j] = True
                heappush(H, (d+1, _i, _j))

    return 0, 0, F+1

for _ in range(M):
    si, sj, d = BFS(T, lambda i, j: W[i][j] == 2)
    if d > F: 
        print(-1)
        exit(0) 
    F -= d
    W[si][sj] = 0

    di, dj, d = BFS((si, sj), lambda i, j: (i, j) == C[(si, sj)])
    if d > F:
        print(-1)
        exit(0)
    T = (di, dj)
    F += d

print(F)