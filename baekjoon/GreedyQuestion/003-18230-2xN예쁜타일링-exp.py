n, a, b = map(int, input().split()) 
li1 = sorted(list(map(int, input().split()))) 
li2 = sorted(list(map(int, input().split())))    
ans = 0 

if n % 2 == 1: 
    ans += li1[-1] 
    li1.pop(-1) 
    n -= 1 
     
for _ in range(0, n, 2): 
    t1, t2 = 0, 0 
    if len(li1) >= 2: 
        t1 = li1[-1] + li1[-2] 
    if len(li2) >= 1: 
        t2 = li2[-1] 
         
    if t1 > t2: 
        ans += t1 
        li1.pop(); li1.pop() 
    else: 
        ans += t2 
        li2.pop() 

print(ans)