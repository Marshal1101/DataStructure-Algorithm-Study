from heapq import heappop, heappush
from sys import stdin

n = int(stdin.readline())
univ = sorted( [tuple(map(int, stdin.readline().split())) for _ in range(n)] , key=lambda x: x[1])

ans = []
for pay, day in univ:
    heappush(ans, pay)

    if day < len(ans):
        heappop(ans)
print(sum(ans))