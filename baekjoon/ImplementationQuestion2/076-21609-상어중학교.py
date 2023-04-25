import sys; input = sys.stdin.readline


"""
1. 블록영역찾기
1-1. 가장 큰 영역 > 무지개 개수 > 행 > 열
2. 점수계산
3. 반시계 회전
4. 중력
"""

def BFS(i, j, visited, board) -> tuple[list, list]:
    color = board[i][j]
    rainbow = []
    visited[i][j] = True
    path = [((i, j))]
    stk = [(i, j)]
    while stk:
        ci, cj = stk.pop()
        for di, dj in delta:
            ni = ci + di
            nj = cj + dj
            if ni < 0 or nj < 0 or ni >= N or nj >= N:
                continue
            if visited[ni][nj]:
                continue
            if board[ni][nj] == 0:
                visited[ni][nj] = True
                rainbow.append((ni, nj))
                stk.append((ni, nj))
            elif board[ni][nj] == color:
                visited[ni][nj] = True
                path.append((ni, nj))
                stk.append((ni, nj))

    return path, rainbow


def find_widest_area(board) -> list:
    visited = [[False] * N for _ in range(N)]
    area_path = dict()
    area = []
    for i in range(N):
        for j in range(N):
            if visited[i][j] or board[i][j] == "" or board[i][j] == -1 or board[i][j] == 0:
                continue
            path, rainbow = BFS(i, j, visited, board)
            area_path[(i, j)] = path + rainbow
            cnt = len(path)+len(rainbow)
            if cnt > 1:
                area.append((cnt, len(rainbow), i, j))
            for ri, rj in rainbow:
                visited[ri][rj] = False
    if not area:
        return []
    area.sort(reverse=True)
    si, sj = area[0][2], area[0][3]
    return area_path[(si, sj)]

def cal_point(area) -> int:
    return len(area) ** 2

def clear_area(area, board) -> None:
    for i, j in area:
        board[i][j] = ""

def rotate(board):
    new_board = [[""] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[i][j] = board[j][N-1-i]
    return new_board

# def rotate(board):
#     return list(reversed(list(map(list, zip(*board)))))

def drop_down(board):
    empty = [N-1] * N
    for j in range(N):
        if board[N-1][j] != "":
            empty[j] -= 1
    # tmp = [board[N-1][j] for j in range(N)]
    for i in range(N-2, -1, -1):
        for j in range(N):
            if board[i][j] == "":
                continue
            if board[i][j] == -1:
                empty[j] = i-1
                continue
            if empty[j] > i:
                board[empty[j]][j] = board[i][j]
                board[i][j] = ""
            empty[j] -= 1


# def printb(board):
#     for b in board:
#         print(b)

def simulate(board):
    ans = 0
    area = find_widest_area(board)
    k = 0
    while area:
        k += 1
        ans += cal_point(area)
        clear_area(area, board)
        # print("clear===========", area, ans)
        # printb(board)
        drop_down(board)
        # print("down===========")
        # printb(board)
        board = rotate(board)
        # print("rotate===========")
        # printb(board)
        drop_down(board)
        # print("down===========")
        # printb(board)
        area = find_widest_area(board)
    return ans


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
print(simulate(board))