## 힙 - 디스크 컨트롤러 (참조)
#출처: https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%94%94%EC%8A%A4%ED%81%AC-%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC-%ED%9E%99


from heapq import heappop,heappush,heapify

def solution(jobs):
    answer , now , i = 0,0,0
    start = -1
    heap = []
    
    
    while i < len(jobs):
        for j in jobs:
            # 디스크 처리 시작 지점이 now이내인 것들을 heap에 모음
            if start < j[0] <= now:
                heappush(heap,[j[1],j[0]])
        if heap:
            # heap중에서 처리시간이 가장 작은것을 선택
            current = heappop(heap)
            # current가 처리되므로 start를 now로 갱신
            start = now
            # current 처리 시간 만큼 Now 갱신
            now += current[0]
            # current 요청 시간부터 최종 완료 시간까지의 시간을 더함
            answer += (now-current[1])
            i += 1
        else:
            now += 1
    return int(answer/len(jobs))


# 그리디, 참조(승현)
def solution(jobs):
    n = len(jobs)
    
    jobs = sorted(jobs, key = lambda x:x[1])
    start = 0
    result = 0
    
    while jobs:
        for i in range(len(jobs)): 
            if jobs[i][0] <= start: 
                start += jobs[i][1] 
                result += start - jobs[i][0] 
                jobs.pop(i)
                break

            if i ==  len(jobs) - 1:
                start += 1
                
    return result // n