## 11720 숫자의 합 (구현)

import sys
input = sys.stdin.readline

n = input()
number = input().strip()
ans = 0
for num in number :
    ans += int(num)
print(ans)