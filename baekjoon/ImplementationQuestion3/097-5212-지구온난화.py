import sys


def main():
    input = sys.stdin.readline
    R, C = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(R)]
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                continue
            cnt = 0
            for di, dj in delta:
                ni = i + di
                nj = j + dj
                if ni < 0 or nj < 0 or ni > R-1 or nj > C-1:
                    cnt += 1
                    continue
                if board[ni][nj] == '.':
                    cnt += 1
                    continue
            if cnt > 2:
                board[i][j] = 'O'

    si = sj = 0
    ei = R-1
    ej = C-1
    flag = False
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'X':
                si = i
                flag = True
                break
        if flag: break

    flag = False
    for i in range(R-1, -1, -1):
        for j in range(C-1, -1, -1):
            if board[i][j] == 'X':
                ei = i
                flag = True
                break
        if flag: break

    flag = False
    for j in range(C):
        for i in range(R):
            if board[i][j] == 'X':
                sj = j
                flag = True
                break
        if flag: break

    flag = False
    for j in range(C-1, -1, -1):
        for i in range(R-1, -1, -1):
            if board[i][j] == 'X':
                ej = j
                flag = True
                break
        if flag: break

    for i in range(si, ei+1):
        for j in range(sj, ej+1):
            if board[i][j] == 'O':
                board[i][j] = '.'
            print(board[i][j], end='')
        print()


if __name__ == '__main__':
    main()