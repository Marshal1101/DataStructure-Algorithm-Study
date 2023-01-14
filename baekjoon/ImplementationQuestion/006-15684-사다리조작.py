# pypy

import sys


def check(N, H, graph) -> bool:
    for i in range(1, N+1):
        cur_i = i
        for j in range(1, H+1):
            if graph[cur_i][j] > 0:
                cur_i = graph[cur_i][j]
        if cur_i != i:
            return False
    return True


def put_ladder(cnt, maxCnt, cur_i, N, H, graph):
    if cnt == maxCnt:
        if check(N, H, graph):
            print(cnt)
            sys.exit(0)
        return

    for i in range(cur_i, N+1):
        for j in range(1, H+1):
            if graph[i][j] == 0 and i < N and graph[i+1][j] == 0:
                graph[i][j] = i + 1
                graph[i+1][j] = i
                put_ladder(cnt+1, maxCnt, cur_i, N, H, graph)
                graph[i][j] = 0
                graph[i+1][j] = 0


def main():
    input = sys.stdin.readline
    N, M, H = map(int, input().split())
    graph = [[0 for _ in range(H+1)] for _ in range(N+1)]
    for _ in range(M):
        j, i = map(int, input().split())
        graph[i][j] = i + 1
        graph[i+1][j] = i

    if check(N, H, graph):
        print(0)
        return

    for k in range(1, 4):
        copy_graph = [g[:] for g in graph]
        put_ladder(0, k, 1, N, H, copy_graph)
    print(-1)


if __name__ == '__main__':
    main()