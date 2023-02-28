import sys


def main():
    count = [0, 0, 0, 0]
    input = sys.stdin.readline
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    cast = [tuple(map(int, input().split())) for _ in range(M)]
    # 회전 좌하우상 0123
    rot = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    dq = [0]
    # 상어 위치 중앙 시작
    i, j = N // 2, N // 2
    # 보드 회전하며 한 줄 리스트에 담기
    k = d = 0
    R = 1
    while i != 0 or j != 0:
        i = i + rot[d][0]
        j = j + rot[d][1]
        dq.append(board[i][j])
        k += 1
        if k == R:
            if d % 2:
                R += 1
            d = (d+1) % 4
            k = 0    

    # 1. 마법사 파편파괴
    for d, s in cast:
        # 1. 구슬파괴
        for k in range(1, s+1):
            # 상하좌우 1234
            if d == 1:
                idx = (2*k+1)**2-1 - k
            elif d == 2:
                idx = (2*k+1)**2-1 - 5*k
            elif d == 3:
                idx = (2*k-1)**2 + (k-1)
            else:
                idx = (2*k+1)**2-1 - 3*k
            
            if idx >= len(dq):
                break
            dq[idx] = 0
    
        # 2. 구슬이동
        ndq = [0]
        for v in dq:
            if v != 0:
                ndq.append(v)
        dq = ndq

        # 3-1. 구슬 4개 이상 연속시 폭발, 새로 생긴 4개 이상 구슬도 폭발
        flag = True
        while flag:
            flag = False
            ndq = [0]
            si = 1
            cnt = 1
            for idx in range(1, len(dq)):
                if ndq[-1] == dq[idx]:
                    cnt += 1            
                else:
                    if cnt >= 4:
                        flag = True
                        count[ndq[-1]] += cnt
                        ndq[si:] = []
                    cnt = 1
                    si = len(ndq)
                ndq.append(dq[idx])
            
            if cnt >= 4:
                flag = True
                count[ndq[-1]] += cnt
                ndq[si:] = []
            dq = ndq
            # 3-2. 구슬이동, 1-2반복

        # 4. 숫자그룹마다 구슬 2개로 변화, 구슬개수, 구슬번호
        ndq = [0]
        cnt = 1
        for idx in range(2, len(dq)):
            if dq[idx-1] == dq[idx]:
                cnt += 1
            else:
                ndq.append(cnt)
                ndq.append(dq[idx-1])
                cnt = 1
            if len(ndq) > N**2:
                ndq[N**2:] = []
                break
        else:
            if 1 < len(ndq) < N**2:
                ndq.append(cnt)
            if 1 < len(ndq) < N**2:
                ndq.append(dq[-1])
        dq = ndq
        
    ans = 0
    for i in range(1, 4):
        ans += i * count[i]

    print(ans)


if __name__ == '__main__':
    main()