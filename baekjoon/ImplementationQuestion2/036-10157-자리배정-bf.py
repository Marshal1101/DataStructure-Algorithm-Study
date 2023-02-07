import sys


def main():
    input = sys.stdin.readline
    C, R = map(int, input().split())
    K = int(input())

    if K > C * R:
        print(0)
        return

    board = [[0] * C for _ in range(R)]
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    j = d = 0
    i = -1
    n = 1
    while n <= K:
        ni = i + delta[d][0]
        nj = j + delta[d][1]
        if ni < 0 or ni >= R or nj < 0 or nj >= C or board[ni][nj] > 0:
            d = (d+1) % 4
            continue

        board[ni][nj] = n
        i = ni
        j = nj
        n += 1

    # for b in board:
    #     print(b)

    print(j+1, i+1)

if __name__ == '__main__':
    main()