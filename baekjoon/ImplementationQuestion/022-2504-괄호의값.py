import sys


input = sys.stdin.readline
stack = []
total = 0
isPossibleSum = True
for p in input().rstrip():
    if p == ')':
        if len(stack) == 0 or stack[-1] == '[':
            isPossibleSum = False
            break
        elif stack[-1] == '(':
            stack.pop()
            stack.append(2)
        else:
            tmpSum = 0
            while stack and stack[-1] != '(' and stack[-1] != '[':
                tmpSum += stack.pop()
            if len(stack) == 0 or stack[-1] == '[':
                isPossibleSum = False
                break
            stack.pop()
            stack.append(tmpSum * 2)
    elif p == ']':
        if len(stack) == 0 or stack[-1] == '(':
            isPossibleSum = False
            break
        elif stack[-1] == '[':
            stack.pop()
            stack.append(3)
        else:
            tmpSum = 0
            while stack and stack[-1] != '(' and stack[-1] != '[':
                tmpSum += stack.pop()
            if len(stack) == 0 or stack[-1] == '(':
                isPossibleSum = False
                break
            stack.pop()
            stack.append(tmpSum * 3)
    else:
        stack.append(p)

if isPossibleSum:
    try: print(sum(stack))
    except: print(0)
else: print(0)