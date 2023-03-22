N, L = map(int, input().split())
arr = sorted(map(int, input().split()))
tape_s = arr[0] - 0.5
i = 1
ans = 1
while i < len(arr):
    if arr[i] + 0.5 > tape_s + L:
        tape_s = arr[i] - 0.5
        ans += 1
    i += 1

print(ans)