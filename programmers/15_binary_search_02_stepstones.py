## 이분탐색 - 징검다리 (참조: https://deok2kim.tistory.com/122)


def solution(distance, rocks, n):
    answer = 0
    rocks.sort()  
    rocks.append(distance)
    
    left, right = 0, distance
    while left <= right:
        # 거리의 최솟값을 mid로 설정
        # (거리가 mid 이하이면 다 없앤다)
        mid = (left + right) // 2  
        min_distance = float('inf')  # 각 mid 최솟값을 저장
        current = 0  # 현재 위치
        remove_cnt = 0  # 제거한 바위 개수
        
        # 거리 재기 스타트
        for rock in rocks:
            diff = rock - current  # 바위와 현재 위치 사이의 거리
            if diff < mid:  # mid 보다 거리가 짧으면 바위 제거
                remove_cnt += 1
            else:  
            # mid 보다 거리가 길거나 같으면 바위 그대로 두고
                current = rock  # 현재 위치를 그 바위로 옮기고
                min_distance = min(min_distance, diff)
        
        # mid를 설정하는 단계
        # 바위를 너무 많이 제거 했다. mid를 줄여서 바위를 조금만 제거하자
        if remove_cnt > n:  
            right = mid - 1

        # 바위를 너무 적게 제거했다 and 딱 맞다.
        # mid를 늘려서 바위를 더 제거하거나 mid의 최댓값을 올려보자
        else:  
            answer = min_distance
            left = mid + 1

    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))



# 테스트 1 〉	통과 (0.32ms, 10.3MB)
# 테스트 2 〉	통과 (0.29ms, 10.2MB)
# 테스트 3 〉	통과 (0.24ms, 10.3MB)
# 테스트 4 〉	통과 (15.49ms, 10.4MB)
# 테스트 5 〉	통과 (14.72ms, 10.4MB)
# 테스트 6 〉	통과 (129.41ms, 12.2MB)
# 테스트 7 〉	통과 (186.50ms, 12.3MB)
# 테스트 8 〉	통과 (182.61ms, 12.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.3MB)