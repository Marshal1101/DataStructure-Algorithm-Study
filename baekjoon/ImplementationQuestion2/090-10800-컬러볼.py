import sys
from collections import defaultdict


def main():
    input = sys.stdin.readline
    N = int(input())
    player = []
    ans = [0] * N
    for i in range(N):
        C, S = map(int, input().split())
        player.append((S, C, i))

    player.sort()
    total = 0
    cl_size = defaultdict(int)
    tmp_sz = defaultdict(int)
    pcl = psz = 0
    for sz, cl, i in player:
        if sz != psz:
            for tcl in tmp_sz:
                cl_size[tcl] += tmp_sz[tcl]
            cl_size[pcl] += psz
            total += tmp_sz[0] + psz
            tmp_sz.clear()
        else:
            tmp_sz[0] += psz
            tmp_sz[pcl] += psz
        ans[i] = total - cl_size[cl]
        pcl = cl
        psz = sz
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()