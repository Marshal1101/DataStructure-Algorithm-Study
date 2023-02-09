import sys


def tornado(i, j, d, N, board, delta):

    def spread_soil(i, j, per):
        nonlocal cur_soil
        nonlocal out_soil
        nonlocal remained
        # 좌우, 가장 앞으로 뿌려진 모래 체크
        soil = int(cur_soil * per)
        if i < 0 or i >= N or j < 0 or j >= N:
            out_soil += soil
        else:
            board[i][j] += soil
        remained -= soil

    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[i][j] = True
    out_soil = 0
    d = 0
    r = 0
    R = 2
    while True:
        r += 1
        ni = i + delta[d][0]
        nj = j + delta[d][1]

        if nj < 0:
            return out_soil

        visited[ni][nj] = True
        cur_soil = board[ni][nj]
        remained = cur_soil

        # d 방향
        ni1 = ni + delta[d][0]
        nj1 = nj + delta[d][1]
        
        # d 방향의 우측
        d1 = (d+4-1) % 4
        ri = i + delta[d1][0]
        rj = j + delta[d1][1]
        ri1 = ri + delta[d][0]
        rj1 = rj + delta[d][1]

        # d 방향의 좌측
        d2 = (d+4+1) % 4
        li = i + delta[d2][0]
        lj = j + delta[d2][1]
        li1 = li + delta[d][0]
        lj1 = lj + delta[d][1]

        spread_soil(ri, rj, 0.01)
        spread_soil(li, lj, 0.01)
        spread_soil(ri1 + delta[d1][0], rj1 + delta[d1][1], 0.02)
        spread_soil(li1 + delta[d2][0], lj1 + delta[d2][1], 0.02)
        spread_soil(ni1 + delta[d][0], nj1 + delta[d][1], 0.05)
        spread_soil(ri1, rj1, 0.07)
        spread_soil(li1, lj1, 0.07)
        spread_soil(ri1 + delta[d][0], rj1 + delta[d][1], 0.1)
        spread_soil(li1 + delta[d][0], lj1 + delta[d][1], 0.1)


        # a로 뿌져진 모래 체크
        if ni1 < 0 or ni1 >= N or nj1 < 0 or nj1 >= N:
            out_soil += remained
        else:
            board[ni1][nj1] += remained
        board[ni][nj] = 0

        i = ni
        j = nj

        if r == R//2:
            d = (d+1) % 4
        elif r == R:
            R += 2
            r = 0
            d = (d+1) % 4


def main():
    input = sys.stdin.readline
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 좌, 하, 우, 상
    print(tornado(N//2, N//2, 0, N, board, delta))


if __name__ == '__main__':
    main()