import sys; input = sys.stdin.readline

board = input().rstrip()
board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")
if board.find("X") == -1: print(board)
else: print(-1)