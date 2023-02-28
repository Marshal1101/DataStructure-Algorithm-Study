import sys


def robot_action(bot:int, com:str, rep:int, robot_pos:dict, board:list[list], delta:list):
    cy, cx, d = robot_pos[bot]
    if com == "L":
        nd = (d+3*rep) % 4
        robot_pos[bot][2] = nd
    elif com == "R":
        nd = (d+1*rep) % 4
        robot_pos[bot][2] = nd
    else:   #F
        k = 1
        while k <= rep:
            ny = cy + k * delta[d][0]
            nx = cx + k * delta[d][1]
            if board[ny][nx] == -1:
                return -1
            if board[ny][nx] > 0:
                return board[ny][nx]
            k += 1
        robot_pos[bot][0] = ny
        robot_pos[bot][1] = nx
        board[cy][cx] = 0
        board[ny][nx] = bot
    return 0


def direct_to_d(direct:str) -> int:
    if direct == "N":
        return 0
    if direct == "E":
        return 1
    if direct == "S":
        return 2
    if direct == "W":
        return 3


def main():
    input = sys.stdin.readline
    A, B = map(int, input().split())
    N, M = map(int, input().split())
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # y,x N하0 E우1 S상2 W좌3
    board = [[-1] * (A+2)] + [[-1] + [0]*A + [-1] for _ in range(B)] + [[-1 for _ in range(A+2)]]
    robot_pos = dict()
    for n in range(1, N+1):
        x, y, direct = input().split()
        y, x = int(y), int(x)
        robot_pos[n] = [y, x, direct_to_d(direct)]
        board[y][x] = n
    for _ in range(M):
        bot, com, rep = input().split()
        bot = int(bot)
        rep = int(rep)
        ret = robot_action(bot, com, rep, robot_pos, board, delta)
        if ret != 0:
            if ret == -1:
                print(f"Robot {bot} crashes into the wall")
                break
            elif ret > 0:
                print(f"Robot {bot} crashes into robot {ret}")
                break
    else:
        print("OK")

        
if __name__ == '__main__':
    main()