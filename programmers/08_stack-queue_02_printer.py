## 스택, 큐 - 프린터 (구현)

from collections import deque
priorities = [1, 1, 9, 1, 1, 1]
location = 0

def solution(priorities, location) :
    queue = deque([])
    for i, value in enumerate(priorities) :
        queue.append((value, i))
    target = -1
    printed_pages = 0
    while target != location :
        max_value, useless = max(queue)
        now_value, now_idx = queue.popleft()
        if now_value != max_value :
            queue.append((now_value, now_idx))
        else :
            printed_pages += 1
            target = now_idx

    return printed_pages

print(solution(priorities, location))


## 프로그래머스 다른 풀이
#
# def solution(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]
#     answer = 0
#     while True:
#         cur = queue.pop(0)
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer