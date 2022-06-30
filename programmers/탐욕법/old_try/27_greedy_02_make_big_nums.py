## 그리디 - 큰 수 만들기 (미구현)   
## 어제 오늘 느낀 바 알고리즘 안 풀리면 혼자서 안 되니까 그만하고, 구글 동료의 도움을 받아라.


from collections import defaultdict, deque
import sys


def solution(number, k):
    answer = ''
    num_list = list(map(int,number))
    n = len(num_list)
    print(num_list)
    if n == 1 :
        return number
    p = n - k
    mid = 5
    cnt = 0
    pre_cnt = 0
    index = defaultdict(list)
    switch = -1
    while True :
        for i in range(n) :
            if num_list[i] >= mid :
                index[mid].append(i)
                cnt += 1
        if cnt == p :
            if switch == 1 :
                return make_str_answer(index[mid], num_list)
            else : ## switch == 0
                del_cnt = 0
                for i in index[mid] :
                    if num_list[i] == mid :
                        del index[mid][i]
                        del_cnt += 1
                    else :
                        break
                for i in range(n-1, 0, -1) :

                if index[mid][-1] < n-1 :
                    
                pre_cnt = cnt - del_cnt
                mid -= 1
                cnt = 0
                continue

        elif cnt > p :
            if switch == 0 :        ## pre_cnt < p < cnt
                diff = (p - pre_cnt)
                ans_list = detail(mid, index[mid], num_list, diff)
                return make_str_answer(ans_list, num_list)
                # for j in range(m) :
                #     answer += index[mid+1][j]
                # return answer
            # if pre_cnt < p :
            mid += 1
            switch = 1
        else :
            ## cnt < p
            if switch == 1 :        ## cnt < p < pre_cnt 
                diff = (p - cnt)
                ans_list = detail(mid-1, index[mid-1], num_list, diff)
                return make_str_answer(ans_list, num_list)
            else :
                mid -= 1
                switch = 0
        pre_cnt = cnt
        cnt = 0

def detail(idx, idx_list, num_list, need_cut) :
    cnt = 0
    while cnt < need_cut :
        if num_list[idx_list[0]] == idx :
            del idx_list[0]
            cnt += 1
    return idx_list

def make_str_answer(list, num_list) :
    answer = '' 
    for v in list :
        answer += str(num_list[v])
    return answer





## 알고리즘은 원리를 알면 개 깔끔이다.


def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
        
    return ''.join(answer[:len(answer) - k])


print(solution("8", 0))
print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("4177252841", 8))
print(solution("12345678901234567890", 19))