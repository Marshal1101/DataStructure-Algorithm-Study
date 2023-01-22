import sys
input = sys.stdin.readline
N = int(input())
s = input().rstrip()
ans = 0
num = ""
for c in s:
    if c.isdigit():
        num += c
    
    else:
        if len(num):
            ans += int(num)
            num = ""

if len(num): ans += int(num)
print(ans)