import sys


def roller_path(R, C, board):
    # 1. 행 또는 열이 홀수이면 모두 출력 가능 표시
    is_print_all = 0
    if R % 2 != 0: is_print_all += 1
    if C % 2 != 0: is_print_all += 2

    # 1-1. 행과 열이 짝수이면 피해야할 최소 값 위치 탐색 행렬 합이 홀수인 대각선마다
    else:
        min_value = 1000
        min_val_R, min_val_C = -1, -1
        for i in range(R):
            for j in range(1 - (i % 2), C, 2):
                if board[i][j] < min_value:
                    min_value = board[i][j]
                    min_val_R, min_val_C = i, j

    ans = ""
    # 전부 출력, 행과 열이 모두 홀수면 긴쪽으로 전개
    # 행이 홀수면 우측으로 전개
    if (is_print_all == 3 and C >= R) or is_print_all == 1:
        for i in range(R):
            if i % 2 == 0: ans += ("R" * (C-1)) + "D"
            else: ans += ("L" * (C-1)) + "D"
        ans = ans[:-1]
    
    # 열이 홀수면 아래로 전개
    elif (is_print_all == 3 and C < R) or is_print_all == 2:
        for j in range(C):
            if j % 2 == 0: ans += ("D" * (R-1)) + "R"
            else: ans += ("U" * (R-1)) + "R"
        ans = ans[:-1]


    # 행열 짝수면 최소값 피하기
    else:
        # 열이 길 때
        if R < C:
            # 최소값 있는 행의 직전 행까지 2줄씩 이동
            for _ in range(min_val_R//2):
                ans += "R"*(C-1) + "D" + "L"*(C-1) + "D"

            # 최소값 있는 열까지 접근
            ans += "DRUR" * (min_val_C // 2)
            
            # 최소값 피하기
            if min_val_C % 2 == 0: ans += "RD"
            else: ans += "DR"
            
            # 피하고 그 행의 열 끝까지 이동
            ans += "RURD" * (C//2 - min_val_C//2 - 1)

            # 우측 하단 까지 마무리
            for _ in range(min_val_R//2, R//2 -1 ):
                ans += "D" + "L"*(C-1) + "D" + "R"*(C-1)

        else:
            for _ in range(min_val_C//2):
                ans += "D"*(R-1) + "R" + "U"*(R-1) + "R"

            ans += "RDLD" * (min_val_R // 2)

            if min_val_R % 2 == 0: ans += "DR"
            else: ans += "RD"

            ans += "DLDR" * (R//2 - min_val_R//2 - 1)

            for _ in range(min_val_C//2, C//2 - 1):
                ans += "R" + "U"*(R-1) + "R" + "D"*(R-1)
    
    return ans


if __name__ == '__main__':
    input = sys.stdin.readline
    R, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(R)]
    print(roller_path(R, C, board))