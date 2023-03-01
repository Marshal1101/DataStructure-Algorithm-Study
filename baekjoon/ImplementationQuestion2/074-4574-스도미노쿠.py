import sys


# A1 -> (0, 0)
def pos_to_rc(pos: str) -> tuple:
    return ord(pos[0])-65, int(pos[1])-1


def check_domino(idx:int, empty_pos:list, board:list[list]):
    global domino, fixed_pos
    # 종료조건
    if idx == len(empty_pos):
        if len(domino) == 0:
            for b in board :
                print(''.join(map(str, b)))
            return 1
        return 0

    r, c = empty_pos[idx]
    n1 = board[r][c]
    # 이미 체크됨 다음
    if (r, c) in fixed_pos:
        return check_domino(idx+1, empty_pos, board)

    # 우
    if c+1 < 9 and not (r, c+1) in fixed_pos:
        n2 = board[r][c+1]
        dm = (n1, n2) if n1 < n2 else (n2, n1)
        if dm in domino:
            domino.remove(dm)
            fixed_pos.add((r, c))
            fixed_pos.add((r, c+1))
            ret = check_domino(idx+1, empty_pos, board)
            if ret:
                return 1
            domino.add(dm)
            fixed_pos.remove((r, c))
            fixed_pos.remove((r, c+1))

    # 하
    if r+1 < 9 and not (r+1, c) in fixed_pos:
        n2 = board[r+1][c]
        dm = (n1, n2) if n1 < n2 else (n2, n1)
        if dm in domino:
            domino.remove(dm)
            fixed_pos.add((r, c))
            fixed_pos.add((r+1, c))
            ret = check_domino(idx+1, empty_pos, board)
            if ret:
                return 1
            domino.add(dm)
            fixed_pos.remove((r, c))
            fixed_pos.remove((r+1, c))
    
    return 0


def sudominoku(idx:int, empty_pos:list, board:list[list], Rv:list[list], Cv:list[list], Av:list[list]):
    if idx == len(empty_pos):
        return check_domino(0, empty_pos, board)

    si, sj = empty_pos[idx]        
    for num in range(1, 10):
        if (not Rv[si][num] and
            not Cv[sj][num] and
            not Av[si//3][sj//3][num]
            ) :
            Rv[si][num] = Cv[sj][num] = Av[si//3][sj//3][num] = True
            board[si][sj] = num

            ret = sudominoku(idx+1, empty_pos, board, Rv, Cv, Av)
            if ret: return ret

            board[si][sj] = ""
            Rv[si][num] = Cv[sj][num] = Av[si//3][sj//3][num] = False

    return 0


def main():
    input = sys.stdin.readline
    puzzle_num = 0
    while (N := int(input())) != 0:
        puzzle_num += 1
        print(f"Puzzle {puzzle_num}")
        # 숫자보드 생성, 행/열/사각/
        board = [[""] * 9 for _ in range(9)]
        Rv = [[False] * 10 for _ in range(9)]
        Cv = [[False] * 10 for _ in range(9)]
        Av = [[[False] * 10 for _ in range(3)] for _ in range(3)]
        
        # 도미노, 숫자 방문 생성
        global domino, fixed_pos
        domino = set()
        fixed_pos = set()
        for n1 in range(1, 10):
            for n2 in range(n1+1, 10):
                domino.add((n1, n2))
        
        # 초기 도미노 입력        
        for _ in range(N):
            u, lu, v, lv = input().split()
            u = int(u)
            v = int(v)
            if u < v:
                domino.remove((u, v))
            else:
                domino.remove((v, u))
            ur, uc = pos_to_rc(lu)
            vr, vc = pos_to_rc(lv)
            board[ur][uc] = u
            board[vr][vc] = v
            Rv[ur][u] = Cv[uc][u] = Av[ur//3][uc//3][u] = True
            Rv[vr][v] = Cv[vc][v] = Av[vr//3][vc//3][v] = True
            fixed_pos.add((ur, uc))
            fixed_pos.add((vr, vc))
        
        # 초기 숫자 입력
        for i, pos in enumerate(input().split()):
            r, c = pos_to_rc(pos)
            fixed_pos.add((r, c))
            board[r][c] = i+1
            Rv[r][i+1] = Cv[c][i+1] = Av[r//3][c//3][i+1] = True

        # 빈 좌표 리스트
        empty_pos = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == "":
                    empty_pos.append((r, c))

        # 백트래킹 시작
        sudominoku(0, empty_pos, board, Rv, Cv, Av)


if __name__ == '__main__':
    main()