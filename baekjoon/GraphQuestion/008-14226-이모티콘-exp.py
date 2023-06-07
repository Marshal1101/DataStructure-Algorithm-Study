INF = 999999999999999999
s = int(input())
num = [i for i in range(1005)]
i=1
while i<=s:
    j=2
    num[i-1]=min(num[i-1], num[i]+1)
    while i*j<1002:
        num[i*j] = min(num[i*j], num[i]+j)
        num[i*j-1] = min(num[i*j-1], num[i*j]+1)
        j+=1
    i+=1

print(num[s])