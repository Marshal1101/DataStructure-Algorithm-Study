# https://www.acmicpc.net/source/54447929

import sys


def main():
    input = sys.stdin.readline

    left = list(input().rstrip())
    right = []

    for _ in range(int(input())):
        args = input().split()
        command = args[0]
        if command == "L":
            if left:
                right.append(left.pop())
        elif command == "D":
            if right:
                left.append(right.pop())
        elif command == "B":
            if left:
                left.pop()
        else:
            left.append(args[1])

    print("".join(left), "".join(reversed(right)), sep="")


if __name__ == "__main__":
    sys.exit(main())
