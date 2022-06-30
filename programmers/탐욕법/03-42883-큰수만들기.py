def solution(number, k):
    stack = []
    del_cnt = 0
    for num in number :
        while del_cnt != k and stack and stack[-1] < num :
            stack.pop()
            del_cnt += 1
        stack.append(num)
        
    while del_cnt < k :
        stack.pop()
        del_cnt += 1

    return "".join(stack)