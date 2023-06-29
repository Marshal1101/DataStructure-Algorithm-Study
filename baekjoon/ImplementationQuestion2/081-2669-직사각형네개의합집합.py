def main():
    board = [[False] * 100 for _ in range(100)]
    for _ in range(4):
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(y1, y2):
            for j in range(x1, x2):
                board[i][j] = True
    cnt = 0
    for i in range(100):
        for j in range(100):
            if board[i][j]:
                cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()