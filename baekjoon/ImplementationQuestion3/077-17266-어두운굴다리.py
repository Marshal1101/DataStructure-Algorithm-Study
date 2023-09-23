import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    pos = [*map(int, input().split())]
    ans = 0
    if pos[0] != 0:
        ans = pos[0]
    for i in range(1, M):
        tmp = pos[i] - pos[i-1]
        tmp = tmp // 2 + 1 if tmp % 2 else tmp // 2
        if tmp > ans:
            ans = tmp
    if pos[-1] != N:
        if N - pos[-1] > ans:
            ans = N - pos[-1]

    print(ans)


if __name__ == '__main__':
    main()