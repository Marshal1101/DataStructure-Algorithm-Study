import sys


def no1(board: list[list]):
    board.reverse()

def no2(board: list[list]):
    for i in range(len(board)):
        board[i].reverse()

def no3(board: list[list]):
    ret = []
    for b in zip(*board):
        b = list(b)
        b.reverse()
        ret.append(b)
    return ret

def no4(board: list[list]):
    ret = []
    board.reverse()
    for b in zip(*board):
        b = list(b)
        b.reverse()
        ret.append(b)
    ret.reverse()
    return ret

def copyhalf(y: int, x: int, board: list[list]):
    ret = []
    yh = len(board) // 2
    xh = len(board[0]) // 2
    y *= yh
    x *= xh
    for i in range(y, y + yh):
        row = []
        for j in range(x, x + xh):
            row.append(board[i][j])
        ret.append(row)
    return ret

def writehalf(copy:list[list], y: int, x: int, board: list[list]):
    yh = len(board) // 2
    xh = len(board[0]) // 2
    y *= yh
    x *= xh
    for i in range(yh):
        for j in range(xh):
            board[y+i][x+j] = copy[i][j] 

def no5(board: list[list]):
    tmp = copyhalf(0, 0, board)
    writehalf(copyhalf(1, 0, board), 0, 0, board)
    writehalf(copyhalf(1, 1, board), 1, 0, board)
    writehalf(copyhalf(0, 1, board), 1, 1, board)
    writehalf(tmp, 0, 1, board)
    
def no6(board: list[list]):
    tmp = copyhalf(0, 0, board)
    writehalf(copyhalf(0, 1, board), 0, 0, board)
    writehalf(copyhalf(1, 1, board), 0, 1, board)
    writehalf(copyhalf(1, 0, board), 1, 1, board)
    writehalf(tmp, 1, 0, board)

def main():
    input = sys.stdin.readline
    N, M, R = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(input().split())
    for f in map(int, input().split()):
        if f == 1:
            no1(board)
        elif f == 2:
            no2(board)
        elif f == 3:
            board = no3(board)
        elif f == 4:
            board = no4(board)
        elif f == 5:
            no5(board)
        elif f == 6:
            no6(board)
    
    for b in board:
        print(*b)


if __name__ == '__main__':
    main()