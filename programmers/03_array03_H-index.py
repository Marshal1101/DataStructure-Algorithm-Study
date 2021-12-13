## 정렬 - H-index (구현)

citations =  [1, 1, 5, 7, 6]

def solution(citations):
    citations.sort()
    n = len(citations)
    left = 0
    right = n - 1
    max_h = 0
    while left <= right :                   ## left < right 아닌 left <= right 해야 구현됨, 왜?
        mid = (left + right) // 2
        if citations[mid] >= n -  mid :
            max_h = n - mid
            right = mid - 1
        else :
            left = mid + 1

    return max_h

print(solution(citations))