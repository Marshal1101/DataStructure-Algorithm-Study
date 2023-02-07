import sys
from itertools import permutations

def simulate(order, board):
    point = 0
    idx = 0
    for b in board:
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            if b[order[idx]] == 0:
                out += 1
            elif b[order[idx]] == 1:
                point += b3
                b1, b2, b3 = 1, b1, b2
            elif b[order[idx]] == 2:
                point += (b3 + b2)
                b1, b2, b3 = 0, 1, b1
            elif b[order[idx]] == 3:
                point += (b3 + b2 + b1)
                b1, b2, b3 = 0, 0, 1
            elif b[order[idx]] == 4:
                point += (b1 + b2 + b3 + 1)
                b1, b2, b3 = 0, 0, 0
            idx = (idx+1) % 9

    return point


def main():
    input = sys.stdin.readline
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_point = 0
    for order in permutations(range(1, 9), 8):
        order = list(order)
        order = order[:3] + [0] + order[3:]
        point = simulate(order, board)
        if point > max_point:
            # print("order:", order)
            max_point = point

    print(max_point)


if __name__ == '__main__':
    main()