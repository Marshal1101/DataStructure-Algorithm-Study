## 11816 8진수, 10진수, 16진수 (구현)

import sys
input = sys.stdin.readline

number = input().strip()
ans = 0
if number[0] != '0' :
    ans = int(number)
else :
    if number[1] != 'x' :
        number = list(number[1:])
        n = len(number) - 1
        for num in number :
            ans += int(num) * (8**n)
            n -= 1
    else :
        number = list(number[2:])
        n = len(number) - 1
        for num in number :
            if num == 'a' :
                s = 10
            elif num == 'b' :
                s = 11
            elif num == 'c' :
                s = 12
            elif num == 'd' :
                s = 13
            elif num == 'e' :
                s = 14
            elif num == 'f' :
                s = 15
            else :
                s = int(num)
            ans += s * (16**n)
            n -= 1
print(ans)