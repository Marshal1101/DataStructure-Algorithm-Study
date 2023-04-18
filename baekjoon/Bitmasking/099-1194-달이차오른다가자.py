import sys
from collections import deque


def BFS(board:list[list], si:int, sj:int, visited:list[list[list]], delta:list):
    # 1. 시작 si, sj, fedcba=000000, cnt
    q = deque([(si, sj, 0, 0)])
    visited[si][sj][0] = True
    # 2. bfs
    while q:
        ci, cj, key, cnt = q.popleft()
        for di, dj in delta:
            ni = ci + di
            nj = cj + dj
            if visited[ni][nj][key] or board[ni][nj] == '#':
                continue
            if board[ni][nj] == '.':
                visited[ni][nj][key] = True
                q.append((ni, nj, key, cnt+1))
            elif 'a' <= board[ni][nj] <= 'f':
                bit = ord(board[ni][nj])-97
                nkey = key | 1 << bit
                if not visited[ni][nj][nkey]:
                    visited[ni][nj][nkey] = True
                    q.append((ni, nj, nkey, cnt+1))
            elif 'A' <= board[ni][nj] <= 'F':
                bit = ord(board[ni][nj])-65
                if key & 1 << bit:
                    visited[ni][nj][key] = True
                    q.append((ni, nj, key, cnt+1))
            else:
                return cnt + 1
    
    return -1


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    # 테두리 벽 치고 보드 생성
    board = [['#'] * (M+2)] + \
        [['#'] + list(input().rstrip()) + ['#'] for _ in range(N)] + \
        [['#'] * (M+2)]
    
    visited = [[[False]*64 for _ in range(M+2)] for _ in range(N+2)]

    # 시작 위치 찾기
    for i in range(1, N+1):
        for j in range(1, M+1):
            if board[i][j] == '0':
                si, sj = i, j
                board[i][j] = '.'

    delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    print(BFS(board, si, sj, visited, delta))


if __name__ == '__main__':
    main()