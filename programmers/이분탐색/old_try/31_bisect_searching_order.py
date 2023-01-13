
from collections import defaultdict,deque
from itertools import combinations
def solution(info, query):
    answer = []
    
    def make_table(info):
        people = defaultdict(list)
        
        for p in info:
            p_list = p.split()
            grade = int(p_list.pop())
            for n in range(5):
                for i in list(combinations(p_list,n)):
                    people["".join(i)].append(grade)
        return people
    
    def make_q_list(r):
        
        # r_list = [ i for i in r.split() if i != "and" and i != "-"]

        r = r.replace(" and", "")
        r = r.replace("-","")
        r_list = r.split()
       
        r_grade = int(r_list.pop())
        
        return ["".join(r_list),r_grade]

    def cal_ans(key,people,grade):
        tmp = 0
    
        
        n = len(people[key])
        start , end = 0, n
        while start != end and start != n:
            mid = (start + end) // 2
            if people[key][mid] >= grade:
                end = mid
            else:
                start = mid + 1
        tmp += n - start
        return tmp
  
    people = make_table(info)

    for value in people.values():
        value.sort()

    for request in query:
        key , grade = make_q_list(request)
        
        answer.append(cal_ans(key,people,grade))    
                
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.20ms, 10.4MB)
# 테스트 2 〉	통과 (0.19ms, 10.4MB)
# 테스트 3 〉	통과 (0.33ms, 10.5MB)
# 테스트 4 〉	통과 (1.56ms, 10.6MB)
# 테스트 5 〉	통과 (2.36ms, 10.5MB)
# 테스트 6 〉	통과 (4.30ms, 10.5MB)
# 테스트 7 〉	통과 (3.45ms, 10.8MB)
# 테스트 8 〉	통과 (33.39ms, 11.5MB)
# 테스트 9 〉	통과 (36.49ms, 11.6MB)
# 테스트 10 〉	통과 (35.20ms, 11.6MB)
# 테스트 11 〉	통과 (2.39ms, 10.6MB)
# 테스트 12 〉	통과 (4.29ms, 10.6MB)
# 테스트 13 〉	통과 (3.40ms, 10.8MB)
# 테스트 14 〉	통과 (17.21ms, 11MB)
# 테스트 15 〉	통과 (17.41ms, 11MB)
# 테스트 16 〉	통과 (2.98ms, 10.5MB)
# 테스트 17 〉	통과 (4.26ms, 10.5MB)
# 테스트 18 〉	통과 (17.12ms, 11MB)
# 효율성  테스트
# 테스트 1 〉	통과 (705.85ms, 42.1MB)
# 테스트 2 〉	통과 (710.93ms, 42.7MB)
# 테스트 3 〉	통과 (637.84ms, 42.2MB)
# 테스트 4 〉	통과 (726.71ms, 42.3MB)

