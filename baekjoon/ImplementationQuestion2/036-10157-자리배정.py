import sys


def main():
    input = sys.stdin.readline
    C, R = map(int, input().split())
    K = int(input())

    if K > C * R:
        print(0)
        return

    # board = [[0] * C for _ in range(R)]
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    add = [R, C, R, C]
    d = 0
    i = -1
    j = d = 0
    
    # board[i][j] = K
    while K > 0:

        if K >= add[d]:
            K -= add[d]
            i = i + add[d] * delta[d][0]
            j = j + add[d] * delta[d][1]
            # board[i][j] = K if K != 0 else -1
            add[(d+1)%4] -= 1
            add[(d+3)%4] -= 1

            d = (d+1) % 4

        else:
            i = i + K * delta[d][0]
            j = j + K * delta[d][1]
            # board[i][j] = -1
            K = 0

    # for b in board:
    #     print(b)

    print(j+1, i+1)


if __name__ == '__main__':
    main()