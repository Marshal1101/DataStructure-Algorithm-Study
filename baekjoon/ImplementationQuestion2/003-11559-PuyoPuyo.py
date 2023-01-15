import sys
from collections import deque


def set_puyo_down(field) -> None:
    i_pos = [-1] * 6
    for j in range(6):
        for i in range(11, -1, -1):
            if field[i][j] == ".":
                i_pos[j] = i
                break

    for j in range(6):
        if i_pos[j] == -1: continue
        for i in range(11, -1, -1):
            if i < i_pos[j] and field[i][j] != ".":
                field[i_pos[j]][j] = field[i][j]
                field[i][j] = "."
                i_pos[j] -= 1


def get_check_puyo(field) -> int:
    delta = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    visited = set()

    def bfs(si, sj):
        visited.add((si, sj))
        queue = deque([(si, sj)])
        ptr = 0
        while ptr < len(queue):
            ci, cj = queue[ptr]
            ptr += 1
            for di, dj in delta:
                ni = ci + di
                nj = cj + dj
                if 0 <= ni < 12 and 0 <= nj < 6 \
                    and not (ni, nj) in visited \
                    and field[ni][nj] == field[si][sj]:
                        visited.add((ni, nj))
                        queue.append((ni, nj))
                        
        if len(queue) < 4: return 0
        else:
            for i, j in queue:
                field[i][j] = "."
            return 1

    puyo_cnt = 0
    for i in range(11, -1, -1):
        for j in range(6):
            if field[i][j] != "." and not (i, j) in visited:
                puyo_cnt += bfs(i, j)
    
    return puyo_cnt



def main():
    input = sys.stdin.readline
    field = [list(input().rstrip()) for _ in range(12)]
    
    chain_cnt = 0
    puyo = 1
    while puyo > 0:
        
        # 4개 이상 찾아 제거
        puyo = 0
        puyo += get_check_puyo(field)
        if puyo > 0: chain_cnt += 1
        else: break
        # 남은 것들 아래로 내려가기
        set_puyo_down(field)

    print(chain_cnt)


if __name__ == '__main__':
    main()