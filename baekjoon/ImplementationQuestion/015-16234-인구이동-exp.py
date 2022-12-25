## https://www.acmicpc.net/problem/16234

import sys
from collections import deque
input = sys.stdin.readline

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def bfs(sy, sx):
    population = lst[sy][sx]
    visit[sy][sx] = day
    # 당일 방문기록 쌓기
    stack = [(sy, sx)]
    for y, x in stack:
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            if visit[ny][nx] == day:
                continue
            diff = abs(lst[y][x] - lst[ny][nx])
            if diff < L or diff > R:
                continue
            visit[ny][nx] = day
            population += lst[ny][nx]
            stack.append((ny, nx))

    if len(stack) > 1:
        avg = population // len(stack)
        for y, x in stack:
            lst[y][x] = avg
            pos.append((y, x))

N, L, R = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

visit = [[-1] * N for _ in range(N)]
# 체스판처럼 체크하기
pos = deque([(y, x) for x in range(N) for y in range(x % 2, N, 2)])

day = 0
while pos:
    for _ in range(len(pos)):
        y, x = pos.popleft()
        # 오늘 방문한게 아니면 방문하기
        if visit[y][x] < day:
            bfs(y, x)
    day += 1

print(day-1)