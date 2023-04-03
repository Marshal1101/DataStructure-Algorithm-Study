change = int(input())
cnt = 0

while change > 0 :
    if change % 5 == 0:
        cnt += change // 5
        change %= 5
        break
    else:
        change -= 2
        cnt += 1
        
if change != 0:
    print(-1)
else:
    print(cnt)

## https://www.acmicpc.net/source/54739298

n=int(input())
k=2*n//5+(n%5!=0)
M=n//2
if k>M:
    print(-1)
else:
    print(3*k-n)


## https://www.acmicpc.net/source/54101525
n = int(input())
for i in range(n//5,-1,-1):
  k = n-5*i
  if k%2==0:
    print(i+k//2)
    break
else:
  print(-1)