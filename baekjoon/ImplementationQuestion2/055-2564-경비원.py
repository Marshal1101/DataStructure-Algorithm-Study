import sys


def main():
    input = sys.stdin.readline
    C, R = map(int, input().split())
    N = int(input())
    # (p북남서동 1234, d왼쪽 또는 상단으로부터 거리)
    store = [list(map(int, input().split())) for _ in range(N)]
    Xp, Xd = map(int, input().split())
    ans = 0
    for p, d in store:
        if Xp == 1:
            if p == 1:
                ans += abs(Xd - d)
            elif p == 2:
                ans += R + min(Xd+d, 2*C-Xd-d)
            elif p == 3:
                ans += Xd + d
            elif p == 4:
                ans += (C-Xd) + d
            
        elif Xp == 2:
            if p == 1:
                ans += R + min(Xd+d, 2*C-Xd-d)
            elif p == 2:
                ans += abs(Xd - d)
            elif p == 3:
                ans += (R-d) + Xd
            elif p == 4:
                ans += (R-d) + (C-Xd)

        elif Xp == 3:
            if p == 1:
                ans += Xd + d
            elif p == 2:
                ans += (R-Xd) + d
            elif p == 3:
                ans += abs(Xd - d)
            elif p == 4:
                ans += C + min(Xd + d, 2*R-Xd-d)
        
        elif Xp == 4:
            if p == 1:
                ans += Xd + C-d
            elif p == 2:
                ans += R-Xd + C-d
            elif p == 3:
                ans += C + min(Xd+d, 2*R-Xd-d)
            elif p == 4:
                ans += abs(Xd - d)

    print(ans)


if __name__ == '__main__':
    main()