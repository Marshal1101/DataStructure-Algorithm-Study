## https://www.acmicpc.net/problem/16234

import sys
from collections import deque


def simulate(N, L, R, area) -> int:
    day = 0
    while True:
        union_cnt = 0
        visited = [False] * (N * N)
        for i in range(N*N):
            if not visited[i]:
                visited[i] = True
                union = bfs(i, N, L, R, area, visited)
                union_man = union.pop()
                new_man = union_man // len(union)
                for i in union:
                    area[i] = new_man
                union_cnt += 1

        if union_cnt == N*N: break
        day += 1
    return day

def bfs(i, N, L, R, area, visited) -> list:
    union = [i]
    union_man = area[i]
    queue = deque([i])
    while queue:
        for _ in range(len(queue)):
            i = queue.popleft()
            r, c = i//N, i%N
            if i - 1 >= r*N and not visited[i-1]:
                if L <= abs(area[i] - area[i-1]) <= R:
                    visited[i-1] = True
                    union_man += area[i-1]
                    union.append(i-1)
                    queue.append(i-1)
            if i + 1 < (r+1)*N and not visited[i+1]:
                if L <= abs(area[i] - area[i+1]) <= R:
                    visited[i+1] = True
                    union_man += area[i+1]
                    union.append(i+1)
                    queue.append(i+1)
            if i - N >= 0 and not visited[i-N]:
                if L <= abs(area[i] - area[i-N]) <= R:
                    visited[i-N] = True
                    union_man += area[i-N]
                    union.append(i-N)
                    queue.append(i-N)
            if i + N < N*N and not visited[i+N]:
                if L <= abs(area[i] - area[i+N]) <= R:
                    visited[i+N] = True
                    union_man += area[i+N]
                    union.append(i+N)
                    queue.append(i+N)
    union.append(union_man)
    return union


def main():
    input = sys.stdin.readline
    N, L, R = map(int, input().split())
    area = []
    for _ in range(N):
        area.extend(list(map(int, input().split())))
    print(simulate(N, L, R, area))


if __name__=='__main__':
    main()