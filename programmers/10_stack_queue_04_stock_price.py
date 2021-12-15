## 스택, 큐 - 주식가격 (시간초과)


prices = [1, 2, 3, 2, 3]

def solution(prices):
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

print(solution(prices))