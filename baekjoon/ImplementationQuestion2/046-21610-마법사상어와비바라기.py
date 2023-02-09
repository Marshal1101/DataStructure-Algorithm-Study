import sys


def bibaragi(N, M, board, move):
    cloud_pos = {(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)}
    #  ←, ↖, ↑, ↗, →, ↘, ↓, ↙
    delta = [-1, (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]

    for d, s in move:
        # 이동하고 +1
        new_cloud_pos = set()
        for i, j in cloud_pos:
            i = (i + s * delta[d][0] + 50*N) % N
            j = (j + s * delta[d][1] + 50*N) % N
            board[i][j] += 1
            new_cloud_pos.add((i, j))
        cloud_pos = new_cloud_pos

        # 대각선 체크, 물있는만큼 +개수
        check = set()
        for i, j in cloud_pos:
            for k in range(2, 9, 2):
                ni = i + delta[k][0]
                nj = j + delta[k][1]
                if ni < 0 or ni >= N or nj < 0 or nj >= N or board[ni][nj] == 0:
                    continue
                board[i][j] += 1


        # 구름있었던 칸 제외 2이상 칸 구름 생성, -2
        new_cloud_pos = set()
        for i in range(N):
            for j in range(N):
                if (i, j) in cloud_pos or board[i][j] < 2:
                    continue
                board[i][j] -= 2
                new_cloud_pos.add((i, j))
        cloud_pos = new_cloud_pos

        # print("===========")
        # print(new_cloud_pos)
        # for b in board:
        #     print(b)

    ans = 0
    for b in board:
        ans += sum(b)

    print(ans)


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    move = [list(map(int, input().split())) for _ in range(M)]
    bibaragi(N, M, board, move)


if __name__ == '__main__':
    main()