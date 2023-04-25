import sys; input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
ans = 0
for a in A:
    a -= B
    ans += 1
    if a > 0:
        if a % C > 0:
            ans += a // C + 1
        else:
            ans += a // C

print(ans)
