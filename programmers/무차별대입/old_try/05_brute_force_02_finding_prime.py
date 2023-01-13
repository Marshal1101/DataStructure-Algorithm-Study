## 완전탐색 - 소수 찾기 (참조)
from itertools import permutations
import math

numbers = "17"

def is_prime_number(x):
    k = math.sqrt(x)
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    if x < 2:
        return False

    for i in range(2, int(k)+1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임


def solution(numbers):
    n = len(numbers)
    answer = []
    for k in range(1, n+1) :
        pool = list(map(''.join, permutations(list(numbers), k)))
        for num in list(set(pool)) :
            if is_prime_number(int(num)) :
                answer.append(int(num))

    return len(set(answer))

print(solution(numbers))