import sys


def main():
    rope = list(map(int, sys.stdin.readlines()))
    N = rope[0]
    rope[0] = 0
    rope.sort()
    for i in range(1, N+1):
        w = (N+1-i) * rope[i]
        if w > rope[0]:
            rope[0] = w

    print(rope[0])


if __name__ == '__main__':
    main()