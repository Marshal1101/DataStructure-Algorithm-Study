from collections import deque

def solution(people, limit):
    people.sort(reverse=True)
    cnt = 0
    people = deque(people)
    while people:
        pas1 = people.popleft()
        if len(people) :
            pas2 = people[-1]
            if pas1 + pas2 <= limit :
                people.pop()
        cnt += 1

    return cnt