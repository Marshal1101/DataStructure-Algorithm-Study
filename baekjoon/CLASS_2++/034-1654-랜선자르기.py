import sys

input = sys.stdin.readline

k, n = map(int, input().split())
arr = list(int(input()) for _ in range(k))
arr.sort(reverse=True)
lp = 0
rp = arr[0]
cnt = 0
maxLen = 0
while (rp != 0 and lp <= rp) :
    cnt = 0
    mid = (lp + rp) // 2
    # if (n <= (arr[0] // mid) * k) :
    for line in arr :
        cnt += line // mid
    if cnt < n :
        rp = mid - 1
    else :
        maxLen = max(maxLen, mid)
        lp = mid + 1
    # else : lp = mid + 1

print(maxLen)