import sys; input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    first = 0
    is_conn = 0
    for j in range(M):
        color = board[i][j]
        if color > 0:
            if first == 0:
                first = color
                ans += 1

            elif color != first:
                if not is_conn:
                    ans += 1
                    is_conn = True
            else:
                is_conn = False
            
        else:
            first = 0
            is_conn = False

print(ans)