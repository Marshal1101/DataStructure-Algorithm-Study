import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    stk = [int(input()) for _ in range(N)]
    stk.sort()

    ans = 0
    mult_on = False
    tmp = 0
    while stk and stk[-1] > 1:
        if mult_on:
            tmp *= stk.pop()
            ans += tmp
            tmp = 0
            mult_on = False
        else:
            tmp = stk.pop()
            mult_on = True
    
    if tmp > 0:
        ans += tmp

    while stk and stk[-1] == 1:
        ans += stk.pop()

    sp = 0
    while stk and stk[-1] == 0:
        sp += 1
        stk.pop()
    
    if len(stk) % 2:
        if sp == 0:
            ans += stk.pop()
        else:
            stk.pop()

    for i in range(0, len(stk), 2):
        ans += (stk[i] * stk[i+1])

    print(ans)


if __name__ == '__main__':
    main()