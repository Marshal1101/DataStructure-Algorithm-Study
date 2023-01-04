import sys


num = sys.stdin.readline().rstrip()

if len(num) == 1: print("NO")
else:
    right_val = 1
    for i in range(len(num)):
        if num[i] != '0':
            right_val *= int(num[i])

    left_val = 1
    is_yujin = False
    for i in range(len(num)):
        left_val *= int(num[i])
        right_val /= int(num[i])
        if left_val == right_val:
            is_yujin = True
            break

    if is_yujin: print("YES")
    else: print("NO")