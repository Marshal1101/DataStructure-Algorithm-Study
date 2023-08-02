N, K = input().split()
nl = len(N)
N = int(N)
K = int(K)
i = 1
sn = 1
en = 10
cl = 0
while i <= nl:
    if cl + (en - sn) * i < K:
        cl += (en - sn) * i
        en *= 10
        sn *= 10
        i += 1
        continue
    else:
        break

# print('else', i, cl, en, sn)
d, m = divmod(K-cl, i)
# print(d, m)
sn += d if m else d - 1
# print('sn', sn)
if sn > N:
    print(-1)
elif m == 0:
    print(str(sn)[-1])
else:
    print(str(sn)[m-1])

