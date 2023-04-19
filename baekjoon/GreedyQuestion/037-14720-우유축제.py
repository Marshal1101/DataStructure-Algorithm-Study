N = int(input())
arr = list(map(int, input().split()))
s = c = b = -1
is_start = False
for i in range(N):
    if not is_start:
        if arr[i] == 0:
            s = 1
            is_start = True
        continue

    if arr[i] == 0:
        s = max(s, b + 1)
    elif arr[i] == 1:
        c = max(c, s + 1)
    elif c != -1:
        b = max(b, c + 1)

print(max(s, c, b))