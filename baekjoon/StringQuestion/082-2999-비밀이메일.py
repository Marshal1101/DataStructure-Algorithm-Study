import sys


pwd = sys.stdin.readline().rstrip()
N = len(pwd)
R = 0
for i in range(1, int(N**0.5) + 1):
    if N % i == 0: R = i

ans = ""
C = N // R
for i in range(R):
    for j in range(i, N, R):
        ans += pwd[j]

print(ans)
