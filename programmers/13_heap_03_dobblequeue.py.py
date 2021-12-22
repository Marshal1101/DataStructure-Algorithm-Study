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
        splited = oper.split(' ')
        if splited[0] == "I" :
            heappush(min_heap, int(splited[1]))
            heappush(max_heap, -int(splited[1]))
            heap_cnt += 1
        elif splited[0] == "D" :
            if heap_cnt > 0 :
                if splited[1] == "-1" :
                    heappop(min_heap)
                elif splited[1] == "1" :
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