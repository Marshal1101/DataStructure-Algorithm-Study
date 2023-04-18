import sys
from collections import deque

def bfs(num:int, si:int, sj:int, visited:list[list], wall:list[list], delta:list) -> int:
    cnt = 1
    q = deque([(si, sj)])
    visited[si][sj] = num
    while q:
        i, j = q.popleft()
        bit = wall[i][j]
        for b in range(4):
            if bit & 1 << b:
                continue
            ni = i + delta[b][0]
            nj = j + delta[b][1]
            if visited[ni][nj]:
                continue
            cnt += 1
            visited[ni][nj] = num
            q.append((ni, nj))

    return cnt


def check(M, N, visited, area):
    ret = 0

    for i in range(1, M+1):
        pre = visited[i][1]
        for j in range(1, N+1):
            num = visited[i][j]
            if num != pre:
                if (size := area[pre] + area[num]) > ret:
                    ret = size
            pre = num
    for j in range(1, N+1):
        pre = visited[1][j]
        for i in range(1, M+1):
            num = visited[i][j]
            if num != pre:
                if (size := area[pre] + area[num]) > ret:
                    ret = size
            pre = num

    return ret


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    wall = [[15]*(N+2)] + [[15]+[0]*N+[15] for _ in range(M)] + [[15]*(N+2)]
    for i in range(1, M+1):
        for j, v in enumerate(map(int, input().split())):
            wall[i][j+1] = v
    delta = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    visited = [[-1]*(N+2)] + [[-1] + [0]*N + [-1] for _ in range(M)] + [[-1]*(N+2)]

    area = [0]
    num = 0
    for i in range(1, M+1):
        for j in range(1, N+1):
            if visited[i][j] == 0:
                num += 1
                cnt = bfs(num, i, j, visited, wall, delta)
                area.append(cnt)
                
    print(num)
    print(max(area))
    print(check(M, N, visited, area))

if __name__ == '__main__':
    main()