# https://www.acmicpc.net/problem/14890

import sys

input = sys.stdin.readline
N, L = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]
# print(N, L)
# for o in range(N):
#     print(road[o])

possible_road_cnt = 0
for i in range(N):
    sq_height_cnt = 0
    prev_height = road[i][0]
    is_goin_down = False
    for j in range(N):
        if is_goin_down and sq_height_cnt == L:
            is_goin_down = False
            sq_height_cnt = 0
        # print(f"{is_goin_down} {sq_height_cnt}", end="")
        gab = road[i][j] - prev_height
        if gab > 1 or gab < -1: break
        elif gab == 1:
            if is_goin_down or sq_height_cnt < L: break
            else: sq_height_cnt = 0
        elif gab == -1:
            if is_goin_down: break
            is_goin_down = True
            sq_height_cnt = 0
        sq_height_cnt += 1
        prev_height = road[i][j]
        # print(f"({i} {j})", end=" ")
    else:
        if not is_goin_down or sq_height_cnt >= L:
            # print(f"possible: {i} {j}", end=" ")
            possible_road_cnt += 1
    # print("=========")
        
for j in range(N):
    sq_height_cnt = 0
    prev_height = road[0][j]
    is_goin_down = False
    for i in range(N):
        if is_goin_down and sq_height_cnt == L:
            is_goin_down = False
            sq_height_cnt = 0
        # print(f"{is_goin_down} {sq_height_cnt}", end="")
        gab = road[i][j] - prev_height
        if gab > 1 or gab < -1: break
        elif gab == 1:
            if is_goin_down or sq_height_cnt < L: break
            else: sq_height_cnt = 0
        elif gab == -1:
            if is_goin_down: break
            is_goin_down = True
            sq_height_cnt = 0
        sq_height_cnt += 1
        prev_height = road[i][j]
        # print(f"({i} {j})", end=" ")
    else:
        if not is_goin_down or sq_height_cnt >= L:
            # print(f"possible: {i} {j}", end=" ")
            possible_road_cnt += 1
    # print("=========")
    
print(possible_road_cnt)


