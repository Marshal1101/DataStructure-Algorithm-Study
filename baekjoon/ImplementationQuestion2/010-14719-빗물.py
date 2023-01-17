"""
바닥은 막힘
처음 벽과 마지막 벽 중요

아이디어
1. 완전탐색(구현/확인)
최대 500 x 500 크기인 H x W 배열이므로
기둥만큼 제한 값, 양 옆 트인 공간부터
물을 제거해 나간 값을 빼면 된다.

2. 스택(미구현/미확인)
왼쪽 기둥으로부터
새로운 기둥을 받을 때
왼쪽 기둥보다
작으면,
	그 차이 예상 값으로 더한다.
같거나 크면,
	값을 total에 더하고,
	그 기둥을 새로운 물막이로 지정하고 반복
마지막 기둥이 시작 기둥보다 작으면,
	시작 기둥과 마지막 기둥 높이 차이에
	그 사이 인덱스 길이 만큼 넓이를 뺀다. 
"""


import sys

# 완전탐색
def main():
    input = sys.stdin.readline
    H, W = map(int, input().split())
    board = [[1 for _ in range(W)] for _ in range(H)]

    total = H * W

    for j, height in enumerate(map(int, input().split())):
        for i in range(height):
            board[i][j] = 0
            total -= 1

    for i in range(H):
        if board[i][0] != 0:
            for j in range(W):
                if board[i][j] != 0:
                    board[i][j] = 0
                    total -= 1
                else: break
    
    for i in range(H):
        if board[i][W-1] != 0:
            for j in range(W-1, -1, -1):
                if board[i][j] != 0:
                    board[i][j] = 0
                    total -= 1
                else: break

    print(total)


# def main2():
#     input = sys.stdin.readline
#     H, W = map(int, input().split())
    
#     stack = []
#     total = 0
    
#     max_h = 0
#     for height in map(int, input().split()):
#         if height >= max_h:
#             max_h = height        
#         else:
#             total += max_h - height
#         stack.append(height)

#     if (end_h := stack.pop()) < max_h:
#         total -= max_h - end_h
#         while stack and end_h != max_h:
#             cur_h = stack.pop()
#             if cur_h < end_h:
#                 total -= max_h - end_h
#             else:
# #                 end_h = cur_h

#     print(total)

if __name__ == '__main__':
    main()