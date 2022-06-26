## 스택, 큐 - 주식가격 (시간초과)


prices = [1, 2, 3, 2, 3]

def solution1(prices):
    n = len(prices)
    bullish = [0] * n
    while prices :
        last = prices.pop()
        n -= 1
        for i in range(n) :
            if prices[i] <= last :
                bullish[i] += 1
            else :
                bullish[i] = 1
    return bullish

print(solution1(prices))



## 참조 정답

def solution(prices):
    from collections import deque
    answer = []
    prices = deque(prices)
    
    while prices:
        now = prices.popleft()
        time = 0
        
        if prices:
            for i in prices:
                if i>= now:
                    time += 1
                else:
                    time += 1
                    break
        
        answer.append(time)
    
    return answer