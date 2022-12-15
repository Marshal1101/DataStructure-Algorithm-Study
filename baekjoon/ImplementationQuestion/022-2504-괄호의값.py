import sys


input = sys.stdin.readline
stack = []
total = 0
openCnt = 0
isClosed = True
for p in input().rstrip():
    if p == ')':
        if len(stack) == 0 or stack[-1] == '[':
            isClosed = False
            break
        elif stack[-1] == '(':
            stack.pop()
            stack.append(2)
        else:
            tmpSum = 0
            while stack and stack[-1] != '(' and stack[-1] != '[':
                tmpSum += stack.pop()
            if len(stack) == 0 or stack[-1] == '[':
                isClosed = False
                break
            stack.pop()
            stack.append(tmpSum * 2)
        openCnt -= 1
    elif p == ']':
        if len(stack) == 0 or stack[-1] == '(':
            isClosed = False
            break
        elif stack[-1] == '[':
            stack.pop()
            stack.append(3)
        else:
            tmpSum = 0
            while stack and stack[-1] != '(' and stack[-1] != '[':
                tmpSum += stack.pop()
            if len(stack) == 0 or stack[-1] == '(':
                isClosed = False
                break
            stack.pop()
            stack.append(tmpSum * 3)
        openCnt -= 1
    else:
        stack.append(p)
        openCnt += 1

if isClosed and openCnt == 0:
    print(sum(stack))
else: print(0)