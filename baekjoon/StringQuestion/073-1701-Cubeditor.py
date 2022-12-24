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


target = sys.stdin.readline().rstrip()
ans = 0
for i in range(len(target)):
    substr = target[i:]
    pi = compute_prefix(substr)
    if (tmp := max(pi)) > ans:
        ans = tmp
print(ans)