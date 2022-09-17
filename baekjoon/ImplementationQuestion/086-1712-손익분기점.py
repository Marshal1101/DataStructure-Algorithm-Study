import sys


A, B, C = map(int, sys.stdin.readline().split())
if C-B <= 0 : print(-1)
else : print(A // (C-B) + 1)