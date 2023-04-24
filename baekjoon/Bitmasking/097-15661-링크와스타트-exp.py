# https://www.acmicpc.net/source/18162413

import sys
input = sys.stdin.readline
M = int(sys.stdin.readline())
N = M // 2
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
row = [sum(i) for i in stat]
col = [sum(i) for i in zip(*stat)]
newstat = [i+ j for i, j in zip(row, col)]
allstat = sum(newstat) // 2
newstat.sort()
c = [0]
for i in newstat[:N]:
    c.extend([i + j for j in c])
bot_up = [False] * (allstat + 1)
for i in c:
    bot_up[i] = True
for i in newstat[N:]:
    bot_up[i:] = [a or b for a, b in zip(bot_up[i:], bot_up)]
for i in range(allstat, -1, -1):
    if bot_up[i]:
        print(allstat - i)
        break