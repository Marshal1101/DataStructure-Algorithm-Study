import sys


input = sys.stdin.readline
N = int(input())
stack = list(map(int, input().split()))
pop_num = [stack.pop()]
while stack and stack[-1] < pop_num[-1]:
    pop_num.append(stack.pop())

if not stack: print(-1)
else:
    bigk = stack.pop()
    tmp = -1
    for i in range(len(pop_num)):
        if pop_num[i] < bigk:
            tmp = pop_num[i]
            pop_num[i] = bigk
            break
    stack.append(tmp)
    stack.extend(pop_num)

    print(*stack)