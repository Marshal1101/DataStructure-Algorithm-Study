import sys
from collections import deque


# 3. 섬연결 체크, MST
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b


# 2. 다리 길이는 2이상이어야 한다. 다리는 직선이고 양 끝단에는 섬이 있어야 한다.
def try_build_bridge(si, sj, N, M, board, bridge):
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    island = board[si][sj]
    for k in range(4):
        ni = si + d[k][0]
        nj = sj + d[k][1]
        if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == 0:
            move_cnt = 0

            # 좌우 직선
            if ni == si:
                while 0 < nj < M-1 and board[si][nj] == 0:
                    move_cnt += 1
                    nj += d[k][1]
                if board[si][nj] != 0 and move_cnt > 1 and board[si][nj] != island \
                    and move_cnt < bridge[island][board[si][nj]]:
                        bridge[island][board[si][nj]] = move_cnt
                        bridge[board[si][nj]][island] = move_cnt

            # 상하 직선
            elif nj == sj:
                while 0 < ni < N-1 and board[ni][sj] == 0:
                    move_cnt += 1
                    ni += d[k][0]
                if board[ni][sj] != 0 and move_cnt > 1 and board[ni][sj] != island \
                    and move_cnt < bridge[island][board[ni][sj]]:
                        bridge[island][board[ni][sj]] = move_cnt
                        bridge[board[ni][sj]][island] = move_cnt


# 1. bfs 섬탐색
def bfs(island_num, si, sj, N, M, board):
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    board[si][sj] = island_num
    queue = deque([(si, sj)])
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni = i + d[k][0]
            nj = j + d[k][1]
            if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == "1":
                board[ni][nj] = island_num
                queue.append((ni, nj))


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    board = [input().split() for _ in range(N)]

    # 1. 탐색 및 bfs하면서 각 섬에 번호를 붙힌다. 섬은 2 ~ 6개이다.
    island_num = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == "0":
                board[i][j] = 0
            elif board[i][j] == "1":
                island_num += 1
                bfs(island_num, i, j, N, M, board)

    # 2. 각 섬 사이에 최단 거리를 구한다.
    bridge = [[100 for _ in range(island_num+1)] for _ in range(island_num+1)]
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                try_build_bridge(i, j, N, M, board, bridge)

    # 3. MST로 연결 최단 거리를 구한다. 모든 연결 불가능하면 -1 출력. 
    adj_list = []
    for v1 in range(1, island_num+1):
        for v2 in range(v1+1, island_num+1):
            if bridge[v1][v2] != 100:
                adj_list.append((bridge[v1][v2], v1, v2))

    adj_list.sort()

    length = 0
    parent = [i for i in range(island_num+1)]
    for w, v1, v2 in adj_list:
        if find(parent, v1) != find(parent, v2):
            union(parent, v1, v2)
            length += w

    for i in parent[1:]:
        if find(parent, i) != 1:
            print(-1)
            return

    print(length)


if __name__ == '__main__':
    main()