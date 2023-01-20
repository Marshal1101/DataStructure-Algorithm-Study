# https://www.acmicpc.net/source/53752759


import sys

input = sys.stdin.readline


def go_down_2_lines(c):
    c -= 1
    print("R" * c + "D" + "L" * c + "D", end='')


def go_down_2_lines_finale(c, down=False):
    c -= 1
    print("L" * c + "D" + "R" * c + "D" * down, end='')


def go_right_2_lines(r):
    r -= 1
    print("D" * r + "R" + "U" * r + "R", end='')


def divide(val, div):
    while val < 0:
        val += div
    return val // div


def main(r, c):
    if r % 2:
        for _ in range(r >> 1):
            go_down_2_lines(c)
        print("R" * (c - 1))
        return

    if c % 2:
        for _ in range(c >> 1):
            go_right_2_lines(r)
        print("D" * (r - 1))
        return

    min_val, min_i, min_j = 1000, 0, 0
    for i in range(r):
        line = list(map(int, input().split()))
        for j in range((i + 1) % 2, c, 2):
            if line[j] < min_val:
                min_val, min_i, min_j = line[j], i, j

    x_is_up = (min_i + 1) % 2
    stick_to_wall = (c - min_j) <= 2
    stick_to_bottom = (r - min_i) <= 2
    for _ in range(min_i >> 1):
        go_down_2_lines(c)
    for _ in range(min_j >> 1):
        go_right_2_lines(2)
    if x_is_up:
        print("DR", end='')
        if stick_to_wall:
            if stick_to_bottom:
                return
            else:
                print("D", end='')
        else:
            print("RUR", end='')
            for _ in range(divide(c - min_j - 2, 2)):
                go_right_2_lines(2)
            print("D", end='')
            if stick_to_bottom:
                return
            else:
                print("D", end='')
    else:
        print("R", end='')
        if stick_to_wall:
            print("D", end='')
            if stick_to_bottom:
                return
            else:
                print("D", end='')
        else:
            for _ in range(divide(c - min_j - 2, 2)):
                go_right_2_lines(2)
            print("D", end='')
            if stick_to_bottom:
                return
            else:
                print("D", end='')

    for _ in range(divide(r - min_i - 3, 2)):
        go_down_2_lines_finale(c, True)

    if divide(r - min_i - 1, 2):
        go_down_2_lines_finale(c, False)


if __name__ == "__main__":
    R, C = list(map(int, input().split()))
    main(R, C)
