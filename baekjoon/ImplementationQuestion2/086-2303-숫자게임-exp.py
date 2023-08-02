from sys import stdin
input = stdin.readline
ans, n = 0, 0
for i in range(1, int(input())+1):
    l = list(map(int, input().split()))
    tmp, s = 0, sum(l)
    for j in range(5):
        for k in range(j+1, 5):
            tmp = max(tmp, (s - l[j] - l[k]) % 10)
    if tmp >= n:
        n = tmp
        ans=i
print(ans)