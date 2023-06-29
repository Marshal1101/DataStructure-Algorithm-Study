import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    board = [[0] * 101 for _ in range(101)]
    for _ in range(N):
        x1, y1 = map(int, input().split())
        for i in range(y1, y1+10):
            for j in range(x1, x1+10):
                board[i][j] = 1
    
    ans = 0
    for i in range(101):
        color = 0
        for j in range(101):
            if board[i][j] != color:
                color = 1 - color
                ans += 1
    
    for j in range(101):
        color = 0
        for i in range(101):
            if board[i][j] != color:
                color = 1 - color
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()