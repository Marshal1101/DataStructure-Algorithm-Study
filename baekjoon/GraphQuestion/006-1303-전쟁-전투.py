import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(M)]
    visited = [[False] * N for _ in range(M)]
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    white_p = blue_p = cnt = 0
    for i in range(M):
        for j in range(N):
            if not visited[i][j]:
                cnt = dfs(i, j, N, M, board, visited, delta)
                if cnt > 0: white_p += (cnt ** 2)
                else: blue_p += (cnt ** 2)
    print(white_p, blue_p)


def dfs(i, j, N, M, board, visited, delta):
    visited[i][j] = True
    stack = [(i, j)]
    cnt = 1
    while stack:
        ci, cj = stack.pop()
        for di, dj in delta:
            ni = ci + di
            nj = cj + dj
            if ni < 0 or nj < 0 or ni >= M or nj >= N:
                continue
            if board[ni][nj] != board[i][j]:
                continue
            if not visited[ni][nj]:
                visited[ni][nj] = True
                stack.append((ni, nj))
                cnt += 1
    return cnt if board[i][j] == 'W' else -cnt

if __name__ == '__main__':
    main()