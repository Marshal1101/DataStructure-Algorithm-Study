N, K = map(int, input().split())
if N.bit_count() <= K:
    print(0)
    exit()

ans = 0
for i in range(N.bit_length()):
    if N & 1 << i:
        N += 1 << i
        ans += 1 << i
        if N.bit_count() <= K:
            print(ans)
            break
else:
    print(-1)