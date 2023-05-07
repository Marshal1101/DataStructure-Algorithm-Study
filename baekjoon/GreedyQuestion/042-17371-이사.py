import sys
import math


def main():
    input = sys.stdin.readline
    N = int(input())
    pos = [tuple(map(int, input().split())) for _ in range(N)]
    mx, my = pos[0]
    max_l = sys.maxsize
    for i in range(N):
        cx, cy = pos[i]
        cml = 0
        for j in range(N):
            px, py = pos[j]
            l = math.sqrt((cx-px)**2 + (cy-py)**2)
            if l > cml:
                cml = l
        if cml < max_l:
            max_l = cml
            mx, my = cx, cy

    print(mx, my)


if __name__ == '__main__':
    main()