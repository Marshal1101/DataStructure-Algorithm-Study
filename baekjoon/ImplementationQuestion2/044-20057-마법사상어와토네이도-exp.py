# https://www.acmicpc.net/source/54630172

import math
import sys
input = sys.stdin.readline

def spread(graph, x, y, i):
    sand = graph[x][y]
    one = math.trunc(sand * 0.01)
    two = math.trunc(sand * 0.02)
    five = math.trunc(sand * 0.05)
    seven = math.trunc(sand * 0.07)
    ten = math.trunc(sand * 0.1)
    mod = sand - (one + two + seven + ten) * 2 - five

    if i % 4 == 0:
        graph[x][y - 2] += five
        graph[x - 1][y - 1] += ten
        graph[x + 1][y - 1] += ten
        graph[x - 2][y] += two
        graph[x + 2][y] += two
        graph[x - 1][y] += seven
        graph[x + 1][y] += seven
        graph[x - 1][y + 1] += one
        graph[x + 1][y + 1] += one
        graph[x][y - 1] += mod
    elif i % 4 == 1:
        graph[x + 2][y] += five
        graph[x + 1][y - 1] += ten
        graph[x + 1][y + 1] += ten
        graph[x][y - 2] += two
        graph[x][y + 2] += two
        graph[x][y - 1] += seven
        graph[x][y + 1] += seven
        graph[x - 1][y - 1] += one
        graph[x - 1][y + 1] += one
        graph[x + 1][y] += mod
    elif i % 4 == 2:
        graph[x][y + 2] += five
        graph[x - 1][y + 1] += ten
        graph[x + 1][y + 1] += ten
        graph[x - 2][y] += two
        graph[x + 2][y] += two
        graph[x - 1][y] += seven
        graph[x + 1][y] += seven
        graph[x - 1][y - 1] += one
        graph[x + 1][y - 1] += one
        graph[x][y + 1] += mod
    else:
        graph[x - 2][y] += five
        graph[x - 1][y - 1] += ten
        graph[x - 1][y + 1] += ten
        graph[x][y - 2] += two
        graph[x][y + 2] += two
        graph[x][y - 1] += seven
        graph[x][y + 1] += seven
        graph[x + 1][y - 1] += one
        graph[x + 1][y + 1] += one
        graph[x - 1][y] += mod
        

n = int(input())
graph = [[0] * (n + 4) for _ in range(n + 4)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
tmp = [1, 1, 2, 2]
now = [n // 2 + 2, n // 2 + 2]
total = 0
board = 0
cnt = (n - 3) * 2 + 5

for i in range(n):
    row = list(map(int, input().split()))
    graph[i + 2][2:n + 2] = row

for i in range(cnt - 5):
    tmp.append(tmp[-1] + 1 if i % 2 == 0 else tmp[-1])
tmp.append(tmp[-1])

for i in range(cnt):
    for _ in range(tmp[i]):
        now[0] += dx[i % 4]
        now[1] += dy[i % 4]

        spread(graph, now[0], now[1], i)

for i in graph:
    total += sum(i)

for x in range(n):
    for y in range(n):
        board += graph[x + 2][y + 2]

print(total - board)