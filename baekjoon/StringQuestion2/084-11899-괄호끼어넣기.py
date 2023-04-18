brk = list(input().rstrip())
cnt = ans = 0
while brk:
    c = brk.pop()
    if c == ')':
        cnt += 1
    else:
        if not cnt:
            ans += 1
        else:
            cnt -= 1

print(ans + cnt)