# https://www.acmicpc.net/source/53047753

import sys
from itertools import accumulate


def main() -> None:
    input = sys.stdin.readline

    n, m = map(int, input().split())
    acc = [[0] * (m + 1)]
    for i in range(1, n + 1):
        row = accumulate(map(int, input().split()), initial=0)
        row = [p + r for p, r in zip(acc[-1], row)]
        acc.append(row)
    ans = []
    for _ in range(int(input())):
        i, j, x, y = map(int, input().split())
        if i < x: r1 = i - 1; r2 = x
        else:     r1 = x - 1; r2 = i
        if j < y: c1 = j - 1; c2 = y
        else:     c1 = y - 1; c2 = j
        ans.append(acc[r1][c1] - acc[r1][c2] - acc[r2][c1] + acc[r2][c2])
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    sys.exit(main())
