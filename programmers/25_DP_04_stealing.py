## DP - 도둑질 ()


money = [1000,1,0,1,2,1000,0]

def solution(money):
    n = len(money)
    dp1 = [0] * n
    dp2 = [0] * n

    dp1[0] = money[0]
    dp1[1] = money[1]
    dp1[2] = money[0] + money[2]

    dp2[0] = money[0]
    dp2[1] = money[1]
    dp2[2] = max(money[1], money[2])

    for i in range(3, n-1) :
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i], dp1[i-3] + money[i])

    for i in range(3, n) :
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])

    return max(dp1[n-2], dp2[n-1])

print(solution(money))

# 정확성  테스트
# 테스트 1 〉	통과 (0.22ms, 10.3MB)
# 테스트 2 〉	통과 (0.61ms, 10.2MB)
# 테스트 3 〉	통과 (0.33ms, 10.3MB)
# 테스트 4 〉	통과 (0.04ms, 10.3MB)
# 테스트 5 〉	통과 (0.17ms, 10.2MB)
# 테스트 6 〉	통과 (0.41ms, 10.3MB)
# 테스트 7 〉	통과 (0.28ms, 10.3MB)
# 테스트 8 〉	통과 (0.19ms, 10.3MB)
# 테스트 9 〉	통과 (1.14ms, 10.2MB)
# 테스트 10 〉	통과 (0.13ms, 10.4MB)
# 효율성  테스트
# 테스트 1 〉	통과 (659.50ms, 92.5MB)
# 테스트 2 〉	통과 (636.31ms, 87.1MB)
# 테스트 3 〉	통과 (602.87ms, 90.3MB)
# 테스트 4 〉	통과 (697.81ms, 91.2MB)
# 테스트 5 〉	통과 (495.79ms, 77.1MB)
# 테스트 6 〉	통과 (615.42ms, 87.8MB)
# 테스트 7 〉	통과 (358.41ms, 55.4MB)
# 테스트 8 〉	통과 (389.20ms, 56.9MB)
# 테스트 9 〉	통과 (394.09ms, 64.9MB)
# 테스트 10 〉	통과 (623.10ms, 88.6MB)


## 참조 (지윤)

def solution(money): 
    dp1 = [0] * len(money) 
    dp2 = [0] * len(money)
    
    dp1[0] = money[0] 
    for i in range(1, len(money) - 1): 
        #첫 번째 집 털었기 때문에 마지막집 제외 
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i]) 
        
    dp2[0] = 0 
    for i in range(1, len(money)): 
        # 첫번째 집 안털어서 (0) 마지막 집 고려대상
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i]) 
        
    return max(dp1[-2], dp2[-1])