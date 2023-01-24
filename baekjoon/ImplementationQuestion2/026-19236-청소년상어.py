import sys, copy

delta = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

def brute_force(point, si, sj, board: list, fishes: dict):

    # 상어 이동한 곳에 물고기 먹고 다시 반복
    dead_fish = board[si][sj]
    shark_d = fishes[dead_fish][2]
    point += dead_fish
    board[si][sj] = -1
    fishes[dead_fish] = []

    # 물고기 1부터 차례대로 이동 시작
    for n in range(1, 17):
        if len(fishes[n]) == 0: continue
        i, j = fishes[n][0], fishes[n][1]
        for k in range(8): 
            di, dj = delta[(fishes[n][2] + k) % 8]
            ni = i + di
            nj = j + dj
            if 0 <= ni < 4 and 0 <= nj < 4 and board[ni][nj] >= 0:
                temp = board[ni][nj]
                board[ni][nj] = n
                fishes[n][0], fishes[n][1] = ni, nj
                fishes[n][2] = (fishes[n][2] + k) % 8
                board[i][j] = 0                    
                if temp > 0:
                    fishes[temp][0], fishes[temp][1] = i, j
                    board[i][j] = temp                    
                break
        # 전부 회전해보아도 이동할 곳이 없으면 그 때 방향은? 원래대로? 아니면 돈 상태로?

    # 다음 상어 타겟 찾기
    is_next = False
    board[si][sj] = 0
    di, dj = delta[shark_d]
    for k in range(1, 4):
        ni = si + di * k
        nj = sj + dj * k
        if ni < 0 or ni > 3 or nj < 0 or nj > 3: break
        if (temp := board[ni][nj]) > 0:
            copy_board = [b[:] for b in board]
            copy_fishes = [f[:] for f in fishes]
            brute_force(point, ni, nj, copy_board, copy_fishes)
            is_next = True

    global max_point
    if not is_next and point > max_point:
        max_point = point


def main():
    input = sys.stdin.readline
    board = [list(map(int, input().split())) for _ in range(4)]
    fishes = [[] for _ in range(17)]
    for i in range(4):
        for j in range(0, 8, 2):
            fishes[board[i][j]] = [i, j//2, board[i][j+1]-1]
    board = [b[::2] for b in board]

    global max_point
    max_point = 0
    brute_force(0, 0, 0, board, fishes)
    print(max_point)


if __name__ == '__main__':
    main()