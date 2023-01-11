import sys


def draw_curve(X, Y, D, G, board, delta):
    # 각 좌표 방향
    curve = []

    # 초기 0레벨
    curve.append(D)
    board[Y][X] = True
    x = X + delta[D][0]
    y = Y + delta[D][1]
    curve.append(D)
    board[y][x] = True

    # G 레벨까지
    t = 0
    while t < G:
        for i in range(len(curve)-1, 0, -1):
            nd = (curve[i] + 1) % 4
            x = x + delta[nd][0]
            y = y + delta[nd][1]
            if 0 <= x < 101 and 0 <= y < 101:
                curve.append(nd)
                board[y][x] = True
        t += 1


def count_curve(board):
    count = 0
    for y in range(1, 101):
        for x in range(1, 101):
            if board[y][x] and board[y-1][x] and board[y-1][x-1] and board[y][x-1]:
                count +=1
    return count


def main():
    input = sys.stdin.readline
    N = int(input())
    board = [[False for _ in range(101)] for _ in range(101)]
    delta = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    for _ in range(N):
        X, Y, D, G = map(int, input().split())
        draw_curve(X, Y, D, G, board, delta)

    print(count_curve(board))


if __name__ == '__main__':
    main()