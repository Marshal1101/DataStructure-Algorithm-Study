import sys


def main():
    input = sys.stdin.readline

    # 빙고판
    board = []
    for _ in range(5):
        board.extend(list(map(int, input().split())))

    # 숫자 위치
    pos = [-1] * 26
    for i in range(25):
        pos[board[i]] = i

    # 빙고 체크
    chk_row = [False] * 5
    chk_col = [False] * 5
    chk_R = False
    chk_L = False

    # 숫자 부르기
    bingo = 0
    for p in range(5):
        line = list(map(int, input().split()))
        for q in range(5):
            num = line[q]
            board[pos[num]] = -num

            # # 보드 확인
            # print(5*p+q+1, "=========")
            # for k in range(0, 25, 5):
            #     print(board[k:k+5])

            # 행 숫자 확인
            for i in range(5):
                if not chk_row[i]:
                    for k in range(5*i, 5*i+5):
                        if board[k] > 0: break
                    else:
                        chk_row[i] = True
                        bingo += 1

            # 열 숫자 확인
            for j in range(5):
                if not chk_col[j]:
                    for k in range(j, j+21, 5):
                        if board[k] > 0: break
                    else:
                        chk_col[j] = True
                        bingo += 1
            
            # 대각선 0시작 오른쪽 아래 방향
            if not chk_R:
                for d in range(0, 25, 6):
                    if board[d] > 0: break
                else:
                    chk_R = True
                    bingo += 1

            # 대각선 4시작 왼쪽 아래 방향
            if not chk_L:
                for d in range(4, 21, 4):
                    if board[d] > 0:
                        break
                else:
                    chk_L = True
                    bingo += 1

            if bingo >= 3:
                print(5 * p + q + 1)
                return

if __name__ == '__main__':
    main()