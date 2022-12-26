# https://www.acmicpc.net/problem/2167

import sys


input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[0]]
for _ in range(N):
    line = list(map(int, input().split()))
    line[0] += arr[-1][-1]
    for i in range(1, len(line)):
        line[i] += line[i-1]
    arr.append([arr[-1][-1]] + line)

K = int(input())
for _ in range(K):
    ans = 0
    i, j, x, y = map(int, input().split())
    for n in range(i, x+1):
        ans += arr[n][y] - arr[n][j-1]

    print(ans)