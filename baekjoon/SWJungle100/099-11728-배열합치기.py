import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

n = 0
m = 0
ans = []
while n < N or m < M:

    if n == N:
        ans.extend(B[m:])
        break
    if m == M:
        ans.extend(A[n:])
        break

    if A[n] > B[m]:
        ans.append(B[m])
        m += 1
    else:
        ans.append(A[n])
        n += 1

print(" ".join(map(str, ans)))