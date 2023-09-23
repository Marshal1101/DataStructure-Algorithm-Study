import sys


def curve(d, pipe):
    # 하0 상1 우2 좌3
    if pipe == '1':
        if d == 1: return 2
        if d == 3: return 0
    if pipe == '2':
        if d == 0: return 2
        if d == 3: return 1
    if pipe == '3':
        if d == 2: return 1
        if d == 0: return 3
    if pipe == '4':
        if d == 2: return 0
        if d == 1: return 3
    return d


def main():
    input = sys.stdin.readline
    R, C = map(int, input().split())
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    board = [list(input().rstrip()) for _ in range(R)]
    pipe = [
        {'|', '+', '2', '3'},
        {'|', '+', '1', '4'},
        {'-', '+', '3', '4'},
        {'-', '+', '1', '2'}
    ]
    si = sj = ei = ej = pi = pj = pd = -1
    ex_pipe = None
    visited = set()
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                continue
            if board[i][j] == 'M':
                si = i
                sj = j
            elif board[i][j] == 'Z':
                ei = i
                ej = j
            else:
                visited.add((i, j))
    stk = [(si, sj, 0), (si, sj, 1), (si, sj, 2), (si, sj, 3)]  # 방향 하상우좌
    is_found_pos = False
    tmp_vst = set()
    while stk:
        n_stk = []
        while stk:
            i, j, d = stk.pop()
            ni = i + delta[d][0]
            nj = j + delta[d][1]
            if ni < 0 or nj < 0 or ni > R-1 or nj > C-1:
                continue
            if ni == ei and nj == ej and len(visited - tmp_vst) == 0:
                print(pi+1, pj+1, ex_pipe)
                return
            if board[ni][nj] == '.':
                continue
            if board[ni][nj] not in pipe[d]:
                continue
            if is_found_pos:
                tmp_vst.add((ni, nj))
            elif (ni, nj) in visited:
                visited.remove((ni, nj))
            nd = curve(d, board[ni][nj])
            n_stk.append((ni, nj, nd))
        if not n_stk:
            if not is_found_pos:
                is_found_pos = True
                ex_pipe_list = sorted(list(pipe[d]))
                pi = i + delta[d][0]
                pj = j + delta[d][1]
                pd = d
            ex_pipe = ex_pipe_list.pop()
            nd = curve(pd, ex_pipe)
            board[pi][pj] = ex_pipe
            tmp_vst.clear()
            n_stk.append((pi, pj, nd))
        stk = n_stk


if __name__ == '__main__':
    main()