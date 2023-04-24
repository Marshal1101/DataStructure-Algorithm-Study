import sys; input = sys.stdin.readline

N = int(input())
line = sorted([int(input().rstrip()) for _ in range(N)], reverse=True)
for i, v in enumerate(line):
    if v < i:
        print(sum(line[:i]) - i*(i-1)//2)
        break
else:
    print(sum(line) - i*(i+1)//2)