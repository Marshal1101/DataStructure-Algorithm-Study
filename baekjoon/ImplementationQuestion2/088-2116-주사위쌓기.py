import sys
sys.setrecursionlimit(10**9)

def main():
    input = sys.stdin.readline
    N = int(input())
    roll = [list(map(int, input().split())) for _ in range(N)]
    global ans
    ans = 0
    for bot in range(1, 7):
        bf(0, bot, N, roll, 0)

    print(ans)


def bf(i, bot, N, roll: list[list], total):
    global ans
    if i == N:
        if ans < total:
            ans = total
        return
    
    sj = roll[i].index(bot)
    # 0-5, 1-3, 2-4
    if sj == 0: ej = 5
    elif sj == 1: ej = 3
    elif sj == 2: ej = 4
    elif sj == 3: ej = 1
    elif sj == 4: ej = 2
    elif sj == 5: ej = 0

    max_num = 6
    if bot == 6:
        max_num = 5
        if roll[i][ej] == 5:
            max_num = 4
    if roll[i][ej] == 6:
        max_num = 5
        if bot == 5:
            max_num = 4

    bf(i+1, roll[i][ej], N, roll, total + max_num)


if __name__ == '__main__':
    main()