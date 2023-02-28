# https://www.acmicpc.net/source/54498118

# 아래 print()계열 주석들 풀면 디버깅 가능

################################################################################################################
# 같은 삼성 문제인 [Gold 3, 16235] 나무 재테크와 매우 비슷한 문제
# 16235와 동일하게 고려할 점 : 물고기를 1마리씩 검증하는 코드를 만들면, 시간초과가 날 수 밖에 없음
# ==> [x, y]위치에 k방향의 물고기 p마리가 있다. 라는 형태로 코드를 구현해서 물고기 p마리를 동시에 움직여야함

# 실전이 아니어서 해결한 문제인데... 실전이면 머리가 아프다.
# 특히, 예제가 제대로 주어지지 않는 상태에서 어디서 오류가 나는지 찾기가 매우 난해한 문제 (코드트리의 예제만으로는 문제 이해가 안되었음 ㅠㅠ)

# (내 경우) 문제를 좀 더 꼼꼼히 읽었어야 했다.
# 1) 상어가 칸 밖으로 넘어가는 경우는 배제해야하는데 그 경우를 배제하지 못해서 시간 소비함.
# 2) 2턴 뒤에 냄새가 사라진다는 것의 의미를 제대로 이해하지 못함
# 3) 상어가 3방향으로 움직이면서 물고기 0마리를 먹는 경우를 생각하지 못함 (예제 6? 에서 확인한듯)
# 이걸 판별하는 max_eat=0을 변수로 주고 64개의 루프를 돌면서 확인했는데, 무지성으로 제일 큰값 찾아야하니 0으로 시작해야지
# 라고 설정한게 화근. -1로 설정하면 상상상[0마리 먹음] 등의 경우를 고려할 수 있었는데, 시간낭비 ㅠㅠ



import itertools
import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

m, s = map(int, input().split())

directions = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)) #방향 0~7로 처리
# arrows = ['←', '↖', '↑', '↗', '→', '↘', '↓', '↙']
# 상어 상좌하우 : 2, 0, 6, 4

fishes = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]
copied_fishes = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]
# 물고기, 복제된 물고기는 [x, y]칸에 0~7로 표현되는 방향의 물고기가 몇 마리 있는지를 기록함

smells = [[[0, 0, 0] for _ in range(4)] for _ in range(4)] # [0, 1, 2턴뒤에 사라지는 애들]

for _ in range(m):
    fx, fy, d = map(int, input().split())
    # 위치, 방향 -1처리
    fx -= 1
    fy -= 1
    d -= 1
    fishes[fx][fy][d] += 1

sx, sy = map(int, input().split()) # 상어 위치
sx -= 1
sy -= 1

# def print_fishes(fishes):
#     for y in range(4):
#         for x in range(4):
#             print('[', end= '')
#             for d in range(8):
#                 if fishes[y][x][d]:
#                     print(str(fishes[y][x][d]) + arrows[d], end = '')
#             print(']', end = '\t')
#         print()

# print('Initial fishes')
# print_fishes(fishes)


def func1_copy(fishes):
    # 물고기 복제
    for x in range(4):
        for y in range(4):
            for d in range(8):
                copied_fishes[x][y][d] += fishes[x][y][d]

def func2_move_fishes(fishes):
    # print('움직일 수 있는 범위')
    # temp = []
    # for x in range(4):
    #     t = []
    #     for y in range(4):
    #         if sum(smells[x][y]) >0 or (x == sx and y == sy):
    #             t.append('x')
    #         else:
    #             t.append('o')
    #     temp.append(t)
    # temp[sx][sy] = 's'
    # for t in temp:
    #     print(t)

    new_fishes = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            for d in range(8):
                if fishes[x][y][d] > 0:
                    num_fish = fishes[x][y][d]
                    curd = d
                    move = False
                    for _ in range(8):
                        dx, dy = directions[curd]
                        nx, ny = x+dx, y+dy
                        # 이부분 주의해라!!! and 무지성으로 쓰다 나락간다!!!!
                        # 상어랑 위치가 다르려면 x, y중에 하나랑만 다르면 됨!
                        if 0<=nx<4 and 0<=ny<4 and (nx != sx or ny != sy) and sum(smells[nx][ny]) == 0:
                            move = True
                            break
                        curd = (curd - 1) % 8


                    if move:
                        # print('이쪽으로 움직임 x, y', x, y, 'dir', arrows[d] , 'to ', nx, ny, arrows[curd])
                        new_fishes[nx][ny][curd] += num_fish
                    else:
                        # 이부분에서 실수함(예제 6으로 확인함)
                        # => 움직일 수 없을 때 복제된 물고기는 기존 물고기와 같은 곳에 생기는데 그부분을 놓쳤음
                        new_fishes[x][y][curd] += num_fish
                        # print('못움직임')
    return new_fishes

