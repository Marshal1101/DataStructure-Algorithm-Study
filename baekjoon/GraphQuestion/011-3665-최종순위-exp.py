# 최종 순위
from sys import stdin
input = stdin.readline

T = int(input())
def solution():
    N = int(input())
    arr = list(map(int, input().split(' ')))
    in_degree = [0] * (N+1)
    for i,v in enumerate(arr):
        in_degree[v] = i
    # original_arr = copy.deepcopy(in_degree)
    original_arr = [*in_degree]
    I = int(input())
    for _ in range(I):
        t1, t2 = map(int, input().split(' '))
        front, back = 0, 0
        if original_arr[t1] < original_arr[t2]:
            front, back = t2, t1
        else:
            front, back = t1, t2
        in_degree[front] -= 1
        in_degree[back] += 1

    result = [0] * N
    for i, v in enumerate(in_degree):
        if not result[v]:
            result[v] = i
        else:
            return print('IMPOSSIBLE')
    return print(*result, sep=" ")

for _ in range(T):
    solution()