import sys


def main():
    input = sys.stdin.readline
    N, L = map(int, input().split())
    cpos = ctime = 0
    for _ in range(N):
        D, R, G = map(int, input().split())
        ctime += D - cpos
        cpos = D
        fr = ctime % (R + G)
        if 0 <= fr < R:
            ctime += R - fr
    ctime += L - cpos
    print(ctime)


if __name__ == '__main__':
    main()