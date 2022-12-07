import re, sys

input = sys.stdin.readline
N = int(input())
string= []
for _ in range(N):
    string.append(input().rstrip())

for i in string:
    p=re.compile('(100+1+|01)+')
    result=p.fullmatch(i)
    if result:
        print('YES')
    else:
        print('NO')