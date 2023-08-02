n,a,b=int(input()),*'* '
m=2*n-3
s=[a*n+b*m+a*n]
x=a+b*(n-2)+a
for i in range(1,n-1):s+=[b*i+x+b*(m-2*i)+x]
print(*s,b*(n-1)+x+x[1:],*s[::-1],sep='\n')