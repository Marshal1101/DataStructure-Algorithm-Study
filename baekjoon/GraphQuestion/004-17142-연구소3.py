import sys
from itertools import combinations


def bfs(case:set, N:int, board:list[list], delta:list, virus:list, empty_cnt:int):
    global ans
    stk = [virus[i] for i in case]
    visited = set(stk)
    time = 0
    while stk:
        time += 1
        if time == ans:
            return -1
        new_stk = []
        while stk:
            i, j = stk.pop()
            for di, dj in delta:
                ni = i + di
                nj = j + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= N:
                    continue
                if (ni, nj) in visited or not board[ni][nj]:
                    continue
                if board[ni][nj] != '2':
                    empty_cnt -= 1
                visited.add((ni, nj))
                new_stk.append((ni, nj))
        if empty_cnt == 0:
            return time
        stk = new_stk
    return -1

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    board = [input().split() for _ in range(N)]
    delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    wall_cnt = 0
    virus_pos = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == '1':
                wall_cnt += 1
                board[i][j] = 0
            elif board[i][j] == '2':
                virus_pos.append((i, j))
    empty_cnt = N*N - len(virus_pos) - wall_cnt
    if empty_cnt == 0:
        print(0)
        return
    global ans
    ans = sys.maxsize
    for case in combinations(range(len(virus_pos)), M):
        ret = bfs(case, N, board, delta, virus_pos, empty_cnt)
        if ret != -1 and ret < ans:
            ans = ret

    if ans != sys.maxsize: print(ans)
    else: print(-1)


if __name__ == '__main__':
    main()