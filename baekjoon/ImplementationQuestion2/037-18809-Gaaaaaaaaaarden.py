import sys
from itertools import combinations


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def simulate(sel, selG, N, M, garden):
    GRpos = set()
    # color G: 3, R: 4
    for pos in sel:
        GRpos.add(pos)
        i, j = pos
        if pos in selG: garden[i][j] = 3
        else: garden[i][j] = 4

    flower_cnt = 0
    while len(GRpos) > 0:
        new_GRpos = set()

        for i, j in GRpos:
            color = garden[i][j]
            for d in range(4):
                ni = i + delta[d][0]
                nj = j + delta[d][1]
                if ni < 0 or ni >= N or nj < 0 or nj >= M or garden[ni][nj] == 0:
                    continue

                if garden[ni][nj] < 3:
                    garden[ni][nj] = color
                    new_GRpos.add((ni, nj))

                if garden[ni][nj] != color and (ni, nj) in new_GRpos:
                    flower_cnt += 1
                    new_GRpos.remove((ni, nj))
                    garden[ni][nj] = 0

        GRpos = new_GRpos

    return flower_cnt


def main():
    input = sys.stdin.readline
    N, M, G, R = map(int, input().split())
    garden = [list(map(int, input().split())) for _ in range(N)]
    start = []
    for i in range(N):
        for j in range(M):
            if garden[i][j] == 2:
                start.append((i, j))

    max_flower_cnt = 0
    for sel in combinations(start, G+R):
        for selG in combinations(sel, G):
            copy_garden = [g[:] for g in garden]
            cnt = simulate(sel, selG, N, M, copy_garden)
            if cnt >  max_flower_cnt:
                max_flower_cnt = cnt

    print(max_flower_cnt)

    
if __name__ == '__main__':
    main()