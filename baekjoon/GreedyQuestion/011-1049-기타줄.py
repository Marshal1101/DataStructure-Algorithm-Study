import sys


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    # 기타 1세트 6줄
    set_p = []
    one_p = []
    for _ in range(M):
        sp, op = map(int, input().split())
        set_p.append(sp)
        one_p.append(op)

    sp = min(set_p)
    op = min(one_p)
    

    ans = 0
    if sp < op * 6:
        ans += sp * (N // 6)
    else:
        ans += op*6 * (N // 6)

    if N % 6 * op < sp:
        ans += N % 6 * op
    else:
        ans += sp
    print(ans)


if __name__ == '__main__':
    main()