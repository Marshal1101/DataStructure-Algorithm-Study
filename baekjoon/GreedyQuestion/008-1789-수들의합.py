N = int(input())
s = 0
i = 1
cnt = 0
while s != N:
    if s + i > N:
        s -= i - 1
        cnt -= 1
    else:
        s += i
        cnt += 1
        i += 1

print(cnt)


# print(int((-1 + (1 + 8*N)**0.5)/2))