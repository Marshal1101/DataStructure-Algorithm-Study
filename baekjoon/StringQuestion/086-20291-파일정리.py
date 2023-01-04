import sys
from collections import defaultdict

input = sys.stdin.readline
N = int(input())
dic = defaultdict(int)
for i in range(N):
    dic[input().rstrip().split(".")[1]] += 1

arr = list(dic.items())
arr.sort()

for key, value in arr:
    print(f"{key} {value}")