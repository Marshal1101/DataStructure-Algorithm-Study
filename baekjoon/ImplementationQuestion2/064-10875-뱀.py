import sys


def check_line(t, nd, time, x, nx, y, ny, d, visited):
    rx = ry = 0
    if d == 0:  # 동
        sx, lx, hv = x, nx, 0
    elif d == 1:    # 남
        sy, ly, hv = ny, y, 1
    elif d == 2:    # 서
        sx, lx, hv = nx, x, 0
    else:   # 북
        sy, ly, hv = y, ny, 1
    
    # (x, nx, y, ny, hv)
    min_time = sys.maxsize
    for k in range(len(visited)-1):
        x1, x2, y1, y2, phv = visited[k]
        # 가로선분
        if hv == 0:
            if hv == phv:
            # 가로선분 만남
                if y != y1:
                    continue
                if sx > x2 or lx < x1:
                    continue
                tt = time + min(abs(x - x2), abs(x1 - x))
                # if abs(x - x2) < abs(x1 - x):
                #     tt = time + x - x2
                #     cx = x2
                # else:
                #     tt = time + x1 - x
                #     cx = x1
                if tt < min_time:
                    min_time = tt
                    # rx = cx
            else:
            # 세로선분 만남
                if sx > x1 or lx < x1:
                    continue
                if y > y2 or y < y1:
                    continue
                tt = time + abs(x - x1)
                if tt < min_time:
                    min_time = tt
                    # rx = x1

        else:
            if hv == phv:
                if x != x1:
                    continue
                if sy > y2 or ly < y1:
                    continue
                tt = time + min(abs(y - y2), abs(y1 - y))
                # if abs(y - y2) < abs(y1 - y):
                #     tt = time + y - y2
                #     cy = y2
                # else:
                #     tt = time + y1 - y
                #     cy = y1                    
                if tt < min_time:
                    min_time = tt
                    # ry = cy
            else:
                if sy > y1 or ly < y2:
                    continue
                if x > x2 or x < x1:
                    continue
                tt = time + abs(y - y1)
                if tt < min_time:
                    min_time = tt
                    # ry = y1

    if min_time != sys.maxsize:
        return 0, rx, ry, min_time

    if hv == 0:
        visited.append((sx, lx, y, y, 0))
    else:
        visited.append((x, x, sy, ly, 1))
    
    if nd == 'L':
        d = (d-1) % 4
    else:
        d = (d+1) % 4

    return time + t, nx, ny, d



def main():
    input = sys.stdin.readline
    L = int(input())
    N = int(input())
    delta = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # 0동 1남 2서 3북 L:-1 <-, R:1 ->
    # (x, nx, y, ny, hv:0,1)
    visited = [
        (-(L+1), L+1, L+1, L+1, 0),
        (-(L+1), L+1, -(L+1), -(L+1), 0),
        (L+1, L+1, -(L+1), L+1, 1),
        (-(L+1), -(L+1), -(L+1), L+1, 1),
        ]
    x = y = 0
    d = 0
    time = 0
    for _ in range(N):
        t, nd = input().split()
        t = int(t)
        nx = x + t * delta[d][0]
        ny = y + t * delta[d][1]
        time, x, y, d = check_line(t, nd, time, x, nx, y, ny, d, visited)
        if time == 0:
            print(d)
            return

    # 마지막 방향 직진
    t = 2 * L + 1
    nd = 'L'
    nx = x + t * delta[d][0]
    ny = y + t * delta[d][1]
    time, x, y, d = check_line(t, nd, time, x, nx, y, ny, d, visited)
    if time == 0:
        print(d)
        return


if __name__ == '__main__':
    main()