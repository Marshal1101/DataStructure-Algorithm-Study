import sys


def throw(flag, h, R, C, board: list[list], mnl_pos: set):
    ret = []
    if not flag:
        for j in range(C):
            if board[h][j] == 'x':
                board[h][j] = '.'
                mnl_pos.remove((h, j))
                if h > 0 and board[h-1][j] == 'x':
                    ret.append((h-1, j))
                if h < R-1 and board[h+1][j] == 'x':
                    ret.append((h+1, j))
                if j > 0 and board[h][j-1] == 'x':
                    ret.append((h, j-1))
                if j < C-1 and board[h][j+1] == 'x':
                    ret.append((h, j+1)) 
                break
    else:
        for j in range(C-1, -1, -1):
            if board[h][j] == 'x':
                board[h][j] = '.'
                mnl_pos.remove((h, j))
                if h > 0 and board[h-1][j] == 'x':
                    ret.append((h-1, j))
                if h < R-1 and board[h+1][j] == 'x':
                    ret.append((h+1, j))
                if j > 0 and board[h][j-1] == 'x':
                    ret.append((h, j-1))
                if j < C-1 and board[h][j+1] == 'x':
                    ret.append((h, j+1)) 
                break
    return ret


def bfs_chk(si, sj, board: list[list], mnl_pos: set):
    is_on_air = True
    R = len(board)
    C = len(board[0])
    mnl_pos.remove((si, sj))
    cur_mnl_pos = [(si, sj)]
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    stk = [(si, sj)]
    while stk:
        next_stk = []
        while stk:
            i, j = stk.pop()
            for di, dj in delta:
                ni = i + di
                nj = j + dj
                if ni < 0 or nj < 0 or ni >= R or nj >= C:
                    continue
                if board[ni][nj] == '.':
                    continue
                if (ni, nj) not in mnl_pos:
                    continue
                mnl_pos.remove((ni, nj))
                cur_mnl_pos.append((ni, nj))
                next_stk.append((ni, nj))
                if ni == R-1:
                    is_on_air = False
        stk = next_stk
    
    if is_on_air:
        return cur_mnl_pos
    else:
        return []


def mnl_down(pmnl_pos, board: list[list], mnl_pos: set):
    R = len(board)
    C = len(board[0])
    col_h = [-1] * C
    for i, j in pmnl_pos:
        if i > col_h[j]:
            col_h[j] = i
    # print("1", col_h)

    for j in range(C):
        if col_h[j] == -1:
            continue
        for i in range(col_h[j]+1, R):
            if board[i][j] == 'x':
                col_h[j] = i-1 - col_h[j]
                break
        else:
            col_h[j] = R-1 - col_h[j]
    
    # print("2", col_h)
    mh = R
    for j in range(C):
        if col_h[j] != -1 and col_h[j] < mh:
            mh = col_h[j]

    pmnl_pos.sort(reverse=True)
    for i, j in pmnl_pos:
        board[i][j] = '.'
        mnl_pos.remove((i, j))
        board[i+mh][j] = 'x'
        mnl_pos.add((i+mh, j))



def main():
    input = sys.stdin.readline
    R, C = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(R)]
    mnl_pos = set()
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'x':
                mnl_pos.add((i, j))

    N = int(input())
    is_right_turn = 0
    for h in map(int, input().split()):
        around = throw(is_right_turn, R-h, R, C, board, mnl_pos)
        is_right_turn = not is_right_turn
        # print(h, around)
        # for b in board:
        #     print(*b, sep='')
        mnl_pos_cpy = mnl_pos.copy()
        pmnl_pos_list = []
        for i, j in around:
            if (i, j) not in mnl_pos_cpy:
                continue
            ret = bfs_chk(i, j, board, mnl_pos_cpy)
            if ret:
                pmnl_pos_list.append(ret)
        # print("pmnl_pos_list", pmnl_pos_list)
        for pmnl_pos in pmnl_pos_list:
            mnl_down(pmnl_pos, board, mnl_pos)

    # print("last")
    for b in board:
        print(*b, sep='')


if __name__ == '__main__':
    main()