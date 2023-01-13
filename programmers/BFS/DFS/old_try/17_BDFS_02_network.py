import sys
sys.setrecursionlimit(2000000)


def solution(n, computers) :

    def DFS(y) :
        # (y, y) 값들을 방문여부로 한다. 미방문 1, 방문 -1
        computers[y][y] = -1
        for j in range(n) :
            if computers[y][j] == 1 :
                if computers[j][j] == 1 :
                    DFS(j)
                computers[y][j] = -1
            

    cnt = 0
    for i in range(n) :
        # DFS 발동하는 회수만큼 네트워크
        if computers[i][i] == 1:
            DFS(i)
            cnt += 1

    return cnt

print(solution(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]))