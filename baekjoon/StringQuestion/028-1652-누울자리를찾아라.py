import sys; input = sys.stdin.readline

N = int(input())
if N == 1: print("0 0")
else:
    metrix = [list(input().rstrip()) for _ in range(N)]

    cntW = 0
    for i in range(N):
        cnt = 0
        prevIdx = -1
        for j in range(N):
            if (metrix[i][j] == 'X'):
                if (j - prevIdx > 2): cnt += 1
                prevIdx = j
        if N - prevIdx > 2: cnt += 1
        cntW += cnt if prevIdx > -1 else 1

    cntH = 0
    for j in range(N):
        cnt = 0
        prevIdx = -1
        for i in range(N):
            if (metrix[i][j] == 'X'):
                if (i - prevIdx > 2): cnt += 1
                prevIdx = i
        if N - prevIdx > 2: cnt += 1
        cntH += cnt if prevIdx > -1 else 1

    print(cntW, cntH)