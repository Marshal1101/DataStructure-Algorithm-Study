import sys


def main():
    input = sys.stdin.readline
    r1, c1, r2, c2 = map(int, input().split())
    tmp = [[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]

    sl = 0
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            v = str(value(i, j))
            tmp[i-r1][j-c1] = v
            if len(v) > sl:
                sl = len(v)

    ans = ""
    for a in tmp:
        for v in a:
            if (vl:=len(v)) < sl:
                v = " "*(sl-vl) + v
            ans += v + " "
        ans += '\n'

    print(ans)

"""
(-n, n) = 4*n**2 - 2*n**2 + 1
(-n, -n) = 4*n**2 + 1
(n, -n) = 4*n**2 + 2*n + 1
(n, n) = 4*n**2 + 4*n + 1
"""
def value(r, c):
    if r == 0 and c == 0:
        return 1

    # n = r
    if abs(r) >= abs(c):
        n = abs(r)

        # (n, n) - (n, c)
        if r > 0:
            var = 4*n**2 + 4*n + 1
            dif = n - c
        # (-n, -n) - (-n, c)
        else:
            var = 4*n**2 + 1
            dif = c - (-n)

    # n = c
    else:
        n = abs(c)

        # (-n, n) - (r, n)
        if c > 0:
            var = 4*n**2 - 2*n + 1
            dif = r - (-n)
        # (-n, -n) - (r, -n)
        else:
            var = 4*n**2 + 2*n + 1
            dif = n - r
    
    return var - dif



if __name__ == '__main__':
    main()