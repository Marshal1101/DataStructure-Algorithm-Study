## 이중순위우선큐 (구현)

# 명령어	수신 탑(높이)
# I 숫자	큐에 주어진 숫자를 삽입합니다.
# D 1	큐에서 최댓값을 삭제합니다.
# D -1	큐에서 최솟값을 삭제합니다.

from heapq import heappop, heappush


operation = ["I 7","I 5","I -5","D -1"] 

def solution(operation):
    min_heap = []
    max_heap = []
    heap_cnt = 0
    for oper in operation :
        # 문자와 숫자 split
        order, num = oper.split(' ')
        if order == "I" :
            heappush(min_heap, int(num))
            heappush(max_heap, -int(num))
            heap_cnt += 1
        elif order == "D" :
            if heap_cnt > 0 :
                if num == "-1" :
                    heappop(min_heap)
                elif num == "1" :
                    heappop(max_heap)
                heap_cnt -= 1
                # 힙 카운트 0이 되면 한 번은 pop이 되었던 숫자들만 남음
                # 최대 최소 힙을 비움 list.clear()
                if heap_cnt == 0 :
                    min_heap.clear()
                    max_heap.clear()
                    
    if heap_cnt > 0 :
        answer = [-heappop(max_heap), heappop(min_heap)]
    else :
        answer = [0, 0]
    return answer

print(solution(operation))




# 바이섹트 인소트

import bisect

def solution(operations):
    num = []
    for op in operations:
        op = op.split()
        
        # Insert 명령
        if op[0] == "I":
            # 아무것도 없으면 그냥 넣고
            if len(num) == 0: num.append(int(op[1]))
            else: bisect.insort(num, int(op[1])) 
        # Delete 명령
        else:
            if len(num) == 0: continue
            # 최소값 제거
            if op[1] == "-1":
                num.pop(0)
            # 최대값 제거
            else:
                num.pop()
    # 결과 반환
    if len(num) == 0: 
        return [0,0]
    else: 
        return [num[-1], num[0]]