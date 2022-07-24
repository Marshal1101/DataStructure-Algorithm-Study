import sys


def adj(k, d, N, M) :
    i, j = k // M, k % M
    dir = d
    ret = []
    for _ in range(4) :
        nd = dir-1 if dir != 0 else 3
        # 북동남서 0123
        # 북
        if nd == 0 and i > 0 :
            ret.append((k-M, 0))
        # 남
        elif nd == 2 and i < N - 1 :
            ret.append((k+M, 2))
        # 서
        elif nd == 3 and j > 0 :
            ret.append((k-1, 3))
        # 동
        elif nd == 1 and j < M - 1 :
            ret.append((k+1, 1))
        dir = nd
    return ret


def pull_back(k, d, N, M) :
    i, j = k // M, k % M
    # 북보며 남으로 후진
    if d == 0 and i < N - 1 :
        return k + M
    # 동보며 서로 후진
    if d == 1 and j > 0 :
        return k - 1
    # 남보며 북으로 후진
    if d == 2 and i > 0 :
        return k - M
    # 서보며 동으로 후진
    if d == 3 and j < M - 1 :
        return k + 1


def clean_dfs(i, j, d, room, N, M) :
    idx = i*M + j
    dir = d
    room[idx] = 1
    cnt = 1
    while True :
        adj_list = adj(idx, dir, N, M)
        for n_idx, nd in adj_list :
            if room[n_idx] == '0' :
                cnt += 1
                room[n_idx] = cnt
                idx = n_idx
                dir = nd
                break
        else :
            dir = nd
            if room[(n_idx := pull_back(idx, dir, N, M))] != '1' :
                idx = n_idx
            else : return cnt


def main() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    room = []
    for _ in range(N) :
        room += input().split()
    print(clean_dfs(r, c, d, room, N, M))

    # 경로 추적 출력
    # for i in range(N) :
    #     print(*[format(int(x), '02') for x in room[i*M:(i+1)*M]], sep=" ")


if __name__ == '__main__' :
    main()