import sys; input = sys.stdin.readline

def is_prime_number(num):
    if num < 2: return False
    if num == 2: return True
    limit = num ** 0.5 + 1
    for i in range(3, limit):
        if num % i == 0:
            return False
    return True


def main():
    P, K = map(int, input().split())
    for i in range(2, K):
        if is_prime_number(i) and P % i == 0:
            print("BAD", i)
            return
    print("GOOD")
    return
