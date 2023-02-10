# https://www.acmicpc.net/source/52881644

import sys
input = sys.stdin.readline

def count(small):   # 물고기 한개씩 채우기


    try:
        index = arr.index(small)
        arr[index] += 1
        count(small)

    except:
        return

def angle(lst, floor):   #long 현재 가로
    high = len(lst)
    new = []
    if high <= N - floor:   # 현재 높이만큼 남은 바닥이 있는 경우
        for i in range(len(lst[0])):
            temp = []
            for j in range(high - 1, -1, -1):
                temp.append(lst[j][i])
            new.append(temp)
        new.append(arr[floor:floor + high])

        return angle(new, floor + high)

    else:       # 다음 바닥이 없는 경우
        extra = N - floor
        lst[-1].extend(arr[floor::])
        for i in range(high - 1):
            lst[i].extend([0] * extra)

        return lst


def plus(lst):
    M = len(lst)    # 높이
    R = len(lst[0]) # 가로
    visit = [[0] * R for _ in range(M)]

    dr = [0, 1]     # 하, 우만 확인
    dc = [1, 0]

    for i in range(M):
        for j in range(R):
            if lst[i][j]:
                visit[i][j] += lst[i][j]
                for k in range(2):
                    nc = i + dc[k]
                    nr = j + dr[k]
                    if 0 <= nc < M and 0 <= nr < R and lst[nc][nr]:
                        diff = abs(lst[i][j] - lst[nc][nr]) // 5
                        if lst[nc][nr] > lst[i][j]:
                            visit[nc][nr] -= diff
                            visit[i][j] += diff
                        else:
                            visit[i][j] -= diff
                            visit[nc][nr] += diff

    return visit

def flat(lst):
    C = len(lst)    # 높이
    R = len(lst[0]) # 가로
    new = []
    for r in range(R):
        for c in range(C - 1, -1, -1):
            if lst[c][r]:
                new.append(lst[c][r])

    return new
def fly(lst):
    R = len(lst) // 2 # 가로
    new = []
    new.append(lst[:R][::-1])
    new.append(lst[R:])

    R = R // 2


    new2 = []
    for i in range(1, -1, -1):
        new2.append(new[i][:R][::-1])
        new[i] = new[i][R:]

    new2.extend(new)
    return new2





N, K = map(int, input().split())    # 어항의 수 ( N은 4 이상, 4의 배수), K개 이하
arr = list(map(int, input().split()))
cnt = 0
while True:    # 차이가 K개 이하가 될 때까지
    small, big = min(arr), max(arr)
    if big - small <= K:
        print(cnt)
        break
    count(small)
    arr = flat(plus(fly(flat(plus(angle([[arr[0]]], 1))))))
    cnt += 1