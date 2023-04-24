import sys

def power(team:int, s:list[list]) -> int:
    ret = 0
    tmp = []
    for i in range(team.bit_length()):
        if team & 1<<i:
            tmp.append(i)
    for i in tmp:
        for j in tmp:
            ret += s[i][j]
    return ret


def main():
    input = sys.stdin.readline
    ans = sys.maxsize
    N = int(input())
    s = [list(map(int, input().split())) for _ in range(N)]
    used = set()
    total = (1 << N) - 1
    for team1 in range(1, 1<<N):
        if team1 in used:
            break
        team2 = total ^ team1
        p1 = power(team1, s)
        p2 = power(team2, s)
        tmp = abs(p1 - p2)
        if tmp == 0:
            print(0)
            return
        if tmp < ans:
            ans = tmp
        used.add(team2)

    print(ans)

if __name__ == '__main__':
    main()