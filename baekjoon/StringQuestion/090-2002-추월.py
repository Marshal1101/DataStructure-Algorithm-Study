# https://www.acmicpc.net/problem/2002

import sys
from collections import deque


input = sys.stdin.readline
N = int(input())
ans = 0
car_in_list = [input().rstrip() for _ in range(N)]
car_out_list = [input().rstrip() for _ in range(N)]
car_out_deque = deque(car_out_list)
car_out_set = set(car_out_list)

for ci in range(N):
    if not car_in_list[ci] in car_out_set: continue
    while car_out_deque and car_out_deque[0] != car_in_list[ci]:
        car_out_set.remove(car_out_deque.popleft())
        ans += 1
    if not car_out_deque: break
    else: car_out_deque.popleft()

print(ans)