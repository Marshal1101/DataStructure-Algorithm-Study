import sys


def main():
    input = sys.stdin.readline
    R, C, ZR, ZC = map(int, input().split())
    ans = ""
    for _ in range(R):
        line = ""
        for c in input().rstrip():
            line += c * ZC
        ans += (line + "\n") * ZR

    print(ans)


if __name__ == '__main__':
    main()