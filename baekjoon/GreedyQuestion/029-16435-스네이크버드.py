N, L = map(int, input().split())
for f in sorted(map(int, input().split())):
    if f <= L:
        L += 1
    else:
        print(L)
        break
else:
    print(L)