N, K = map(int, input().split())
sw_H = []
sw_P = []
hptr = pptr = 0
arr = input().rstrip()
ans = 0
for i in range(N):
    if arr[i] == 'P':
        if hptr == len(sw_H):
            sw_P.append(i)
        else:
            while hptr != len(sw_H):
                if i - sw_H[hptr] <= K:
                    ans += 1
                    hptr += 1
                    break
                hptr += 1


    else:
        if pptr == len(sw_P):
            sw_H.append(i)
        else:
            while pptr != len(sw_P):
                if i - sw_P[pptr] <= K:
                    ans += 1
                    pptr += 1
                    break
                pptr += 1

print(ans)
