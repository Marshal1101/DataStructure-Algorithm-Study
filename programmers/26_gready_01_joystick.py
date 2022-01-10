## 그리디 - 조이스틱 (미구현)

from collections import deque

name = "ZAAAZAZZZZZZ"  ## return 15

# # def solution(name):
#     capitals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     position = []
#     n = len(name)
#     a_idx = [False] * n
#     for i in range(n) :
#         order = capitals.index(name[i])
#         if not order :
#             a_idx[i] = True
#         position.append(order)

#     visited = [False] * n
#     stack = [0]
#     visited[0] = True
#     while stack :
#         idx = stack.pop()
#         if position[idx+1] :
#             if not visited[idx+1] :
#                 visited[idx+1] = True
#                 stack.append(idx+1)
#         else :
#             if position[idx-1] :
#                 if not visited[idx-1] :
#                     visited[idx-1] = True
#                     stack.append(idx-1)           
#                 else :


#     print(f'n: {n}, postion: {position}, right: {right}, left: {left}, a: {a}')

def solution(name):
    capitals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    position = []
    n = len(name)
    cnt_list = [0] * n
    right = 0
    right_l = 0
    is_last_right_before_a = True

    a = 0
    k = n // 2
    for i in range(k+1) :
        order = capitals.index(name[i])
        if order != 0 :
            if is_last_right_before_a :
                right_l = i
            right = i
            cnt_list[i] = i
        else :
            is_last_right_before_a = False
            a += 1
            
        if order > 13 :
            order = 26 - order
        position.append(order)
    
    left = 0
    left_r = 0
    is_first_left_after_a = True
    for i in range(n-1, k, -1) :
        order = capitals.index(name[i])
        if order != 0 :
            if is_first_left_after_a :
                left_r = i
            left = i
            cnt_list[i] = i
        else :
            is_first_left_after_a = False
            a += 1

        if order > 13 :
            order = 26 - order
        position.append(order)

    # print(f'n: {n}, postion: {position}, right: {right}, left: {left}, a: {a}')
    updown = sum(position)
    end = max(cnt_list)
    if not a :
        answer = n-1 + updown
    if right + 1 == left :
        if right_l == 0 or left_r == 0 :
            answer = min(end, 2*right_l + left+1, right+1 + 2*left_r) + updown
        else :
            answer = min(end, 2*right_l + left, right + 2*left_r) + updown
    else :
        if right > 0 and left > 0 :
            answer = min(end, right*2 + (n-left), right + (n-left)*2) + updown
        else :
            if right > 0 and left == 0 :
                answer = end + updown
            if right == 0 and left > 0 :
                answer = min(end + updown, n-left + updown)
            else :
                answer = end + updown

    # print(answer)
    return answer

print(solution(name))