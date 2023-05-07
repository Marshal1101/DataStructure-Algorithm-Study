import sys
from bisect import bisect_left


def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        A = list(map(int, input().split()))
        B = sorted(map(int, input().split()))
        ans = 0
        for a in A:
            val = bisect_left(B, a)
            ans += val
        print(ans)



def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        A = sorted(map(int, input().split()))
        B = sorted(map(int, input().split()))
        ap = bp = 0
        ans = 0
        while ap < N and bp < M:
            if A[ap] > B[bp]:
                bp += 1
            else:
                ans += bp
                ap += 1

        if ap < N:
            ans += bp
            ans += (N-1 - ap) * M

        print(ans)


if __name__ == '__main__':
    main()