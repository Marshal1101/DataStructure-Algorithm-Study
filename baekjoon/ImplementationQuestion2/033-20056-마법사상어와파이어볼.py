import sys
from collections import defaultdict


def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    fireball = defaultdict(list)
    for _ in range(M):
        r, c, m, s, d = map(int, input().split())
        fireball[(r, c)].append((m, s, d))

    delta = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    
    while K > 0:
        new_fireball = defaultdict(list)
        for pos, fire in fireball.items():
            i, j = pos
            while fire:
                m, s, d = fire.pop()
                ni = (i + s * delta[d][0]) % N
                nj = (j + s * delta[d][1]) % N
                new_fireball[(ni, nj)].append((m, s, d))

        for n_pos, n_fire in new_fireball.items():
            if (fcnt := len(n_fire)) < 2: continue
            nm, ns, nd = n_fire.pop()
            while n_fire:
                m, s, d = n_fire.pop()
                nm += m
                ns += s
                if nd != -1:
                    if (nd % 2) != (d % 2):
                        nd = -1

            if nm // 5 != 0:
                if nd != -1:
                    for d in range(0, 7, 2):
                        new_fireball[n_pos].append((nm//5, ns//fcnt, d))
                else:
                    for d in range(1, 8, 2):
                        new_fireball[n_pos].append((nm//5, ns//fcnt, d))

        fireball = new_fireball
        K -= 1

    total_m = 0
    for fire in fireball.values():
        for m, s, d in fire:
            total_m += m

    print(total_m)


if __name__ == '__main__':
    main()