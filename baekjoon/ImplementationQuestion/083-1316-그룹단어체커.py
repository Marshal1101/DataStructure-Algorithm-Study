import sys; input = sys.stdin.readline


T = int(input())
cnt = 0
for _ in range(T):
    used = set()
    arr = input().rstrip()
    before = ''
    for i in range(len(arr)):
        if before != arr[i] and arr[i] in used:
            break
        elif before != arr[i]:
            used.add(arr[i])
            before = arr[i]
    else: cnt += 1
print(cnt)