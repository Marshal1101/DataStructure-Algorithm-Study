import sys


paper = [[0] * 100 for _ in range(100)]
input = sys.stdin.readline
N = int(input())

def draw(x, y, paper):
    for i in range(y, y+10):
        for j in range(x, x+10):
            paper[i][j] = 1

def size(paper):
    cnt = 0
    for i in range(100):
        for j in range(100):
            if paper[i][j]: cnt += 1
    return cnt

for _ in range(N):
    x, y = map(int, input().split())
    draw(x, y, paper)

print(size(paper))