import sys


def dfs(num, i, j, board, visited, delta):
    visited[i][j] = num
    stk = [(i, j)]
    while stk:
        ci, cj = stk.pop()
        d = board[ci][cj]
        ni, nj, = ci + delta[d][0], cj + delta[d][1]
        if not visited[ni][nj]:
            visited[ni][nj] = num
            stk.append((ni, nj))
        elif visited[ni][nj] == num:
            return 1
        else:
            return 0


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    delta = {
        'S': (1, 0),
        'N': (-1, 0),
        'W': (0, -1),
        'E': (0, 1),
    }
    ans = num = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue
            num += 1
            ans += dfs(num, i, j, board, visited, delta)

    print(ans)


if __name__ == '__main__':
    main()