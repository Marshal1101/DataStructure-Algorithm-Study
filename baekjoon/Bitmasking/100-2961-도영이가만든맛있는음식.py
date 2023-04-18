N = int(input())
ans = 1e9 + 1
stk = []
for _ in range(N):
    s, b = map(int, input().split())
    tmp = abs(s - b)
    if tmp < ans:
        ans = tmp
    for i in range(len(stk)):
        xs, xb = stk[i]
        ts = s * xs
        tb = b + xb
        tmp = abs(ts - tb)
        if tmp < ans:
            ans = tmp
        stk.append((ts, tb))
    stk.append((s, b))

print(ans)