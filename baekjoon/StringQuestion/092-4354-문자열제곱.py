import sys


def compute_prefix(target: str) -> list:
    M = len(target)
    pi = [0] * M

    k = 0
    for q in range(1, M):
        while k > 0 and target[k] != target[q]:
            k = pi[k-1]
        if target[k] == target[q]:
            k += 1
        pi[q] = k

    return pi


input = sys.stdin.readline
while (s := input().rstrip()) != ".":
    pi = compute_prefix(s)
    if pi[-1] == 0: print(1)
    else:
        div = len(s) - pi[-1]
        if pi[-1] % div == 0: print(len(s)//div)
        else: print(1)