def func3_shark_move(fishes):
    global sx, sy
    # print('상어 위치', sx, sy)
    # DFS로.... : (X) 어차피 64면 그냥 돌려도 시간초과가 나진 않을 것 같음.

    max_eat = -1
    max_case = []
    for shark_dirs in itertools.product([2, 0, 6, 4], [2, 0, 6, 4], [2, 0, 6, 4]):
        # print(shark_dirs, arrows[shark_dirs[0]], arrows[shark_dirs[1]], arrows[shark_dirs[2]])
        move_count = 0
        pos = set() # 상하상 처럼 중복되는 경우가 있어서 그걸 처리 => 상하상으로 움직일 수는 있으나 죽는 물고기 수는 상하만 포함됨
        px, py = sx, sy
        can_move = True
        for pd in shark_dirs:
            dx, dy = directions[pd]
            nx, ny = px+dx, py+dy
            if 0<=nx<4 and 0<=ny<4:
                px, py = nx, ny
                pos.add((px, py))
                move_count += 1
            else:
                can_move = False

        if can_move: # 문제 꼼꼼히 읽을것. 범위를 벗어나는 경우는 배제함
            eat = 0
            for xx, yy in pos:
                eat += sum(fishes[xx][yy])
            # temp_arrows = [arrows[p] for p in shark_dirs]
            # print('상어 움직이는 방향', temp_arrows, 'pos', pos, '먹은양', eat)
            if max_eat < eat:
                max_eat = eat
                max_case = shark_dirs

    # temp_arrows = [arrows[p] for p in max_case]
    # print('최종 선택')
    # print('상어 움직이는 방향', temp_arrows, '먹은양', max_eat)

    for mc in max_case:
        dx, dy = directions[mc]
        sx = sx + dx
        sy = sy + dy

        deads = sum(fishes[sx][sy]) # 죽는 애들
        smells[sx][sy][2] += deads # 죽은만큼 시체에 추가하고
        fishes[sx][sy] = [0 for _ in range(8)] # 해당 칸의 몬스터는 모두 죽음
        # print('상어 위치', sx, sy, '시체 추가', deads)

def func5_hatch_copied_fishes():
    for y in range(4):
        for x in range(4):
            for d in range(8):
                fishes[y][x][d] += copied_fishes[y][x][d]
                copied_fishes[y][x][d] = 0

for stage in range(s):
    # print()
    # print('=====================================================================================')
    # print(stage, 'th stage start')

    # print('상어 위치 : ', sx, sy)
    # print('1. 물고기 복제하기 [복제 대기]')
    func1_copy(fishes)
    # print_fishes(copied_fishes)


    fishes = func2_move_fishes(fishes)
    # print('2. 물고기 움직이기')
    # print_fishes(fishes)

    # 냄새 하루 지남
    for y in range(4):
        for x in range(4):
            smells[y][x][0] = smells[y][x][1]
            smells[y][x][1] = smells[y][x][2]
            smells[y][x][2] = 0

    # print('3. 상어 움직이기')
    func3_shark_move(fishes)
#     print('남은 물고기')
#     print_fishes(fishes)

#     print('상어가 먹어서 생긴 냄새 + 냄새 소멸')
    for y in range(4):
        for x in range(4):
            smells[y][x][0] = 0

    # print('냄새 소멸')
    # for b in smells:
    #     print(b)

    # print('5. 복제 물고기 부화하기')
    func5_hatch_copied_fishes()

    # print('최종 결과')
    # print('남은 물고기')
    # print_fishes(fishes)
    # print('냄새')
    # for b in smells:
    #     print(b)
    # print('상어', sx, sy)

answer = 0
for y in range(4):
    for x in range(4):
        answer += sum(fishes[y][x])
print(answer)
