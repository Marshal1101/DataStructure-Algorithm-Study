import sys
from collections import deque
from itertools import combinations


def bfs_shoot(pos_j, board: list[list], N, M, D) -> tuple:
    if board[N-1][pos_j] != 0:
        # print(f"killed: {N-1} {pos_j} by {pos_j}, dist: 1")
        return (N-1, pos_j)

    delta = [(0, -1), (-1, 0), (0, 1)]
    visited = set()
    visited.add((N-1, pos_j))
    queue = deque([(N-1, pos_j)])
    k = 1
    while k < D:
        k += 1
        for _ in range(len(queue)):
            ai, aj = queue.popleft()
            for di, dj in delta:
                ni = ai + di
                nj = aj + dj
                if ni >= 0 and 0 <= nj < M and not (ni, nj) in visited:
                    if board[ni][nj] != 0:
                        # print(f"killed: {ni} {nj} by {pos_j}, dist: {k}")
                        return (ni, nj)
                    else:
                        visited.add((ni, nj))
                        queue.append((ni, nj))

    return (-1, -1)


def simulate(pos: tuple, board: list[list], N, M, D):
    kill = 0
    is_enemy_there = True
    dead = set()
    while is_enemy_there:
        # print(f"{pos}, distance: {D}, play ====== next turn======")
        dead.clear()
        # 사격
        for j in pos:
            zi, zj = bfs_shoot(j, board, N, M, D)
            if zi != -1 and not (zi, zj) in dead:
                dead.add((zi, zj))
                kill += 1
        # 적 전진
        is_enemy_there = enemy_move(dead, board, N, M)

    return kill

def enemy_move(dead, board, N, M) -> bool:
    for ei, ej in dead:
        board[ei][ej] = 0

    is_enemy = False
    for i in range(N-1, -1, -1):
        for j in range(M):
            if board[i][j] != 0:
                board[i][j] = 0
                if i < N-1:
                    board[i+1][j] = 1
                    is_enemy = True

    return is_enemy

def main():
    input = sys.stdin.readline
    N, M, D = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    max_kill = 0
    castle = [j for j in range(M)]
    for pos in combinations(castle, 3):
        copy_board = [b[:] for b in board]
        cnt = simulate(pos, copy_board, N, M, D)
        if cnt > max_kill: max_kill = cnt

    print(max_kill)


if __name__ == '__main__':
    main()




