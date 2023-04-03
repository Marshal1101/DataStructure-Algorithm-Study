import sys


def dfs(si, sj, C, board, delta):
    board[si][sj] = 'x'
    if sj == C:
        return 1
    for di, dj in delta:
        ni = si + di
        nj = sj + dj
        if board[ni][nj] != 'x':
            ret = dfs(ni, nj, C, board, delta)
            if ret:
                return ret
    return 0


def main():
    input = sys.stdin.readline
    R, C = map(int, input().split())
    board = [['x'] * (C+2)] + [['x'] + list(input().rstrip()) + ['x'] for _ in range(R)] + [['x'] * (C+2)]
    delta = [(-1, 1), (0, 1), (1, 1)]
    ans = 0
    for i in range(1, R+1):
        ans += dfs(i, 1, C, board, delta)

    print(ans)

if __name__ == '__main__':
    main()