import sys


input = sys.stdin.readline
N = int(input())
switch = [0] + [int(i) for i in input().split()]
M = int(input())
for _ in range(M):
    sex, num = map(int, input().split())
    if sex == 1:
        for i in range(num, N+1, num):
            switch[i] = 1 - switch[i]
    else:
        switch[num] = 1 - switch[num]
        lp = num - 1
        rp = num + 1
        while lp > 0 and rp < N+1 and switch[lp] == switch[rp]:
            switch[lp] = 1 - switch[lp]
            switch[rp] = 1 - switch[rp]
            lp -= 1
            rp += 1

ans = []
line = (len(switch) - 1) // 20
rest = (len(switch) - 1) % 20
for i in range(line):
    print(*switch[20*i+1:(i+1)*20+1])
if rest != 0:
    print(*switch[20*(line)+1:])