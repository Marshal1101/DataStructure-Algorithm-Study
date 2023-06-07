import sys


def check_rec(v, sr, er, dr, sc, ec, dc, board, shape):
    
    lr = lc = 0
    while i < er:
        i = i + dr
        if board[i][sc] == v:
            lr += 1
        else:
            break

    while j < ec:
        j = j + dc
        if board[sr][j] == v:
            lc += 1
        else:
            break

    if lr != lc:
        return False

    sr += 1
    sc += 1
    while board[sr][sc] == v:
        i = sr
        j = sc
        while i < er:
            i = i + dr
            if board[i][sc] == v:
                lr += 1
            else:
                break

        while j < ec:
            j = j + dc
            if board[sr][j] == v:
                lc += 1
            else:
                break

        if lr != lc:
            



    for i in range(sr, er, dr):
        for j in range(sc, ec, dc):
            if board[i][j] != v:




def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        R, C = map(int, input().split())
        shape = [True] * 4
        board = [input().split() for _ in range(R)]
        stack = []
        v = ['#', '.']
        tick = False
        w1 = w2 = w3 = h1 = h2 = h3 = -1
        for i in range(R):
            for j in range(C):
                if board[i][j] == v[tick]:
                    tick = not tick
                    h1 = i - stack[-1][0]
                    w1 = j - stack[-1][1]
                    stack.append((i, j))



        check_rec(board[0][0], 0, 0, R, C, board, shape)
