import sys


def parallel(i):
    if i == 1: return 2
    elif i == 2: return 1
    elif i == 3: return 4
    elif i == 4: return 3


input = sys.stdin.readline
K = int(input())
max_w = 0
max_h = 0
draw = []
for _ in range(6):
    d, length = map(int, input().split())
    if (d == 1 or d == 2) and length > max_w:
        max_w = length
    if (d == 3 or d == 4) and length > max_h:
        max_h = length
    draw.append(length)

wi = draw.index(max_w)
if draw[(wi+1)%6] != max_h:
    sh = draw[(wi+1)%6]
elif draw[(wi+5)%6] != max_h:
    sh = draw[(wi+5)%6]

hi = draw.index(max_h)
if draw[(hi+1)%6] != max_w:
    sw = draw[(hi+1)%6]
elif draw[(hi+5)%6] != max_w:
    sw = draw[(hi+5)%6]

square = (max_h * max_w) - (max_h - sh) * (max_w - sw)
print(square * K)