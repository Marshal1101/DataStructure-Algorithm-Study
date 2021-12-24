## 이중순위우선큐 (구현)

# 명령어	수신 탑(높이)
# I 숫자	큐에 주어진 숫자를 삽입합니다.
# D 1	큐에서 최댓값을 삭제합니다.
# D -1	큐에서 최솟값을 삭제합니다.

from heapq import heappop, heappush
import sys

input = sys.stdin.readline

k = int(input())
for i in range(k) :
    n = int(input())
    min_heap = []
    max_heap = []
    heap_cnt = 0
    for j in range(n) :
        order, num = input().split()
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
        print(-heappop(max_heap), heappop(min_heap))
    else :
        print("EMPTY")