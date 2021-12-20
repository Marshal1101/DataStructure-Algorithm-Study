## heap - 더 맵게

import heapq


scoville = [1, 2, 3, 9, 10, 12]
K = 7

def solution(scoville, K) :
    hq = []
    for i in scoville :
        heapq.heappush(hq, i)

    cnt = 0
    scov1 = heapq.heappop(hq)
    while scov1 < K :
        # K보다 작았다면 큐에서 꺼내려 한다.
        try :
            scov2 = heapq.heappop(hq)
            new_one = scov1 + (scov2 * 2)
            heapq.heappush(hq, new_one)
            cnt += 1
            scov1 = heapq.heappop(hq)
        # 꺼낼 것이 없는데, 꺼내려고 했다면 K 만들기 불가능
        except :
            return -1
    return cnt

print(solution(scoville, K))