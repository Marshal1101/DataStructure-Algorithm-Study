import sys


def move_time(N, crain, M, box):
    checked = [False] * M
    m = 0
    ans = 0
    maxp = M-1
    while m < M:
        ans += 1
        for i in range(maxp, -1, -1):
            if not checked[i]:
                if crain[0] < box[i]:
                    return -1
                else:
                    checked[i] = True
                    m += 1
                    maxp = i-1
                    break
        if m == M:
            break
        subp = maxp
        for k in range(1, len(crain)):
            for i in range(subp, -1, -1):
                if not checked[i] and crain[k] >= box[i]:
                    checked[i] = True
                    m += 1
                    subp = i-1
                    break
            else:
                crain = crain[:k]
                break
            if m == M:
                break

    return ans


def main():
    input = sys.stdin.readline
    N = int(input())
    crain = [*map(int, input().split())]
    crain.sort(reverse=True)
    M = int(input())
    box = [*map(int, input().split())]
    box.sort()
    min_b = box[0]
    for i in range(N):
        if crain[i] < min_b:
            crain = crain[:i]
            break
    print(move_time(N, crain, M, box))


if __name__ == '__main__':
    main()