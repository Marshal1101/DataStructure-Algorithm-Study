import sys


def round_odd(num):
    t = num - int(num)
    if t < 0.5:
        return int(num)
    else:
        return int(num) + 1


def main():
    input = sys.stdin.readline
    N = int(input())
    if N == 0:
        print(0)
        return
    
    point = [int(input()) for _ in range(N)]
    total = sum(point)
    cutoff = round_odd(N * 0.15)
    if cutoff != 0:
        point.sort()
        for i in range(cutoff):
            total -= point[i]
        for i in range(N-1, N-1-cutoff, -1):
            total -= point[i]
        print(round_odd(total / (N-2*cutoff)))

    else:
        print(round_odd(total / N))


if __name__ == '__main__':
    main()