import sys


input = sys.stdin.readline
N = int(input())
arr = sorted([int(input()) for _ in range(N)], reverse=True)
for i in range(2, N, 3):
    arr[i] = 0

print(sum(arr))