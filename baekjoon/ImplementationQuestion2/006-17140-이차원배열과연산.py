import sys
from collections import Counter


def padding(idx, s, end, metrix, dir=0):
    if dir == 0:
        while s < end:
            metrix[idx][s] = 0
            s += 1
    else:
        while s < end:
            metrix[s][idx] = 0
            s += 1

def main():
    input = sys.stdin.readline
    R, C, K = map(int, input().split())
    R = R-1
    C = C-1
    metrix = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(3):
        for j, val in enumerate(map(int, input().split())):
            metrix[i][j] = val

    if metrix[R][C] == K:
        print(0)
        return

    max_R = 3
    max_C = 3
    time = 0
    while time < 100:
        time += 1
        cur_max_R = 0
        cur_max_C = 0
        end = []

        if max_R >= max_C:
            for i in range(max_R):
                row = Counter(metrix[i])
                if row[0]: row.pop(0)
                row = row.most_common()
                row.sort(key=lambda x: (x[1], x[0]))
                length = len(row) if len(row) < 50 else 50
                for j in range(length):
                    num, cnt = row[j]
                    metrix[i][2*j] = num
                    metrix[i][2*j+1] = cnt

                end.append(2*length)
                if 2*length > cur_max_C: cur_max_C = 2*length
            
            for i in range(max_R):
                padding(i, end[i], max_C, metrix, 0)
            max_C = cur_max_C

        else:
            for j in range(max_C):
                col = Counter([metrix[i][j] for i in range(max_R)])
                if col[0]: col.pop(0)
                col = col.most_common()
                col.sort(key=lambda x: (x[1], x[0]))
                length = len(col) if len(col) < 50 else 50
                for i in range(length):
                    num, cnt = col[i]
                    metrix[2*i][j] = num
                    metrix[2*i+1][j] = cnt

                end.append(2*length)
                if 2*length > cur_max_R: cur_max_R = 2*length
            
            for j in range(max_C):
                padding(j, end[j], max_R, metrix, 1)
            max_R = cur_max_R

        if metrix[R][C] == K:
            print(time)
            return

    print(-1)


if __name__ == '__main__':
    main()