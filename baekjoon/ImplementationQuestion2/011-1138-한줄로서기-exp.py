N=int(input())
h=list(map(int,input().split()))[::-1]
o=[]
for i in h:
    o.insert(i,N)
    N-=1
print(*o)