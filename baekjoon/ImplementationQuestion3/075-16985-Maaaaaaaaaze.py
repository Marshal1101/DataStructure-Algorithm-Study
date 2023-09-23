import sys
from itertools import permutations

def get_rotate_clockwise(board):
    ret = list(map(list, zip(*[line[:] for line in board])))
    for r in ret:
        r.reverse()
    return ret

def bfs(h, r, cube, delta):
    visited = set()
    visited.add((0, 0, 0))
    qstk = [(0, 0, 0)]
    moved = 0
    while qstk:
        n_qstk = []
        while qstk:
            i, j, k = qstk.pop()
            for di, dj, dk in delta:
                ni = i + di
                nj = j + dj
                nk = k + dk
                if ni < 0 or nj < 0 or nk < 0:
                    continue
                if ni > 4 or nj > 4 or nk > 4:
                    continue
                if not cube[h[ni]][r[ni]][nj][nk]:
                    continue
                if (ni, nj, nk) in visited:
                    continue
                if ni == 4 and nj == 4 and nk == 4:
                    return moved + 1
                visited.add((ni, nj, nk))
                n_qstk.append((ni, nj, nk))

        if n_qstk:
            moved += 1
            qstk = n_qstk

    return -1


def main():
    input = sys.stdin.readline
    cube = [ [ [] for _ in range(4) ] for _ in range(5) ]
    delta = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    # 보드 입력
    for i in range(5):
        for j in range(5):
            cube[i][0].append(list(map(int, input().split())))

        # 회전된 보드 생성 입력
        for rot in range(1, 4):
            cube[i][rot] = get_rotate_clockwise(cube[i][rot-1])

    # 보드 스택 순서 생성, h[0] 맨 위, h[4] 맨 아래
    ans = sys.maxsize
    for h in permutations(range(5), 5):
        for r0 in range(4):
            if not cube[h[0]][r0][0][0]:
                continue
            for r4 in range(4):
                if not cube[h[4]][r4][4][4]:
                    continue
                for r1 in range(4):
                    for r2 in range(4):
                        for r3 in range(4):
                            r = [r0, r1, r2, r3, r4]
                            ret = bfs(h, r, cube, delta)
                            if ret != -1 and ret < ans:
                                ans = ret
                                if ans == 12:
                                    print(12)
                                    return
    
    if ans != sys.maxsize:
        print(ans)
    else:
        print(-1)


if __name__ == '__main__':
    main()