import sys


def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    chess = [list(map(lambda x: int(x)-1, input().split())) for _ in range(K)]
    delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    stack = [[[] for _ in range(N)] for _ in range(N)]
    for k in range(K):
        i, j, d = chess[k]
        stack[i][j].append(k)

    # 이동
    time = 0
    while time < 1001:
        time += 1
        flag_3 = False
        k = 0
        while k < K:
            i, j, d = chess[k]
            ni = i + delta[d][0]
            nj = j + delta[d][1]

            # 3, out
            if ni < 0 or ni >= N or nj < 0 or nj >= N or board[ni][nj] == 2:
                if flag_3:
                    flag_3 = False
                    k += 1
                    continue
                if d % 2 == 0: d += 1
                else: d -= 1
                chess[k][2] = d
                flag_3 = True
                continue

            # 0
            elif board[ni][nj] == 0:
                flag_3 = False
                s = stack[i][j].index(k)
                move = stack[i][j][s:]
                stack[ni][nj].extend(move)
                stack[i][j] = stack[i][j][:s]
                
                # 옮겨진 체스 좌표갱신
                for m in move:
                    chess[m][0] = ni
                    chess[m][1] = nj
            # 1
            elif board[ni][nj] == 1:
                flag_3 = False
                s = stack[i][j].index(k)
                move = stack[i][j][s:]
                move.reverse()
                stack[ni][nj].extend(move)
                stack[i][j] = stack[i][j][:s]

                # 옮겨진 체스 좌표갱신
                for m in move:
                    chess[m][0] = ni
                    chess[m][1] = nj

            # 말 개수 체크
            if len(stack[ni][nj]) >= 4:
                print(time)
                sys.exit(0)

            k += 1

    print(-1)


if __name__ == '__main__':
    main()