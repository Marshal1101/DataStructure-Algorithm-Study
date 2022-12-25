import sys


def check_divisor(n):
    divisor = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisor.append(i)
            if i != int(n/i):
                divisor.append(int(n/i))
    return divisor


def get_sum_divisor(n):
    ret = 0
    for i in range(1, n+1):
        if i % 2 == 0: ret += n // i
        else: ret -= n // i
    return ret


S, T = map(int, sys.stdin.readline().split())
print(get_sum_divisor(T) - get_sum_divisor(S-1))