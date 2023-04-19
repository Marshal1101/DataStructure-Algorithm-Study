N = int(input())
arr = list(map(int, input().split()))
ans = 0
seq = 0
prev = arr[0]
for i in range(1, N):
    if arr[i] < prev:
        seq += 1
    else:
        if seq > ans:
            ans = seq
        seq = 0
        prev = arr[i]
if seq > ans:
    ans = seq
print(ans)