import sys, math


def LCA(n1, n2, K):
    o1 = h1 = math.floor(math.log(1 + n1*(K-1), K))
    o2 = h2 = math.floor(math.log(1 + n2*(K-1), K))

    if h1 < h2:
        n1, n2 = n2, n1
        h1, h2 = h2, h1

    while h1 != h2:
        if n1 % K == 0:
            n1 = (n1 // K) - 1
        else:
            n1 = (n1 // K)

        h1 -= 1

    while n1 != n2:
        if n1 % K == 0:
            n1 = (n1 // K) - 1
        else:
            n1 = (n1 // K)

        if n2 % K == 0:
            n2 = (n2 // K) - 1
        else:
            n2 = (n2 // K)


    lca_h = math.floor(math.log(1 + n1*(K-1), K))
    print(o1 + o2 - 2*lca_h)



def main():
    input = sys.stdin.readline
    N, K, Q = map(int, input().split())
    for _ in range(Q):
        n1, n2 = map(lambda x: int(x)-1, input().split())
        if K == 1:
            print(n1-n2 if n1 > n2 else n2-n1)
        else:
            LCA(n1, n2, K)


if __name__ == '__main__':
    main()