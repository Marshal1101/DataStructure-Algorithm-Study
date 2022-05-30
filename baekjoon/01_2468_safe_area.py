## 01 2468 안전영역

from collections import deque
import sys

input = sys.stdin.readline


n = int(input())
world = []
for i in range(n) :
    world.append(list(map(int,input().split())))

def max_height(area) :
    max_h = 0
    for i in range(n) :
        for j in range(n) :
            if area[i][j] > max_h :
                max_h = area[i][j]
    return max_h

def safe_checher(area, h, visited) :
    for i in range(n) :
        for j in range(n) :
            if area[i][j] <= h :
                visited[i][j] = True
    return visited

def BFS(y, x, visited) :
    if visited[y][x] :
        return 0
    visited[y][x] = True
    queue = deque([(y, x)])
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    while queue :
        y, x = queue.popleft()
        for k in range(4) :
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] :
                queue.append((ny, nx))
                visited[ny][nx] = True
    return 1

max_h = max_height(world)
h = 1
pre_cnt = 0
while h <= max_h :
    visited = [[False for _ in range(n)] for _ in range(n)]   
    v = safe_checher(world, h, visited)
    cnt = 0
    for i in range(n) :
        for j in range(n) :
            cnt += BFS(j, i, v)
    if pre_cnt <= cnt :
        pre_cnt = cnt
        h += 1
    else :
        break

print(pre_cnt)