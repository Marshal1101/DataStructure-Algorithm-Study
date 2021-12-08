## 완전탐색 - 모의고사 (구현)

from collections import deque

answers = [1, 3, 2, 4, 2]

def solution(answers):
    answer = []
    check = deque(answers)
    student1 = deque([1, 2, 3, 4, 5])
    student2 = deque([2, 1, 2, 3, 2, 4, 2, 5])
    student3 = deque([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    std1_point = 0
    std2_point = 0
    std3_point = 0
    while check :
        ans = check.popleft()
        std1_ans = student1.popleft()
        std2_ans = student2.popleft()
        std3_ans = student3.popleft()
        
        if ans == std1_ans :
            std1_point += 1            
        if ans == std2_ans :
            std2_point += 1         
        if ans == std3_ans :
            std3_point += 1

        student1.append(std1_ans)
        student2.append(std2_ans)
        student3.append(std3_ans)

    max_point = max(std1_point, std2_point, std3_point)
    if max_point == std1_point :
        answer.append(1)
    if max_point == std2_point :
        answer.append(2)
    if max_point == std3_point :
        answer.append(3)   
    return answer

print(solution(answers))





# 프로그래머스 좋아요 풀이
#
# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []

#     for idx, answer in enumerate(answers):
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1

#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)

#     return result