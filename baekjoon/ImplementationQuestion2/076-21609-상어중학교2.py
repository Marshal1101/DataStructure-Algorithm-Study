import sys; input = sys.stdin.readline


def BFS(i, j, visited, rot) -> tuple[int, int, list]:
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
    if rot == 0:
        ei, ej = sorted(path, key=lambda x: (x[0], x[1]))[0]
    elif rot == 1:
        ei, ej = sorted(path, key=lambda x: (-x[1], x[0]))[0]
    elif rot == 2:
        ei, ej = sorted(path, key=lambda x: (-x[0], -x[1]))[0]
    elif rot == 3:
        ei, ej = sorted(path, key=lambda x: (x[1], -x[0]))[0]

    return ei, ej, path, rainbow


def find_widest_area(rot) -> list:
    visited = [[False] * N for _ in range(N)]
    area_path = dict()
    area = []
    for i in range(N):
        for j in range(N):
            if visited[i][j] or board[i][j] == "" or board[i][j] == -1 or board[i][j] == 0:
                continue
            ei, ej, path, rainbow = BFS(i, j, visited, rot)
            area_path[(ei, ej)] = path + rainbow
            cnt = len(path) + len(rainbow)
            if cnt > 1:
                area.append((cnt, len(rainbow), ei, ej))
            for ri, rj in rainbow:
                visited[ri][rj] = False
    if not area:
        return []
    
    if rot == 0:
        area.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
    elif rot == 1:
        area.sort(key=lambda x: (-x[0], -x[1], x[3], -x[2]))
    elif rot == 2:
        area.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    elif rot == 3:
        area.sort(key=lambda x: (-x[0], -x[1], -x[3], x[2]))
    max_cnt, max_rain, si, sj = area[0]
    return area_path[(si, sj)]


def cal_point(area) -> int:
    return len(area) ** 2

def clear_area(area) -> None:
    for i, j in area:
        board[i][j] = ""


def drop_down():
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

def drop_left():
    empty = [0] * N
    for i in range(N):
        if board[i][0] != "":
            empty[i] += 1
    for j in range(1, N):
        for i in range(N):
            if board[i][j] == "":
                continue
            if board[i][j] == -1:
                empty[i] = j+1
                continue
            if empty[i] < j:
                board[i][empty[i]] = board[i][j]
                board[i][j] = ""
            empty[i] += 1

def drop_up():
    empty = [0] * N
    for j in range(N):
        if board[0][j] != "":
            empty[j] += 1
    for i in range(1, N):
        for j in range(N):
            if board[i][j] == "":
                continue
            if board[i][j] == -1:
                empty[j] = i+1
                continue
            if empty[j] < i:
                board[empty[j]][j] = board[i][j]
                board[i][j] = ""
            empty[j] += 1

def drop_right():
    empty = [N-1] * N
    for i in range(N):
        if board[i][N-1] != "":
            empty[i] -= 1
    for j in range(N-2, -1, -1):
        for i in range(N):
            if board[i][j] == "":
                continue
            if board[i][j] == -1:
                empty[i] = j-1
                continue
            if empty[i] > j:
                board[i][empty[i]] = board[i][j]
                board[i][j] = ""
            empty[i] -= 1

# def printb():
#     for b in board:
#         print(b)


def simulate():
    ans = 0
    drop = [drop_down, drop_left, drop_up, drop_right]
    rot = 0
    area = find_widest_area(rot)
    while area:
        ans += cal_point(area)
        clear_area(area)
        # print("clear===========", area, ans)
        # printb()
        drop[rot]()
        # print("rot===========", rot)
        # printb()
        rot = (rot + 1) % 4
        drop[rot]()
        # print("rot===========", rot)
        # printb()
        area = find_widest_area(rot)

    return ans


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
print(simulate())