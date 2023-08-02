import sys


def seqtop(seq:list[tuple]) -> tuple:
    seq.sort()
    if seq[0][0] == seq[2][0]:
        return (*seq[1], 0)
    elif seq[0][1] == seq[2][1]:
        return (*seq[1], 1)

def main():
    input = sys.stdin.readline
    N = int(input())
    board = [list(input().rstrip()) for _ in range(N)]
    bseq = []
    eseq = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'B':
                bseq.append((i, j))
            elif board[i][j] == 'E':
                eseq.append((i, j))
    bp = seqtop(bseq)
    ep = seqtop(eseq)
    visited = set()
    visited.add(bp)
    stk = [bp]
    time = 0
    while stk:
        time += 1
        nstk = []
        while stk:
            i, j, d = stk.pop()
            # 가로
            if d == 0:
                upflag = False
                downflag = False
                if i > 0:
                    if board[i-1][j-1] != '1' and board[i-1][j] != '1' and board[i-1][j+1] != '1':
                        upflag = True
                        if (np := (i-1, j, 0)) not in visited:
                            if np == ep: return time
                            visited.add(np)
                            nstk.append(np)
                if i < N-1:
                    if board[i+1][j-1] != '1' and board[i+1][j] != '1' and board[i+1][j+1] != '1':
                        downflag = True
                        if (np := (i+1, j, 0)) not in visited:
                            if np == ep: return time
                            visited.add(np)
                            nstk.append(np)
                if j > 1 and board[i][j-2] != '1' and (np := (i, j-1, 0)) not in visited:
                    if np == ep: return time
                    visited.add(np)
                    nstk.append(np)
                if j < N-2 and board[i][j+2] != '1' and (np := (i, j+1, 0)) not in visited:
                    if np == ep: return time
                    visited.add(np)
                    nstk.append(np)
                if upflag and downflag and (np := (i, j, 1)) not in visited:
                    if np == ep: return time
                    visited.add(np)
                    nstk.append(np)
            # 세로
            else:
                lflag = False
                rflag = False
                if j > 0:
                    if board[i-1][j-1] != '1' and board[i][j-1] != '1' and board[i+1][j-1] != '1':
                        lflag = True
                        if (np := (i, j-1, 1)) not in visited:
                            if np == ep: return time
                            visited.add(np)
                            nstk.append(np)
                if j < N-1:
                    if board[i-1][j+1] != '1' and board[i][j+1] != '1' and board[i+1][j+1] != '1':
                        rflag = True
                        if (np := (i, j+1, 1)) not in visited:
                            if np == ep: return time
                            visited.add(np)
                            nstk.append(np)
                if i > 1 and board[i-2][j] != '1' and (np := (i-1, j, 1)) not in visited:
                    if np == ep: return time
                    visited.add(np)
                    nstk.append(np)
                if i < N-2 and board[i+2][j] != '1' and (np := (i+1, j, 1)) not in visited:
                    if np == ep: return time
                    visited.add(np)
                    nstk.append(np)
                if lflag and rflag and (np := (i, j, 0)) not in visited:
                    if np == ep: return time
                    visited.add(np)
                    nstk.append(np)
        stk = nstk
    return 0


if __name__ == '__main__':
    print(main())