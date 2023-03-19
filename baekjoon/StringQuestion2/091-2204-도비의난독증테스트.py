import sys


input = sys.stdin.readline
while (N:=int(input())) != 0:
    arr = [input().rstrip() for _ in range(N)]
    arr = sorted(arr, key=lambda x: str.lower(x))
    print(arr[0])
