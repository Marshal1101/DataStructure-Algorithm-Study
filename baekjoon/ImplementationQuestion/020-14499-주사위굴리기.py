import sys


def surface_dice_map(dice: list, dir: int):
    ## dice = ['', 위1, 앞2, 오3, 왼4, 뒤5, 밑6]
    if dir == 1:
        temp = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = dice[3]
        dice[3] = temp
    elif dir == 2:
        temp = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[6]
        dice[6] = dice[4]
        dice[4] = temp
    elif dir == 3:
        temp = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = dice[2]
        dice[2] = temp
    elif dir == 4:
        temp = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[6]
        dice[6] = dice[5]
        dice[5] = temp


def dice_move(i, j, N, M, graph, command):
    dice = [0] * 7
    d = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
    for dir in command:
        ni = i + d[dir][0]
        nj = j + d[dir][1]
        if 0 <= ni < N and 0 <= nj < M:
            surface_dice_map(dice, dir)
            if graph[ni][nj] == 0:
                graph[ni][nj] = dice[6]
            else:
                dice[6] = graph[ni][nj]
                graph[ni][nj] = 0
            print(dice[1])
            i = ni
            j = nj

def main():
    input = sys.stdin.readline
    N, M, i, j, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    command = list(map(int, input().split()))
    dice_move(i, j, N, M, graph, command)


if __name__ == '__main__':
    main()