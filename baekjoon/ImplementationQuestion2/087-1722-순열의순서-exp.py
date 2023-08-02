N = int(input())
NL = [x for x in range(1,N+1)]
L = [1]
x = 1
for i in range(N-1) :
    L.append(L[i]*x)
    x += 1
Q = list(map(int,input().split()))
if Q[0] == 1 :
    a = Q[1]-1
    while L :
       x = L.pop()
       print(NL[a//x],end=" ")
       NL.remove(NL[a//x])
       a %= x
else :
    a = Q[1:]
    res = 1
    idx = 0
    while L :
        x = L.pop()
        res += x*NL.index(a[idx])
        NL.remove(a[idx])
        idx += 1
    print(res)