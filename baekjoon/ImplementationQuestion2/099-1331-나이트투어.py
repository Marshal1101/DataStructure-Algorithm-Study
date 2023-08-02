import sys


def check_knight_move(pi, pj, ni, nj):
    di = abs(ni - pi)
    dj = abs(nj - pj)
    if (di == 1 and dj == 2) or (di == 2 and dj == 1):
        return True
    return False

def simulate(readlines: list[str], board: list[list]):
    pos = readlines[0]
    si = pi = ord(pos[0]) - 65
    sj = pj = int(pos[1]) - 1
    for k in range(1, 36):
        pos = readlines[k].rstrip()
        i = ord(pos[0]) - 65
        j = int(pos[1]) - 1

        if not check_knight_move(pi, pj, i, j):
            return False
        if board[i][j]:
            return False
        board[i][j] = k
        pi = i
        pj = j

    if not check_knight_move(pi, pj, si, sj):
        return False
    else:
        return True


def main():
    board = [[0] * 6 for _ in range(6)]
    if simulate(sys.stdin.readlines(), board):
        print("Valid")
    else:
        print("Invalid")



if __name__ == '__main__':
    main()