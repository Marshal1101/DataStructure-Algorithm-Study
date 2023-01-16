import sys
input = sys.stdin.readline
n,k = map(int,input().split())
medals = []
for _ in range(n):
    x, g, s, b = map(int,input().split())
    medals.append((g, s, b))
    if x == k:
        k = (g, s, b)
medals.sort(reverse=True)
for i in range(n):
    if medals[i] == k:
        print(i+1)
        break