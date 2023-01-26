import sys
from collections import deque


def count_popul(N, area, board) -> list:
    popul = [0] * 5
    for i in range(N):
        for j in range(N):
            popul[area[i][j]-1] += board[i][j]
    return popul


def bfs(num, si, sj, N, area):
    # 경계 안을 탐색한다.
    area[si][sj] = num
    queue = deque([(si, sj)])
    while queue:
        i, j = queue.popleft()
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni = i + di
            nj = j + dj
            if ni < 0 or nj < 0 or ni >= N or nj >= N \
                or area[ni][nj] != 0:
                continue
            area[ni][nj] = num
            queue.append((ni, nj))


def set_border_line(x, y, d1, d2, N, area):
    ## 1. 5번 구역을 만든다.
    # 5선거구 2경계선
    for k in range(d2+1):
        area[x+k][y+k] = 5
    # 5선거구 1경계선
    for k in range(d1+1):
        area[x+k][y-k] = 5
    # 5선거구 3경계선
    for k in range(d2+1):
        area[x+d1+k][y-d1+k] = 5
    # 5선거구 4경계선
    for k in range(d1+1):
        area[x+d2+k][y+d2-k] = 5

    ## 2. 1234 구역을 경계를 긋는다.
    # 1-2선거구 경계선
    for i in range(x):
        area[i][y] = 1
    # 2-4선거구 경계선
    for j in range(y+d2+1, N):
        area[x+d2][j] = 2
    # 3-1선거구 경계선
    for j in range(y-d1):
        area[x+d1][j] = 3
    # 4-3선거구 경계선
    for i in range(x+d1+d2+1, N):
        area[i][y+d2-d1] = 4


def get_minimum_diff(x, y, N, board):
    xy_min_pop = 40001
    for d1 in range(1, y+1):
        for d2 in range(1, N-x-1):
            if x + d1 + d2 >= N or y - d1 < 0 or y + d2 >= N:
                continue
            is_return = True
            area = [[0]*N for _ in range(N)]
            set_border_line(x, y, d1, d2, N, area)

            # 3. bfs로 각 영역을 탐색하여 인구를 구한다.
            bfs(5, x+1, y, N, area)
            bfs(1, 0, 0, N, area)
            bfs(2, 0, N-1, N, area)
            bfs(3, N-1, 0, N, area)
            bfs(4, N-1, N-1, N, area)

            # 4. 인구 합산
            popul = count_popul(N, area, board)
            min_pop = min(popul)
            max_pop = max(popul)

            if (temp := max_pop - min_pop) < xy_min_pop:
                xy_min_pop = temp

    return xy_min_pop


def main():
    input = sys.stdin.readline
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    min_diff = 40001
    for x in range(N):
        for y in range(1, N):
            diff = get_minimum_diff(x, y, N, board)

            
            if diff < min_diff:
                min_diff = diff

    print(min_diff)


if __name__ == '__main__':
    main()