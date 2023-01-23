import sys
from collections import deque


def rotate(X, D, K, N, M, circle):
    for n in range(N):
        if (n+1) % X == 0:
            if D == 1: # 반시계방향
                circle[n] = circle[n][K:] + circle[n][:K]

            elif D == 0: # 시계방향 
                circle[n] = circle[n][-K:] + circle[n][:(M-K)]


def handle_board(num_cnt, N, M, circle, board):
    # 수가 남아 있으면 인접 수 같은 것을 찾는다.
    # 같은 수를 모두 지운다
    def bfs(sn, si, num):
        is_del = False
        queue = deque([(sn, si)])
        while queue:
            n, i = queue.popleft()
            for dn, di in delta:
                nn = n + dn
                ni = (i + di + M) % M
                if 0 <= nn < N and board[nn][circle[nn][ni]] == num:
                    board[nn][circle[nn][ni]] = -num
                    queue.append((nn, ni))
                    is_del = True
                    
        if is_del > 0:
            board[sn][circle[sn][si]] = -num
        return is_del
    
    delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    is_del = False
    for n in range(N):
        for i in range(M):
            if not (n, i) in visited and board[n][circle[n][i]] > 0:
                is_del |= bfs(n, i, board[n][circle[n][i]])


    # 같은 수 없어 삭제 안했으면 평균 구하고 큰수는 -1 작은수는 +1
    total = 0
    if is_del == 0:
        for n in range(N):
            total += sum(board[n])
        if total != 0:
            mean = total / num_cnt
            # print("total:", total, "num_cnt:", num_cnt, "mean:",mean)
            for i in range(N):
                for j in range(M):
                    if board[i][j] != 0:
                        if board[i][j] < mean:
                            board[i][j] += 1
                            total += 1
                        elif board[i][j] > mean:
                            board[i][j] -= 1
                            total -= 1
    
    # 같은 수 있으면 해당 수들 원판에서 삭제
    else:
        for i in range(N):
            for j in range(M):
                if board[i][j] < 0:
                    board[i][j] = 0
                    num_cnt -= 1
                elif board[i][j] > 0:
                    total += board[i][j]

    return num_cnt, total


def main():
    input = sys.stdin.readline
    N, M, T = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    circle = [[i for i in range(M)] for _ in range(N)]
    num_cnt = N * M
    total = 0
    for t in range(T):
        X, D, K = map(int, input().split())
        rotate(X, D, K, N, M, circle)
        num_cnt, total = handle_board(num_cnt, N, M, circle, board)

    print(total)


if __name__ == '__main__':
    main()
