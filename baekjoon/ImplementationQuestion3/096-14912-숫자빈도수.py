n, d = input().split()
ans = 0
for i in range(1, int(n)+1):
    for j in str(i):
        if j == d:
            ans += 1
print(ans)