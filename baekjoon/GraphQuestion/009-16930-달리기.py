import sys


def bfs(x1, y1, x2, y2, board, K):
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = dict()
    visited[(x1, y1)] = 0
    qstack = [(x1, y1, -1)]
    time = 0
    while qstack:
        new_qstk = []
        time += 1
        while qstack:
            cx, cy, prevdir = qstack.pop()
            for i in range(4):
                if i == prevdir: continue
                for j in range(1, K+1):
                    nx = cx + j * delta[i][0]
                    ny = cy + j * delta[i][1]
                    if board[nx][ny] == '#':
                        break
                    if (nx, ny) in visited:
                        if time > visited[(nx, ny)]: break
                        else: continue
                    visited[(nx, ny)] = time
                    if j == K: new_qstk.append((nx, ny, -1))
                    else: new_qstk.append((nx, ny, i))
        if (x2, y2) in visited:
            return visited[(x2, y2)]
        qstack = new_qstk
    
    return -1


def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    board = [['#'] * (M+2)] + \
            [['#'] + list(input().rstrip()) + ['#'] for _ in range(N)] + \
            [['#'] * (M+2)]
    x1, y1, x2, y2 = map(int, input().split())
    print(bfs(x1, y1, x2, y2, board, K))


if __name__ == '__main__':
    main()