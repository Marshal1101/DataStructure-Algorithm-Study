import sys


def sec_to_mmss(sec:int) -> str:
    m = sec // 60
    s = sec % 60
    return str(m).zfill(2) + ":" + str(s).zfill(2)

def mmss_to_sec(mmss:str) -> int:
    mm, ss = map(int, mmss.split(":"))
    return mm * 60 + ss

def main():
    input = sys.stdin.readline
    N = int(input())
    time = 0
    twin1 = twin2 = 0
    score = [0, 0, 0]
    is_team1_win = -1
    for _ in range(N):
        team, mmss = input().split()
        sec = mmss_to_sec(mmss)
        if is_team1_win == 1:
            twin1 += sec - time
        elif is_team1_win == 0:
            twin2 += sec - time
        score[int(team)] += 1
        if score[1] > score[2]:
            is_team1_win = 1
        elif score[2] > score[1]:
            is_team1_win = 0
        else:
            is_team1_win = -1
        time = sec
    if is_team1_win == 1:
        twin1 += 48*60 - time
    elif is_team1_win == 0:
        twin2 += 48*60 - time
    
    print(sec_to_mmss(twin1))
    print(sec_to_mmss(twin2))


if __name__ == '__main__':
    main()