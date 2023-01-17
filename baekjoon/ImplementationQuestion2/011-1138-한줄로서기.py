import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    taller_cnt = [-1] + list(map(int, input().split()))
    row = list(range(1, N+1))

    for n in range(N, 0, -1):
        cnt = taller_cnt[n]
        idx = row.index(n)
        for k in range(N):
            if cnt == 0:
                del row[idx]
                row.insert(k, n)
                break
            if row[k] > row[idx]:
                cnt -= 1

    print(*row)


if __name__ == '__main__':
    main()