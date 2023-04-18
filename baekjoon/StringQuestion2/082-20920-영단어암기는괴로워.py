import sys
from collections import defaultdict

input = sys.stdin.readline
N, M = map(int, input().split())
cnt = defaultdict(int)
for _ in range(N):
    word = input().strip()
    if len(word) < M:
        continue
    cnt[word] += 1
print(*map(lambda k: k[0], sorted(list(cnt.items()), key=lambda x: (-x[1], -len(x[0]), x[0]))), sep="\n")