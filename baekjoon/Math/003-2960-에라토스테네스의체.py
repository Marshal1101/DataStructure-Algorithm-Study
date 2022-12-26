import sys


def count_del_prime(N, K):
    deleted_cnt = 0
    sieve = [True] * (N + 1)
    for i in range(2, N + 1):
        if sieve[i]:
            for j in range(i, N+1, i):
                if sieve[j]:
                    sieve[j] = False
                    deleted_cnt += 1
                    if deleted_cnt == K:
                        return j

N, K = map(int, sys.stdin.readline().split())
print(count_del_prime(N, K))