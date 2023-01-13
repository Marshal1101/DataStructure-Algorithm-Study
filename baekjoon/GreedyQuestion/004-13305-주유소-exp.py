# https://www.acmicpc.net/source/54011877

def solution():
    N = int(input())
    dist = list(map(int,input().split()))
    price = list(map(int,input().split()))

    # print(N)
    # print(dist)
    # print(price)
    answer = 0

    local_min_price = price[0]


    for i in range(len(dist)):
      if price[i] < local_min_price:
        local_min_price = price[i]
      answer += local_min_price * dist[i]
        
    return answer

ret = solution()
print(ret)