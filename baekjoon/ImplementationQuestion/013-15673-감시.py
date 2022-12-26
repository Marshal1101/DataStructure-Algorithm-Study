import sys


def watch_right(i, j, cctv, area):
    while j < len(area[0]):
        if area[i][j] == 6: break
        area[i][j] = cctv
        j += 1

def watch_left(i, j, cctv, area):
    while j >= 0:
        if area[i][j] == 6: break
        area[i][j] = cctv
        j -= 1

def watch_up(i, j, cctv, area):
    while i >= 0:
        if area[i][j] == 6: break
        area[i][j] = cctv
        i -= 1

def watch_down(i, j, cctv, area):
    while i < len(area):
        if area[i][j] == 6: break
        area[i][j] = cctv
        i += 1

def watch_cctv(i, j, cctv, angle, area):
    if cctv == 1:
        if angle == 1: watch_up(i, j, cctv, area)
        elif angle == 2: watch_right(i, j, cctv, area)
        elif angle == 3: watch_down(i, j, cctv, area)
        elif angle == 4: watch_left(i, j, cctv, area)
            
    elif cctv == 2:
        if angle == 1:
            watch_left(i, j, cctv, area)
            watch_right(i, j, cctv, area)
        elif angle == 2:
            watch_up(i, j, cctv, area)
            watch_down(i, j, cctv, area)

    elif cctv == 3:
        if angle == 1:
            watch_up(i, j, cctv, area)
            watch_right(i, j, cctv, area)
        elif angle == 2:
            watch_up(i, j, cctv, area)
            watch_left(i, j, cctv, area)
        elif angle == 3:
            watch_left(i, j, cctv, area)
            watch_down(i, j, cctv, area)
        elif angle == 4:
            watch_down(i, j, cctv, area)
            watch_right(i, j, cctv, area)

    elif cctv == 4:
        if angle == 1:
            watch_up(i, j, cctv, area)
            watch_left(i, j, cctv, area)
            watch_right(i, j, cctv, area)
        elif angle == 2:
            watch_up(i, j, cctv, area)
            watch_left(i, j, cctv, area)
            watch_down(i, j, cctv, area)
        elif angle == 3:
            watch_left(i, j, cctv, area)
            watch_down(i, j, cctv, area)
            watch_right(i, j, cctv, area)
        elif angle == 4:
            watch_down(i, j, cctv, area)
            watch_right(i, j, cctv, area)
            watch_up(i, j, cctv, area)

    elif cctv == 5:
        watch_up(i, j, cctv, area)
        watch_left(i, j, cctv, area)
        watch_right(i, j, cctv, area)
        watch_down(i, j, cctv, area)

def brute_force(k, angle, cctv_q, N, M, area):
    if k == len(cctv_q): 
        global min_ans
        cnt = 0
        for i in range(N):
            for j in range(M):
                if area[i][j] == 0:
                    cnt += 1
        if cnt < min_ans:
            min_ans = cnt
        return

    i, j, cctv = cctv_q[k]
    if cctv == 2 and angle > 2: return
    if cctv == 5 and angle > 1: return
    
    copy_area = [area[k][:] for k in range(N)]
    watch_cctv(i, j, cctv, angle, copy_area)
    
    brute_force(k+1, 1, cctv_q, N, M, copy_area)
    brute_force(k+1, 2, cctv_q, N, M, copy_area)
    brute_force(k+1, 3, cctv_q, N, M, copy_area)
    brute_force(k+1, 4, cctv_q, N, M, copy_area)


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]

    global min_ans
    min_ans = N * M

    cctv_q = []
    for i in range(N):
        for j in range(M):
            if 0 < area[i][j] <= 6:
                min_ans -= 1
                if area[i][j] != 6:
                    cctv_q.append((i, j, area[i][j]))
    
    if cctv_q:
        brute_force(0, 1, cctv_q, N, M, area)
        brute_force(0, 2, cctv_q, N, M, area)
        brute_force(0, 3, cctv_q, N, M, area)
        brute_force(0, 4, cctv_q, N, M, area)
    print(min_ans)

if __name__=='__main__':
    main()