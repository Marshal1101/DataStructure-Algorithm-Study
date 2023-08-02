def clockwise(n: list):
    twt=[]
    for _ in range(4):
        twt.append("".join(n))
        n.insert(0,n.pop())
    return min(twt)
n=list(input().split())
m=clockwise(n)
c=0
used = set()
for j in range(1111, int(m)):
    j = str(j)
    sj = list(j)
    if "0" in sj:
        continue
    cj = clockwise(sj)
    if cj in used:
        continue
    used.add(j)
    c+=1
    
print(c+1)