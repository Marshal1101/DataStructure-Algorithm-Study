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



## 참조 (민수)

from collections import deque

alpha = ['A', 'B', 'C', 'D' ,'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def solution(name):
    answer = 0
    length = len(name)
    # 로직
    # 1. 각 자리마다 A가 원하는 문자가 될 때까지의 cnt를 answer에 더해준다. 
    # 2. 각 자리를 어느 순으로 이동할지에 대해서 bfs로 최소 경로를 구한다. 
    
    # 1. 원하는 문자 만들기
    for each in name:
        position = alpha.index(each)
        answer += min(position, 26 - position)

    #2. 이동에 대한 최소 경로수 찾기 (bfs) 
    q = deque([[0, name, 0]])
    while q:
        temp = q.popleft()
        for dx in [1, -1]:
            s_idx, string, cnt = temp[0], temp[1], temp[2]
            # 땜빵은 힘들다 1 (idx가 마이너스가 되면 아래 if문의 string 변경해주는 부분이 에러가 난다.)
            if s_idx < 0: s_idx += length
            
            # A가 아닌 부분이 나온다면 A로 변경한다. 
            if string[s_idx] != 'A':
                string = string[:s_idx] + 'A' + string[s_idx+1:]

            # 다 변경되었는지를 확인한다. 
            if length == string.count('A'):
                answer += cnt
                return answer
            # 다 변경 안되었을때 인덱스를 이동하면서 CNT를 늘려준다. 
            else:
                n_idx = s_idx + dx
                cnt += 1
                # 땜빵은 힘들다 2 (name의 길이 이상을 안 갖도록 미리미리 챙기자)         
                if  n_idx >= length: n_idx -= length
                elif n_idx <= -(length+1): n_idx -= length   
                q.append([n_idx, string, cnt])

print(solution("JEROEN"	))


# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.05ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.51ms, 10.3MB)
# 테스트 5 〉	통과 (1.07ms, 10.3MB)
# 테스트 6 〉	통과 (0.05ms, 10.3MB)
# 테스트 7 〉	통과 (0.57ms, 10.3MB)
# 테스트 8 〉	통과 (0.02ms, 10.2MB)
# 테스트 9 〉	통과 (0.07ms, 10.3MB)
# 테스트 10 〉	통과 (0.02ms, 10.3MB)
# 테스트 11 〉	통과 (0.04ms, 10.3MB)