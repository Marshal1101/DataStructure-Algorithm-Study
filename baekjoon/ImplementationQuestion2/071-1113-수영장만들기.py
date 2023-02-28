import sys


def chk_bfs(num:int, si:int, sj:int, delta:list, N:int, M:int, board:list[list], visited:set):
    cnt = 1
    is_hole = False
    stk = [(si, sj)]
    visited.add((si, sj))
    while stk:
        new_stk = []
        while stk:
            ci, cj = stk.pop()
            for d in range(4):
                ni = ci + delta[d][0]
                nj = cj + delta[d][1]
                if ni < 0 or ni >= N or nj < 0 or nj >= M:
                    is_hole = True
                    continue

                if (ni, nj) in visited:
                    continue

                if board[ni][nj] <= num:
                    visited.add((ni, nj))
                    new_stk.append((ni, nj))
                    cnt += 1

        stk = new_stk

    if not is_hole:
        return cnt
    else:
        return 0

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]  #상좌하우0123
    board = [list(map(int, input().rstrip())) for _ in range(N)]

    ans = 0
    for n in range(1, 9):
        visited = set()
        for i in range(N):
            for j in range(M):
                if board[i][j] <= n and not (i, j) in visited:
                    ans += chk_bfs(n, i, j, delta, N, M, board, visited)

    print(ans)



if __name__ == '__main__':
    main()