import sys


def move_time(N, crain, M, box):
    checked = [False] * M
    m = 0
    ans = 0
    ptr = M-1
    while m < M:
        ans += 1
        for i in range(ptr, -1, -1):
            if not checked[i]:
                if crain[0] < box[i]:
                    return -1
                else:
                    checked[i] = True
                    m += 1
                    ptr = i-1
                    if m == M:
                        return ans
                    break
        
        for k in range(1, len(crain)):
            for i in range(ptr, -1, -1):
                if not checked[i] and crain[k] >= box[i]:
                    checked[i] = True
                    m += 1
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
    if len(crain) == 0:
        print(-1)
    else:
        print(move_time(N, crain, M, box))


if __name__ == '__main__':
    main()