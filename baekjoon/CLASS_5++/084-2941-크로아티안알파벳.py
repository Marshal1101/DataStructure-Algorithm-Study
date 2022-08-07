import sys


string = sys.stdin.readline().rstrip()
cnt = 0
for i in range(len(string)):
    if i > 0 :
        if string[i] == 'j':
            if string[i-1] == 'l' or string[i-1] == 'n': continue
        elif string[i] == '=':
            if string[i-1] == 'c' or string[i-1] == 's': continue
            if string[i-1] == 'z' and i-1 > 0 and string[i-2] == 'd':
                cnt -= 1
                continue 
            else : continue
        elif string[i] == '-':
            if string[i-1] == 'c' or string[i-1] == 'd': continue
    cnt += 1

print(cnt)