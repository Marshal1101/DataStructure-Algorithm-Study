import sys


"""
0. 동으로 한칸 구른다

1. 이동방향으로 구른다.
1-1 막다르면 반대로 구른다
2. 도착한 지도점수 획득
2-1 주사위 아랫면과 지도 정수와 비교
    주사위 > 지도: 이동방향 90도 시계방향 회전
    주사위 < 지도: 반시계방향 90도 회전
    주사위 = 지도: 변화없음
2-0 지도점수계산
    지도점수 = 지도정수 * 그 정수와 같은 연결된 칸들의 개수

"""
class Dice:
    def __init__(self, up=1, down=6, front=5, rear=2, left=4, right=3) -> None:
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.front = front
        self.rear = rear
    
    def roll(self, dir):
        # 동으로 이동
        if dir == 0:
            tmp = self.up
            self.up = self.left
            self.left = self.down
            self.down = self.right
            self.right = tmp
        # 남으로 이동
        elif dir == 1:
            tmp = self.up
            self.up = self.rear
            self.rear = self.down
            self.down = self.front
            self.front = tmp
        # 서로 이동
        elif dir == 2:
            tmp = self.up
            self.up = self.right
            self.right = self.down
            self.down = self.left
            self.left = tmp
        # 북으로 이동
        elif dir == 3:
            tmp = self.up
            self.up = self.front
            self.front = self.down
            self.down = self.rear
            self.rear = tmp

    def get_bottom(self):
        return self.down


def dfs(si, sj):
    cnt = 1
    visited = set([(si, sj)])
    stk = [(si, sj)]
    num = board[si][sj]
    while stk:
        i, j = stk.pop()
        for di, dj in delta:
            ni = i + di
            nj = j + dj
            if ni < 0 or nj < 0 or ni >= N or nj >= M:
                continue
            if board[ni][nj] != num or (ni, nj) in visited:
                continue
            cnt += 1
            visited.add((ni, nj))
            stk.append((ni, nj))
    return cnt

input = sys.stdin.readline
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dice = Dice()
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
i = j = d = t = ans = 0
while t < K:
    ni, nj = i + delta[d][0], j + delta[d][1]
    if nj >= M or nj < 0 or ni >= N or ni < 0:
        d = (d + 6) % 4
        ni, nj = i + delta[d][0], j + delta[d][1]
    # print(f"{t}, ni: {ni}, nj: {nj}, d:{d}")
    dice.roll(d)
    a = dice.get_bottom()
    b = board[ni][nj]
    if a > b:
        d = (d + 5) % 4
    elif a < b:
        d = (d + 3) % 4
    cnt = dfs(ni, nj)
    ans += b * cnt
    # print(f"{t}, a: {a}, b: {b}, cnt:{cnt}, ans: {ans}")
    i, j = ni, nj
    t += 1

print(ans)