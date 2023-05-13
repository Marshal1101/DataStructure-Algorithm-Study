import sys

for _ in range(3):
    N = int(sys.stdin.readline())
    num = 0
    for _ in range(N):
        num += int(sys.stdin.readline())
    if num > 0: print('+')
    elif num < 0: print('-')
    else: print('0')