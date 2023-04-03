import sys      
input = sys.stdin.readline

R, C = map(int, input().split())
Map = [list(input().rstrip()) for _ in range(R)]

def dfs(r, c):
    Map[r][c] = 'x'

    if c == C - 1:
        return True

    if r > 0 and Map[r-1][c+1] != 'x':
        if dfs(r-1, c+1):
            return True
    if Map[r][c+1] != 'x':
        if dfs(r, c+1):
            return True
    if r < R-1 and Map[r+1][c+1] != 'x':
        if dfs(r+1, c+1):
            return True

    return False

count = 0
for r in range(R):
    if dfs(r, 0):
        count += 1
print(count)