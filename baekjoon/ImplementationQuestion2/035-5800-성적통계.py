import sys


def main():
    input = sys.stdin.readline
    K = int(input())
    for i in range(1, K+1):
        print(f"Class {i}")
        point = list(map(int, input().split()))
        point.pop(0)
        mx = max(point)
        mn = min(point)
        gap = 0
        prev = mx
        for p in sorted(point, reverse=True):
            if (temp := prev - p) > gap:
                gap = temp
            prev = p

        print(f"Max {mx}, Min {mn}, Largest gap {gap}")


if __name__ == '__main__':
    main()