import sys


def check_win(i: int, j: int, board: list[list[int]], visit: list[set]):
    color = board[i][j]
    ni = nj = 0

    # 우:1
    if not (i, j, 1) in visit[color]:
        temp = []
        for k in range(1, 5):
            nj = j + k
            if board[i][nj] != color:
                for tj in temp:
                    visit[color].add((i, tj, 1))
                break
            temp.append(nj)
        else:
            if board[i][j+5] != color:
                return (color, i, j)
            for k in range(5, 20):
                nj = j + k
                if board[i][nj] != color:
                    for tj in temp:
                        visit[color].add((i, tj, 1))
                    break
                temp.append(nj)

    # 우하:2
    if not (i, j, 2) in visit[color]:
        temp = []
        for k in range(1, 5):
            ni, nj = i + k, j + k
            if board[ni][nj] != color:
                for ti, tj in temp:
                    visit[color].add((ti, tj, 2))
                break
            temp.append((ni, nj))
        else:
            if board[i+5][j+5] != color:
                return (color, i, j)
            for k in range(5, 20):
                ni, nj = i + k, j + k
                if board[ni][nj] != color:
                    for ti, tj in temp:
                        visit[color].add((ti, tj, 2))
                    break
                temp.append((ni, nj))
    
    # 하:3
    if not (i, j, 3) in visit[color]:
        temp = []
        for k in range(1, 5):
            ni = i + k
            if board[ni][j] != color:
                for ti in temp:
                    visit[color].add((ti, j, 3))
                break
            temp.append(ni)
        else:
            if board[i+5][j] != color:
                return (color, i, j)
            for k in range(5, 20):
                ni = i + k
                if board[ni][j] != color:
                    for ti in temp:
                        visit[color].add((ti, j, 3))
                    break
                temp.append(ni)

    # 좌하:4
    if not (i, j, 4) in visit[color]:
        temp = []
        for k in range(1, 5):
            ni, nj = i + k, j - k
            if board[ni][nj] != color:
                for ti, tj in temp:
                    visit[color].add((ti, tj, 4))
                break
            temp.append((ni, nj))
        else:
            if board[i+5][j-5] != color:
                i = ni
                j = nj
                return (color, i, j)
            for k in range(5, 20):
                ni, nj = i + k, j - k
                if board[ni][nj] != color:
                    for ti, tj in temp:
                        visit[color].add((ti, tj, 4))
                    break
                temp.append((ni, nj))

    return 0, 0, 0



def main():
    input = sys.stdin.readline
    board = [[0] * 21] + [[0] + list(map(int, input().split())) + [0] for _ in range(19)] + [[0] * 21]
    visit = [-1, set(), set()]
    for i in range(1, 20):
        for j in range(1, 20):
            if board[i][j]:
                rc, ri, rj = check_win(i, j, board, visit)
                if rc:
                    print(rc)
                    print(ri, rj)
                    sys.exit()
    print(0)

if __name__ == '__main__':
    main()