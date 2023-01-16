import sys

stack = list(sys.stdin.readline().rstrip())
flag = True
while (N := len(stack)) > 1:
    c = stack.pop()
    if c == "i" and stack[-1] == "p":
        stack.pop()
    elif c == "a" and stack[-1] == "k":
        stack.pop()
    elif c == "u":
        if len(stack) > 1 and stack[-1] == "h" and stack[-2] == "c":
            stack.pop()
            stack.pop()
        else:
            flag = False
            break
    else:
        flag = False
        break

if stack or not flag: print("NO")
else: print("YES")