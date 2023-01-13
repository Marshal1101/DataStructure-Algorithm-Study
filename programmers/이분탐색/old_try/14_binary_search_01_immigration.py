## 이분탐색 - 입국심사 (구현)

n = 6
times = [7, 10]

def solution(n, times) :
    left = 0
    right = n * max(times)
    checked_people = 0
    min_time = 0
    while left <= right :
        mid = (left + right) // 2
        for work_t in times :
            checked_people += mid // work_t
        if checked_people >= n :
            right = mid - 1
            min_time = mid
        else :
            left = mid + 1
        checked_people = 0
    return min_time

print(solution(n, times))