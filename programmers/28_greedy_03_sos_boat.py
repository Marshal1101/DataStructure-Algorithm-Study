## 그리디 - 구명보트 (미구현)

from bisect import bisect_left, bisect_right
from collections import deque

def solution(people, limit):
    answer = 0
    n = len(people)
    sorted_people = sorted(people)
    min_weight = sorted_people[0]
    new_n = bisect_right(sorted_people, limit - min_weight)
    answer += n - new_n

    queue = deque(sorted_people[:new_n])
    
    if n == 0 :
        return answer
    if n == 1 :
        return answer + 1

    status = False
    while queue :
        big = queue.pop()
        if status == False :
            try :
                small = queue.popleft()
            except :
                return answer + 1
        total = big + small
        if total > limit :
            answer += 1
            status = True
        else :
            answer += 1
            status = False
    if status == True :
        answer += 1                 

    return answer

print(solution([70, 50, 80, 50], 100))