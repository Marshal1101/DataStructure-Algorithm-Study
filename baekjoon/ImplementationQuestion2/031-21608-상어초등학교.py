import sys
from collections import defaultdict


# 자리에 선호하는 친구가 없어 주변에 빈 자리가 가장 많은 곳 앉을 때,
def sit_without_myfav(me, N, board, frd_pos, empty_max) -> int:
    # i, j 순으로 탐색해서 상하좌우 빈자리 수가 empty_max인 자리 찾으면 바로 배정
    # empty_max = 0 이 되면, (i, j)가 빈자리이기만 하면 배정된다.
    while empty_max >= 0:
        for i in range(N):
            for j in range(N):
                if board[i][j] != 0: continue
                cnt = len(chk_empty_pos(i, j, N, board))
                if cnt == empty_max:
                    board[i][j] = me
                    frd_pos[me] = (i, j)
                    return empty_max
        
        # 자리없으면 empty_max 낮춰가며 최대 빈자리 탐색 
        empty_max -= 1


# 점수 합산
def count_point(N, board, favor):
    point = 0
    for i in range(N):
        for j in range(N):
            # 현재 숫자
            me = board[i][j]
            cnt = 0
            for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= N:
                    continue
                # 주변 있는 숫자가 선호 친구일 때 카운트
                if board[ni][nj] in favor[me]:
                    cnt += 1

            if cnt == 1: point += 1
            elif cnt == 2: point += 10
            elif cnt == 3: point += 100
            elif cnt == 4: point += 1000
    
    return point


# i,j 상하좌우 중에 배열범위 벗어나지 않고, 숫자 자리배정된 적 없는 위치 리스트 반환
def chk_empty_pos(i, j, N, board):
    empty_pos = []
    for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ni, nj = i + di, j + dj
        if ni < 0 or ni >= N or nj < 0 or nj >= N or board[ni][nj] != 0:
            continue
        empty_pos.append((ni, nj))
    
    return empty_pos


def main():
    input = sys.stdin.readline
    N = int(input())

    # 자리 배열
    board = [[0] * N for _ in range(N)]
    
    # n의 선호 친구들 favor[n] = set()
    favor = [set() for _ in range(N*N + 1)]
    
    # n의 배정된 자리 frd_pos[n] = (i, j)
    frd_pos = dict()

    # 임의 자리에서 주위 빈 자리의 최대개수, 초기값 상하좌우 4 
    empty_max = 4

    for _ in range(N*N):
        line = list(map(int, input().split()))
        me = line[0]
        favor[me].update(line[1:])

        # 선호하는 자리들의 위치
        good_pos = defaultdict(int)
        
        # max_pt: 내 자리 주변에 선호 친구들 최대 몇 명
        max_pt = 0
        
        # 내가 선호하는 친구들 중에
        for myfav in line:
            if myfav in frd_pos:
                # 있으면 친구자리의 주변자리들에 +1
                fi, fj = frd_pos[myfav]   # 친구 위치
                for ni, nj in chk_empty_pos(fi, fj, N, board):
                    good_pos[(ni, nj)] += 1
                    if good_pos[(ni, nj)] > max_pt:
                        max_pt = good_pos[(ni, nj)]

        # 내가 선호하는 친구들의 주변 자리가 있으면
        if len(good_pos) > 0:
            # 친구 최대 가능한 자리들은 변별력 위해 자리 주위에 있는 빈 자리 개수만큼 점수 추가
            for i, j in good_pos.keys():
                if good_pos[(i, j)] == max_pt:
                    good_pos[(i, j)] += len(chk_empty_pos(i, j, N, board))
            
            # 점수 내림차순, ij 오름차순 정렬
            sorted_good_pos = sorted(good_pos.items(), key=lambda x: (-x[1], x[0]))
            
            # 현재 학생의 선정된 자리 위치 ni nj, 숫자를 자리배열에 입력, 위치정보 저장 
            ni, nj = sorted_good_pos[0][0]
            board[ni][nj] = me
            frd_pos[me] = (ni, nj)
        
        # 자리에 선호하는 친구들이 없으면
        else:
            empty_max = sit_without_myfav(me, N, board, frd_pos, empty_max)

    print(count_point(N, board, favor))



if __name__ == '__main__':
    main()