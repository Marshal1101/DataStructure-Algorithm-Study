import sys
from collections import defaultdict


def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())

    # 영역표시
    board = [[[-1, -1] for _ in range(N)] for _ in range(N)]
    # 상어 위치
    shark_pos = defaultdict(list)
    # 상어 우선방향
    prio_dir = [[] for _ in range(M+1)]
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 초기 값
    for i in range(N):
        for j, num in enumerate(map(int, input().split())):
            if num > 0:
                shark_pos[num] = [i, j, 0]
                board[i][j] = [0, num]

    for n, d in enumerate(map(int, input().split())):
        shark_pos[n+1][2] = d-1

    for n in range(1, M+1):
        for _ in range(4):
            prio_dir[n].append(list(map(lambda x: int(x)-1, input().split())))

    # 상어 1만 남는지
    only_one = False
    
    time = 0
    while time < 1001:
        # 한 마리이면 종료
        if len(shark_pos) == 1:
            only_one = True
            break

        time += 1
        new_shark_pos = defaultdict(list)
        
        # 이동
        for n, pos in shark_pos.items():
            i, j, d = pos
            
            is_found = False
            # 주변에 빈 곳 있을 때
            for nd in prio_dir[n][d]:
                ni = i + delta[nd][0]
                nj = j + delta[nd][1]

                if ni < 0 or ni >= N or nj < 0 or nj >= N:
                    continue
                
                # 빈 곳 또는 영역표시 사라진 곳
                if board[ni][nj][0] == -1 \
                    or time - abs(board[ni][nj][0]) > K:
                    is_found = True
                    board[ni][nj][0] = time
                    board[ni][nj][1] = n
                    new_shark_pos[n] = [ni, nj, nd]
                    break

                # 방금 다른 상어가 온 곳, 싸운다.
                if board[ni][nj][0] == time:
                    is_found = True
                    # 그 상어보다 낮은 수이면 쫓아냄
                    if (en := board[ni][nj][1]) > n:
                        board[ni][nj][1] = n
                        new_shark_pos[n] = [ni, nj, nd]
                        del new_shark_pos[en]
                        break
                    # 그 상어보다 큰 수이면 die
                    else: break

            # 빈 곳 없을 때
            if not is_found:
                for nd in prio_dir[n][d]:
                    ni = i + delta[nd][0]
                    nj = j + delta[nd][1]

                    if ni < 0 or ni >= N or nj < 0 or nj >= N:
                        continue
                    
                    # 내가 왔던 곳, 음수로 입력, 싸우지 않게
                    if board[ni][nj][1] == n:
                        board[ni][nj][0] = -time
                        new_shark_pos[n] = [ni, nj, nd]
                        break
        
        shark_pos = new_shark_pos

        # print(time, "=================")
        # for b in board:
        #     print(b)

    if only_one: print(time)
    else: print(-1)


if __name__ == '__main__':
    main()