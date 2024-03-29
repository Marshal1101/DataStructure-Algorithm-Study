# https://www.acmicpc.net/source/53579759

import sys
from itertools import combinations


def kill(cur_field: list, archer_pos: tuple(int, int, int)):
    global N, M, D
    kill_counts = 0

    new_field = duplicateField(cur_field)
    targets = set()

    for cur_lane in range(N, 0, -1):
        targets.clear()
        for archer_num in range(3):
            pos = archer_pos[archer_num]
            has_shot = False

            for d in range(1, D + 1):
                if has_shot:
                    break
                top_y = max(cur_lane - d, 0)
                for x in range(max(pos - d + 1, 0), min(pos + d, M)):
                    y = - d + abs(x - pos) + cur_lane
                    if y >= top_y and new_field[y][x] == 1:
                        targets.add((x, y))
                        has_shot = True
                        break

        for x, y in targets:
            new_field[y][x] = 0
            kill_counts += 1

    return kill_counts


def duplicateField(target: list[list]):
    to = list()
    for i in range(N):
        to.append(target[i].copy())
    return to


def enemyCounterLambda(x):
    global enemies_count
    y = int(x)
    if y == 1:
        enemies_count += 1
    return y


input = sys.stdin.readline
N, M, D = map(int, input().strip().split(sep=' '))

field = []
archer_positions = list(combinations(range(M), 3))

enemies_count = 0

for i in range(N):
    field.append(list(map(lambda x: enemyCounterLambda(x), input().strip().split())))

max_kills = 0
for comb in archer_positions:
    max_kills = max(max_kills, kill(field, comb))
print(max_kills)