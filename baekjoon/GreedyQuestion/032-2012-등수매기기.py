import sys; input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)])
ans = 0
for i in range(N):
    ans += abs((i+1) - arr[i])

print(ans)