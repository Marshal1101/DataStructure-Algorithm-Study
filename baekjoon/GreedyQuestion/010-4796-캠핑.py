import sys


def main():
    input = sys.stdin.readline
    k = 0
    while True:
        k += 1
        L, P, V = map(int, input().split())
        if L == 0: return

        ans = 0
        d, v = divmod(V, P)
        ans += d * L
        if v >= L:
            ans += L
        else:
            ans += v
        print(f"Case {k}: {ans}")

if __name__ == '__main__':
    main()