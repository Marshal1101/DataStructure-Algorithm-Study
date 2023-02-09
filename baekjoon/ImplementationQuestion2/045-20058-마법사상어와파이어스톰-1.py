import sys


def rotate(i, j, n, board, delta):
    for k in range(2**(n-1)):
        for _ in range(2**n - (2*k+1)):
            si = i + k
            sj = j + k
            ni = nj = -1
            pi = pj = -1
            d = 0
            temp = board[si][sj]
            # print("temp<=:", si, sj, board[si][sj])
            for _ in range(4):
                s = 0
                while s < 2**n - (2*k+1) :
                    # 7 5 3 1
                    s += 1
                    ni = si + delta[d][0]
                    nj = sj + delta[d][1]
                    # print("si, sj:", si, sj, "<=", "ni, nj:", ni, nj)
                    board[si][sj] = board[ni][nj]
                    pi, pj = si, sj
                    si, sj = ni, nj
                d = (d+1) % 4
            board[pi][pj] = temp
            # print("temp=>:", ni, nj, board[ni][nj])



def count_around(i, j, N, board, delta):
    cnt = 1
    for di, dj in delta:
        ni = i + di
        nj = j + dj
        if ni < 0 or ni >= 2**N or nj < 0 or nj >= 2**N or board[ni][nj] == 0:
            continue
        cnt += 1

    return cnt

def dfs(i, j, N, board, delta, visited):
    visited.add((i, j))
    stack = [(i, j)]
    cnt = 1
    while stack:
        i, j = stack.pop()
        for di, dj in delta:
            ni = i + di
            nj = j + dj
            if (ni, nj) in visited or ni < 0 or ni >= 2**N or nj < 0 or nj >= 2**N or board[ni][nj] == 0:
                continue
            cnt += 1
            visited.add((ni, nj))
            stack.append((ni, nj))

    return cnt


def fire_Storm(n, N, board, delta):
    # 0 <= n <= N
    # 1. 배열 분할, 회전
    step = 2**n
    for i in range(0, 2**N, step):
        if n == 0: break
        for j in range(0, 2**N, step):
            rotate(i, j, n, board, delta)

    # 1-1 얼음칸 3개 이하는 1줄어든다.
    melted = set()
    for i in range(2**N):
        for j in range(2**N):
            if board[i][j] == 0: continue
            cnt = count_around(i, j, N, board, delta)
            if cnt < 4:
                melted.add((i, j))
    for mi, mj in melted:
        board[mi][mj] -= 1


def main():
    input = sys.stdin.readline
    N, Q =map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(2**N)]
    delta = [(1,0), (0,1), (-1,0), (0,-1)]  # 하 우 상 좌
    ans1 = ans2 = 0
    for n in map(int, input().split()):
        fire_Storm(n, N, board, delta)

    # 2. 배열 값 합산
    ans1 = 0
    for b in board:
        ans1 += sum(b)
    
    # 3. 큰 덩어리 탐색
    ans2 = 0
    visited = set()
    for i in range(2**N):
        for j in range(2**N):
            if (i, j) in visited or board[i][j] == 0: continue
            cnt = dfs(i, j, N, board, delta, visited)
            if cnt > ans2:
                ans2 = cnt

    print(ans1)
    print(ans2)


if __name__ == '__main__':
    main()