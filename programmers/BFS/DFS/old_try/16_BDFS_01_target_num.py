## 타겟 넘버 (스터디 디버깅 치료 받음)

cnt = 0

    
def solution(numbers, target):
    
    def DFS(value, idx, end, target) :
        global cnt
        if idx == end :
            if value == target :
                return 1
            return
        DFS(value + numbers[idx+1], idx+1, end, target)
        DFS(value - numbers[idx+1], idx+1, end, target)
    
    idx = 0
    end = len(numbers) - 1
    start = numbers[idx]
    global cnt
    DFS(start, idx, end, target)
    DFS(-start, idx, end, target)
    return cnt


# 테스트 1 〉	통과 (342.14ms, 10.2MB)
# 테스트 2 〉	통과 (315.78ms, 10.2MB)
# 테스트 3 〉	통과 (0.31ms, 10.3MB)
# 테스트 4 〉	통과 (1.27ms, 10.2MB)
# 테스트 5 〉	통과 (10.11ms, 10.2MB)
# 테스트 6 〉	통과 (0.61ms, 10.4MB)
# 테스트 7 〉	통과 (0.31ms, 10.2MB)
# 테스트 8 〉	통과 (2.53ms, 10.2MB)