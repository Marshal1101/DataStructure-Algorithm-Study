import sys

input = sys.stdin.readline
A, B = map(int, input().split())
arr = []
n = 1
while len(arr) < B:
    for _ in range(n):
        arr.append(n)
    n += 1

print(sum(arr[A-1:B]))