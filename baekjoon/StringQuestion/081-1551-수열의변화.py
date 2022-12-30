import sys

input = sys.stdin.readline
N, K = map(int, input().split())
arr = list(map(int, input().split(",")))

k = 0
while k < K:
    k += 1
    for i in range(N-k):
        arr[i] = arr[i+1] - arr[i]

ret = str(arr[0])
for i in range(1, N-K):
    ret += "," + str(arr[i])

print(ret)