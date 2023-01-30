import sys
input = sys.stdin.readline
src = input().rstrip()
keyword = input().rstrip()

for n in range(10):
    src = src.replace(str(n), "")

if src.find(keyword) != -1: print(1)
else: print(0)