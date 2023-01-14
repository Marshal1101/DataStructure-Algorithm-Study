"""
같은 1×1 크기의 칸에 여러 개의 나무가 심어져 있을 수도 있다.
가장 처음에 양분은 모든 칸에 5만큼 들어있다.
봄: 나이만큼 해당 땅의 양분 소모, 나이 +1, 나이가 어린 나무부터 양분 소모, 양분 부족 시 죽음
여름: 죽은 나무 // 2 만큼 해당 땅 양분 증가
가을: 5의 배수인 나무들 인접 칸 모두에 나이 1인 나무들 생김
겨울: 전체 땅에 A[r][c] 만큼 양분 추가
K년이 지난 후 상도의 땅에 살아있는 나무의 개수를 구하는 프로그램을 작성하시오
"""

# pypy

import sys
from collections import deque


def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    nutr = [list(map(int, input().split())) for _ in range(N)]
    land = [[5 for _ in range(N)] for _ in range(N)]
    init_tree = []
    dead_tree = deque()
    five_tree = deque()
    for _ in range(M):
        x, y, z = map(int, input().split())
        init_tree.append((z, x-1, y-1))
    
    init_tree.sort()
    tree = deque(init_tree)
    delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    year = 0
    while year < K:

        length = len(tree)        
        # 봄
        for _ in range(length):
            age, i, j = tree.popleft()
            if age > land[i][j]:
                dead_tree.append((age//2, i, j))
            else:
                land[i][j] -= age
                age += 1
                tree.append((age, i, j))
                if age % 5 == 0:
                    five_tree.append((i, j))

        # 여름
        while dead_tree:
            nut, i, j = dead_tree.popleft()
            land[i][j] += nut

        # 가을
        while five_tree:
            i, j = five_tree.popleft()
            for d in delta:
                ni = i + d[0]
                nj = j + d[1]
                if 0 <= ni < N and 0 <= nj < N:
                    tree.appendleft((1, ni, nj))

        # 겨울
        for i in range(N):
            for j in range(N):
                land[i][j] += nutr[i][j]

        year += 1

    print(len(tree))


if __name__ == '__main__':
    main()