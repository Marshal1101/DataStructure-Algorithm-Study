import sys


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    board = [input().rstrip() for _ in range(N)]
    visited = set()
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    ri = rj = bi = bj = hi = hj = cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == '#' or board[i][j] == '.':
                continue
            if board[i][j] == 'R':
                ri = i
                rj = j
            if board[i][j] == 'B':
                bi = i
                bj = j
            if board[i][j] == 'O':
                hi = i
                hj = j
    visited.add((ri, rj, bi, bj))
    stack = [(ri, rj, bi, bj, cnt+1, "")]
    turn = ['U', 'R', 'D', 'L']
    while stack:
        next_stack = []
        while stack:
            ri, rj, bi, bj, cnt, path = stack.pop()
            # cnt > 10 이상이면 -1
            if cnt > 10:
                print(-1)
                return

            for k in range(4):  # 상 우 하 좌
                np = turn[k]
                red_into_hole = False
                blue_into_hole = False
                nri, nrj, nbi, nbj = ri, rj, bi, bj
                # 레드 이동, 구멍 체크
                while board[nri+di[k]][nrj+dj[k]] != '#':
                    nri += di[k]
                    nrj += dj[k]
                    if nri == hi and nrj == hj:
                        red_into_hole = True
                        break

                # 블루 이동, 구멍 체크
                while board[nbi+di[k]][nbj+dj[k]] != '#':
                    nbi += di[k]
                    nbj += dj[k]
                    if nbi == hi and nbj == hj:
                        blue_into_hole = True
                        break

                if blue_into_hole:
                    continue

                if red_into_hole:
                    print(cnt)
                    print(path + np)
                    return

                # 레드 블루 위치 겹치는 경우 체크, 위치 조정
                if nri == nbi and nrj == nbj:
                    # 상
                    if k == 0:
                        if ri < bi:
                            nbi += 1
                        else:
                            nri += 1
                    # 우
                    elif k == 1:
                        if rj < bj:
                            nrj -= 1
                        else:
                            nbj -= 1
                    # 하
                    elif k == 2:
                        if ri < bi:
                            nri -= 1
                        else:
                            nbi -= 1
                    # 좌
                    else:
                        if rj < bj:
                            nbj += 1
                        else:
                            nrj += 1

                # 방문 체크
                if not (nri, nrj, nbi, nbj) in visited:
                    visited.add((nri, nrj, nbi, nbj))
                    next_stack.append((nri, nrj, nbi, nbj, cnt+1, path+np))

        stack = next_stack

    print(-1)


if __name__ == '__main__':
    main()