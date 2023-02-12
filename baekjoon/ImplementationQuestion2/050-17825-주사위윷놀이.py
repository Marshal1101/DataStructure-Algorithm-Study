import sys


def BF(idx, sel, point, pos, dice, board):
    global max_point
    if idx == 10:
        if point > max_point:
            max_point = point
        return

    i, j = pos[sel]
    step = dice[idx]
    ni = i
    nj = j + step
    if i == 0:
        if nj > 20:
            ni, nj = -1, 0
        elif nj == 5:
            ni, nj = 1, 0
        elif nj == 10:
            ni, nj = 2, 0
        elif nj == 15:
            ni, nj = 3, 0

    elif i == 1:
        if nj > 7:
            ni, nj = -1, 0
    
    elif i == 2:
        if nj > 6:
            ni, nj = -1, 0
    
    elif i == 3:
        if nj > 7:
            ni, nj = -1, 0

    point40 = [(0, 20), (1, 7), (2, 6), (3, 7)]
    point35 = [(1, 6), (2, 5), (3, 6)]
    point30 = [(1, 5), (2, 4), (3, 5)]
    point25 = [(1, 4), (2, 3), (3, 4)]
    for ci, cj in pos:
        if ci == -1: continue
        if ci == ni and cj == nj:
            return
        if (ci, cj) in point40 and (ni, nj) in point40:
            return
        if (ci, cj) in point25 and (ni, nj) in point25:
            return
        if (ci, cj) in point30 and (ni, nj) in point30:
            return
        if (ci, cj) in point35 and (ni, nj) in point35:
            return

    pos[sel][0] = ni
    pos[sel][1] = nj

    cnt = 0
    for ci, cj in pos:
        cnt += ci
    if cnt == -4:
        if point > max_point:
            max_point = point
        return

    if ni != -1:
        point += board[ni][nj]

    for k in range(4):
        if pos[k][0] != -1:
            BF(idx+1, k, point, [p[:] for p in pos], dice, board)


def main():
    input = sys.stdin.readline
    board = [
        [n for n in range(0, 41, 2)],    # 40
        [10, 13, 16, 19, 25, 30, 35, 40], # 4(25)~
        [20, 22, 24, 25, 30, 35, 40],     # 3(25)~
        [30, 28, 27, 26, 25, 30, 35, 40], # 4(25)~
    ]
    global max_point
    max_point = 0
    dice = list(map(int, input().split()))
    pos = [[0, 0] for _ in range(4)]
    BF(0, 0, 0, pos, dice, board)

    print(max_point)


if __name__ == '__main__':
    main()