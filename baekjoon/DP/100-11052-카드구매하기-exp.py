from sys import stdin

input = stdin.readline


def sol(n: int, p: list) -> int:
    d: list = [0] + p
    for i in range(2, n + 1):
        l1 = d[:i//2+1]
        l2 = d[i:(i-1)//2:-1]
        d[i] = max([a + b for a, b in zip(d[:i//2+1], d[i:(i-1)//2:-1])])
        print(i, l1, l2, d)
    return d[n]


N = int(input())
P = list(map(int, input().rstrip().split()))
print(sol(N, P))
