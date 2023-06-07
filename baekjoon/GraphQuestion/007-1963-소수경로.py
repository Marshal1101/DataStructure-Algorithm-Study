import sys
from collections import deque


def is_prime(num: int):
    if num < 2:
        return False
    elif num == 2:
        return True
    limit = round(num ** (1/2)) + 1
    for i in range(2, limit):
        if num % i == 0:
            return False
    return True

def set_graph(n, primes: dict):
    if n not in primes:
        primes[n] = set()
    
    n1 = n // 1000
    n2 = (n // 100) % 10
    n3 = (n // 10) % 10
    n4 = n % 10

    for i in range(1, 10):
        if (i != n1):
            if (adj := i*1000 + n2*100 + n3*10 + n4) in primes:
                primes[adj].add(n)
                primes[n].add(adj)

    for i in range(0, 10):
        if (i != n2):
            if (adj := n1*1000 + i*100 + n3*10 + n4) in primes:
                primes[adj].add(n)
                primes[n].add(adj)
        if (i != n3):
            if (adj := n1*1000 + n2*100 + i*10 + n4) in primes:
                primes[adj].add(n)
                primes[n].add(adj)
        if (i != n4):
            if (adj := n1*1000 + n2*100 +n3*10 + i) in primes:
                primes[adj].add(n)
                primes[n].add(adj)


def bfs(sp, ep, primes: dict):
    if sp == ep: return 0
    visited = {sp}
    queue = deque([(sp, 0)])
    while queue:
        cp, cnt = queue.popleft()
        for adj in primes[cp]:
            if adj == ep:
                return cnt + 1
            if adj not in visited:
                queue.append((adj, cnt+1))
                visited.add(adj)
    return -1

def main():
    input = sys.stdin.readline
    primes = dict()
    for n in range(1000, 10000):
        if is_prime(n):
            set_graph(n, primes)

    T = int(input())
    for _ in range(T):
        sp, ep = map(int, input().split())
        if (sp not in primes and ep not in primes):
            print("Impossible")
            continue

        cnt = bfs(sp, ep, primes)
        if cnt != -1: print(cnt)
        else: print("Impossible")


if __name__ == '__main__':
    main()