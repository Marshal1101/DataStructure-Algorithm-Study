import sys


input = sys.stdin.readline

N = 0
while (line := input().rstrip())[0] != "-":
    N += 1
    stack = []
    cnt = 0
    for c in line:
        if not stack:
            if c == "}":
                cnt += 1
                stack.append("{")
            else: stack.append(c)

        else:
            if c == "}":
                if stack[-1] == "{":
                    stack.pop()
                else: stack.append(c)
            else:
                stack.append(c)

    cnt += len(stack)//2
    # while stack and stack[-1] == "{":
    #     stack.pop() 
    #     cnt += 1
    #     stack.pop()
    print(f"{N}. {cnt}")