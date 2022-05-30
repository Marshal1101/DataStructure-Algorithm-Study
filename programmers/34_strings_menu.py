## 문자열 - 매뉴 리뉴얼 (참조 승현) 


from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for course_num in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), course_num)
            temp += combi
        course_set = Counter(temp)
# Counter({('X', 'Y'): 2, ('W', 'X'): 2, ('X', 'Z'): 1, ('Y', 'Z'): 1, ('W', 'Y'): 1, ('A', 'W'): 1, ('A', 'X'): 1})
# Counter({('X', 'Y', 'Z'): 1, ('W', 'X', 'Y'): 1, ('A', 'W', 'X'): 1})
        if len(course_set) != 0 and max(course_set.values()) != 1:
            for f in course_set :
                if course_set[f] == max(course_set.values()) :
                    answer.append(''.join(f))
                
    return sorted(answer)
