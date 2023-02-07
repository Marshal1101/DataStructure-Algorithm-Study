import sys
from collections import deque


def bfs_find_goal(si, sj, gi, gj, F, N, board, psg, delta):
    visited = set()
    visited.add((si, sj))
    q = deque([(si, sj)])
    move = 0
    while q and move < F:
        move += 1
        for _ in range(len(q)):
            i, j = q.popleft()
            for k in range(4):
                ni = i + delta[k][0]
                nj = j + delta[k][1]
                if ni < 0 or ni >= N or nj < 0 or nj >= N or board[ni][nj] == 1 or (ni, nj) in visited: continue
                if ni == gi and nj == gj:
                    del psg[(si, sj)]
                    return F + move

                visited.add((ni, nj))
                q.append((ni, nj))

    return -1


def bfs_find_psg(si, sj, F, N, board, psg, delta):
    if not psg: return F

    if (si, sj) in psg:
        gi, gj = psg[(si, sj)]
        nf = bfs_find_goal(si, sj, gi, gj, F, N, board, psg, delta)
        si, sj = gi, gj
        if nf != -1 and psg: bfs_find_psg(gi, gj, nf, N, board, psg, delta)
        else:
            print(nf)
            sys.exit(0)

    visited = set()
    queue = deque()
    visited.add((si, sj))
    queue.append((si, sj))
    move = 0
    while queue and move < F:
        move += 1
        found = []
        for _ in range(len(queue)):
            i, j = queue.popleft()
            for k in range(4):
                ni = i + delta[k][0]
                nj = j + delta[k][1]
                if ni < 0 or ni >= N or nj < 0 or nj >= N or board[ni][nj] == 1 \
                    or (ni, nj) in visited: continue
                if (ni, nj) in psg:
                    found.append((ni, nj))
                visited.add((ni, nj))
                queue.append((ni, nj))

        if found:
            found.sort()
            ni, nj = found[0]
            gi, gj = psg[(ni, nj)]
            nf = bfs_find_goal(ni, nj, gi, gj, F-move, N, board, psg, delta)
            if nf != -1 and psg:
                bfs_find_psg(gi, gj, nf, N, board, psg, delta)
            else:
                print(nf)
                sys.exit(0)
                
    print(-1)
    sys.exit(0)


def main():
    input = sys.stdin.readline
    N, M, F = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    ti, tj = map(lambda x: int(x)-1, input().split())
    psg = dict()
    for _ in range(M):
        pi, pj, gi, gj = map(lambda x: int(x)-1, input().split())
        psg[(pi, pj)] = (gi, gj)

    delta = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    bfs_find_psg(ti, tj, F, N, board, psg, delta)


if __name__ == '__main__':
    main()