import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    stk = []
    ans = 0
    for i in range(N):
        task = list(map(int, input().split()))
        if task[0] == 1:
            stk.append([task[1], task[2]-1])
        elif stk:
            stk[-1][1] -= 1

        if stk and stk[-1][1] == 0:
            point, _ = stk.pop()
            ans += point

    print(ans)


if __name__ == '__main__':
    main()