import sys; input = sys.stdin.readline()

N = int(input())
dir = [0] * 5
tmp1 = 0
tmp2 = 0
for i in range(5):
    d, l = map(int, input().split())
    if d % 2:
        if not dir[d]:
            dir[d] = l
            if dir[d+1]:
                if dir[d] > dir[d+1]:
                    tmp1 = dir[d]
                else:
                    tmp1 = dir[d+1]
        else:
            dir[d] += l
            tmp1 = dir[d]
    else:
        if not dir[d]:
            dir[d] = l
            if dir[d-1]:
                if dir[d] > dir[d-1]:
                    tmp2 = dir[d]
                else:
                    tmp2 = dir[d-1]
        else:
            dir[d] += l
            tmp2 = dir[d]
    if tmp1:
        if tmp1 < 3:
            width = tmp1
        else:
            height = tmp1
    if tmp2:
        if tmp2 > 2:
            height = tmp2
        else:
            width = tmp2

