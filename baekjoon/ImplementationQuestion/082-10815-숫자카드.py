import sys; input = sys.stdin.readline


N = int(input())
card = set(input().split())
M = int(input())
for num in input().split():
    if num in card:
        print(1, end=" ")
    else:
        print(0, end=" ")