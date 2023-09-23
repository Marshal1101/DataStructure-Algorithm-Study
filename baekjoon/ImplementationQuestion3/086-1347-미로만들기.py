def main():
    N = int(input())
    maxy = maxx = 0
    miny = minx = 0
    y = x = 0
    d = 0
    delta = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    path = [(0, 0)]
    for com in input().rstrip():
        if com == 'R':
            d = (d + 1) % 4
        elif com == 'L':
            d = (d - 1) % 4
        elif com == 'F':
            y += delta[d][0]
            x += delta[d][1]
            if y > maxy: maxy = y
            if x > maxx: maxx = x
            if y < miny: miny = y
            if x < minx: minx = x
            path.append((y, x))

    # print(maxy, maxx, miny, minx)
    R = maxy - miny + 1
    C = maxx - minx + 1
    # print(path)
    board = [['#'] * C for _ in range(R)]
    for y, x in path:
        board[y-miny][x-minx] = '.'

    for b in board:
        print("".join(b))


if __name__ == '__main__':
    main()