# 풀이2
def solution(info, query):
    answer = []
    dict_info = {
        "cpp" : -1,
        "java" : -2,
        "python" : -3,
        "backend" : 1,
        "frontend" : 0,
        "junior" : 1,
        "senior" : 0,
        "chicken" : 1,
        "pizza" : 0,
        "-" : 0
    }
    
    def make_table(info,dict_info):
        people = [[] for _ in range(42)]
        
        for p in info:
            x = 1
            lang , area , year , food , grade = p.split()
            x = (x << 2) + dict_info[lang]
            x = (x << 1) + dict_info[area]
            x = (x << 1) + dict_info[year]
            x = (x << 1) + dict_info[food]
            people[x].append(int(grade))
        return people
    
    def make_q_list(r,dict_info):
        r = r.replace(" and","")
        r_lang , r_area , r_year, r_food, r_grade = r.split()
        r_grade = int(r_grade)
        x_list = deque([])
    
        if r_lang == "-":
            x_list = deque([1,2,3])
        else:
            x_list.append((1 << 2) + dict_info[r_lang])
        if r_area == "-":            
            for _ in range(len(x_list)):
                now = x_list.pop()
                x_list.appendleft((now<<1)+1)
                x_list.appendleft((now<<1))
        else:
            for i in range(len(x_list)):
                x_list[i] = (x_list[i]<<1) + dict_info[r_area]
        if r_year == "-":            
            for _ in range(len(x_list)):
                now = x_list.pop()
                x_list.appendleft((now<<1)+1)
                x_list.appendleft((now<<1))
        else:
            for i in range(len(x_list)):
                x_list[i] = (x_list[i]<<1) + dict_info[r_year]
        if r_food == "-":            
            for _ in range(len(x_list)):
                now = x_list.pop()
                x_list.appendleft((now<<1)+1)
                x_list.appendleft((now<<1))
        else:
            for i in range(len(x_list)):
                x_list[i] = (x_list[i]<<1) + dict_info[r_food]

        return [x_list,r_grade]
    
    def cal_ans(r_list,people,grade):
        tmp = 0
        for y in r_list:
            
            n = len(people[y])
            start , end = 0, n
            while start != end and start != n:
                mid = (start + end) // 2
                if people[y][mid] >= grade:
                    end = mid
                else:
                    start = mid + 1
            tmp += n - start
        return tmp
  
    people = make_table(info,dict_info)
    
    for value in people:
        value.sort()
    
    for request in query:
        r_list , grade = make_q_list(request,dict_info)
        
        answer.append(cal_ans(r_list,people,grade))    
                
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.10ms, 10.5MB)
# 테스트 2 〉	통과 (0.09ms, 10.4MB)
# 테스트 3 〉	통과 (0.41ms, 10.5MB)
# 테스트 4 〉	통과 (3.70ms, 10.5MB)
# 테스트 5 〉	통과 (4.31ms, 10.6MB)
# 테스트 6 〉	통과 (3.18ms, 10.5MB)
# 테스트 7 〉	통과 (7.75ms, 10.7MB)
# 테스트 8 〉	통과 (4.92ms, 10.6MB)
# 테스트 9 〉	통과 (4.97ms, 10.7MB)
# 테스트 10 〉	통과 (5.53ms, 11MB)
# 테스트 11 〉	통과 (4.49ms, 10.5MB)
# 테스트 12 〉	통과 (3.07ms, 10.5MB)
# 테스트 13 〉	통과 (7.68ms, 10.6MB)
# 테스트 14 〉	통과 (3.43ms, 10.6MB)
# 테스트 15 〉	통과 (3.44ms, 10.7MB)
# 테스트 16 〉	통과 (4.86ms, 10.5MB)
# 테스트 17 〉	통과 (3.12ms, 10.5MB)
# 테스트 18 〉	통과 (3.74ms, 10.6MB)
# 효율성  테스트
# 테스트 1 〉	통과 (952.35ms, 35.8MB)
# 테스트 2 〉	통과 (968.97ms, 36.6MB)
# 테스트 3 〉	통과 (4317.33ms, 35.7MB)
# 테스트 4 〉	통과 (3903.76ms, 36.2MB)


import bisect

def solution(info, query):
    result = [0] * len(query)
    
    # info 전처리 하기
    info_dic = dict()
    for INFO in info:
        info_list = INFO.split()
        # print(info_list) : ['java', 'backend', 'junior', 'pizza', '150']

        key, value = tuple(info_list[:-1]), int(info_list[-1])
        if key in info_dic:
            bisect.insort(info_dic[key], value) # 정렬된 채로 넣기, bisect써도 되나..?
        else:
            info_dic[key] = [value]  
    # print(info_dic) : ('python', 'frontend', 'senior', 'chicken'): [150, 210]
    
    # query 전처리 하기
    query_list = []
    for string in query:
        # print(string) : java and backend and junior and pizza 100
        string_list = string.replace('-', '').replace(' and', '').split()
        # print(string_list) : ['java', 'backend', 'junior', 'pizza', '100']
        query_list.append((set(string_list[:-1]), int(string_list[-1])))
        # print(query_list) : ({'backend', 'java', 'pizza', 'junior'}, 100)
    
    
    for index, tup in enumerate(query_list):
        for infos, score in info_dic.items():
            # print(infos, score) : ('java', 'backend', 'junior', 'pizza') [150]
            if tup[0] <= set(infos):
                # print(tup[0], set(infos)) : {'backend', 'junior', 'pizza', 'java'} {'backend', 'junior', 'pizza', 'java'}
                result[index] += len(score) - bisect.bisect_left(score, tup[1])
                # print(len(score)) : 1
                # print(bisect.bisect_left(score, tup[1])) : 0
    
    return result