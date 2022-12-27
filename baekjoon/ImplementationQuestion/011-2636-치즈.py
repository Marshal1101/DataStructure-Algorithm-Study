# https://www.acmicpc.net/problem/2636
import sys
from collections import deque


def bfs(N, M, area):
    cheese = 0
    for i in range(N):
        for j in range(M):
            if area[i][j] == 1:
                area[i][j] = -1
                cheese += 1
    delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    hour = 1
    melted = 0
    queue = deque([(0, 0)])
    while queue:
        melted_per_hour = 0
        while queue:
            i, j = queue.popleft()
            for di, dj in delta:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < M and area[ni][nj] < hour:
                    if area[ni][nj] == -1:
                        area[ni][nj] = hour
                        melted_per_hour += 1
                    else:
                        area[ni][nj] = hour
                        queue.append((ni, nj))
        melted += melted_per_hour
        if melted == cheese: break
        hour += 1
        queue.append((0, 0))
    
    print(hour)
    print(melted_per_hour)


def main():
    N, M = map(int, sys.stdin.readline().split())
    area = [list(map(int, input().split())) for _ in range(N)]
    bfs(N, M, area)


if __name__=='__main__':
    main()