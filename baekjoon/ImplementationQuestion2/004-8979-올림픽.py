import sys
from collections import defaultdict

input = sys.stdin.readline
N, K = map(int, input().split())
record = [list(map(int, input().split())) for _ in range(N)]
record.sort(key=lambda x: x[0], reverse=True)
# print(f"N, K : {N} {K}")
same_rank = defaultdict(int)
rank = dict()
for nation, gld, slv, brz in record:
    rank[nation] = (gld, slv, brz, same_rank[(gld, slv, brz)])
    same_rank[(gld, slv, brz)] += 1 
    # print("input", nation, gld, slv, brz)

k = 0
grade = (-1, -1, -1)
for nation, (gld, slv, brz, same) in sorted(rank.items(), key=lambda x: (x[1][0], x[1][1], x[1][2], x[0]), reverse=True):
    # print("finding", nation, gld, slv, brz, "same:", same)
    k += 1
    if nation == K:
        print(k - same)
        break

