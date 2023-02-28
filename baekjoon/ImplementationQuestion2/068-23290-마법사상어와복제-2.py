import sys
# defaultdict import 하지 않는 게 빠르지만, 조건문이 매우 귀찮음

def main():
    input = sys.stdin.readline
    M, S = map(int, input().split())
    f_delta = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    s_delta = [None, (-1, 0), (0, -1), (1, 0), (0, 1)]
    board = [[""] * 6] + [[""] + [0]*4 + [""] for _ in range(4)] + [[""] * 6]
    fish_pos = dict()
    for _ in range(M):
        fr, fc, d = map(int, input().split())
        if not (fr, fc) in fish_pos:
            fish_pos[(fr, fc)] = {d-1: 1}
        else:
            if d-1 in fish_pos[(fr, fc)]:
                fish_pos[(fr, fc)][d-1] += 1
            else:
                fish_pos[(fr, fc)][d-1] = 1
    sr, sc = map(int, input().split())

    for t in range(3, S+3):
        new_fish_pos = dict()
        # 1. 물고기 이동: 45도 반시계 돌면서 이동가능체크. 상어위치, 범위밖, 물고기냄새 칸에는 이동불가
        # 같은 칸에 물고기 중첩가능
        # 0←, 1↖, 2↑, 3↗, 4→, 5↘, 6↓, 7↙
        for pos, fish_d_cnt in fish_pos.items():
            fr, fc = pos
            for d in fish_d_cnt:
                for k in range(8, 0, -1):
                    nd = (d + k) % 8
                    nfr = fr + f_delta[nd][0]
                    nfc = fc + f_delta[nd][1]
                    # 범위 밖
                    if board[nfr][nfc] == "":
                        continue
                    # 상어 위치
                    if nfr == sr and nfc == sc:
                        continue
                    # 물고기 냄새
                    if t - board[nfr][nfc] < 3:
                        continue
                    if not (nfr, nfc) in new_fish_pos:
                        new_fish_pos[(nfr, nfc)] = {nd: fish_d_cnt[d]}
                    else:
                        if nd in new_fish_pos[(nfr, nfc)]:
                            new_fish_pos[(nfr, nfc)][nd] += fish_d_cnt[d]
                        else:
                            new_fish_pos[(nfr, nfc)][nd] = fish_d_cnt[d]
                    break
                else:
                    if not (fr, fc) in new_fish_pos:
                        new_fish_pos[pos] = {d: fish_d_cnt[d]}
                    else:
                        if d in new_fish_pos[pos]:
                            new_fish_pos[pos][d] += fish_d_cnt[d]
                        else:
                            new_fish_pos[pos][d] = fish_d_cnt[d]
        # print(t, "fish moved=========")
        # for pos, fish_d_cnt in new_fish_pos.items():
        #     for d, cnt in fish_d_cnt.items():
        #         if cnt > 0:
        #             print("pos:", pos, "fish:", d, "cnt:", cnt)
        # 0←, 1↖, 2↑, 3↗, 4→, 5↘, 6↓, 7↙
        # 2. 상어 연속 3칸이동. 상하좌우 이동가능. 범위밖 이동불가. 칸에 물고기 있으면 물고기 냄새 남기고 죽음.
        # 이동되어진 물고기 위치 기준으로 최대로 죽게끔 이동해야함. 여러가지인 경우 사전순 이동
        # (kill, 1move, 2move, 3move) 상좌하우 1234
        # print(t, "shark sr, sc", sr, sc)
        shark_pos = []
        for m1 in range(1, 5):
            k1 = 0
            m1r = sr + s_delta[m1][0]
            m1c = sc + s_delta[m1][1]
            if board[m1r][m1c] == "":
                continue
            if (m1r, m1c) in new_fish_pos:
                k1 += sum(new_fish_pos[(m1r, m1c)].values())
            for m2 in range(1, 5):
                k2 = k1
                m2r = m1r + s_delta[m2][0]
                m2c = m1c + s_delta[m2][1]
                if board[m2r][m2c] == "":
                    continue
                if (m2r, m2c) in new_fish_pos:
                    k2 += sum(new_fish_pos[(m2r, m2c)].values())
                for m3 in range(1, 5):
                    k3 = k2
                    m3r = m2r + s_delta[m3][0]
                    m3c = m2c + s_delta[m3][1]
                    if board[m3r][m3c] == "":
                        continue
                    if (m3r, m3c) in new_fish_pos and (m3r != m1r or m3c != m1c):
                        k3 += sum(new_fish_pos[(m3r, m3c)].values())
                    shark_pos.append((k3, m1, m2, m3))
        shark_pos.sort(key=lambda x: (-x[0], x[1], x[2], x[3]))
        # kill, m1, m2, m3 = shark_pos[0]
        # 최대 물고기 죽이기
        # print(t, "shark step", shark_pos[0])
        for m in range(1, 4):
            d = shark_pos[0][m]
            nsr = sr + s_delta[d][0]
            nsc = sc + s_delta[d][1]
            if (nsr, nsc) in new_fish_pos and (tmp:=sum(new_fish_pos[(nsr, nsc)].values())) > 0:
                new_fish_pos[(nsr, nsc)].clear()
                board[nsr][nsc] = t
                # print(tmp, "die", nsr, nsc, "time:", t)
            sr = nsr
            sc = nsc

        # 3. 2턴 전 생긴 물고기 냄새가 격자에서 사라진다. (현재 t와의 값 비교하면 됨.)
        # 4. 물고기 이동한 구간에 복제됨
        for pos, fish_d_cnt in new_fish_pos.items():
            if not pos in fish_pos:
                fish_pos[pos] = {}
            for d, cnt in fish_d_cnt.items():
                if d in fish_pos[pos]:
                    fish_pos[pos][d] += cnt
                else:
                    fish_pos[pos][d] = cnt
        # print(f"{t}, shark moved========= {sr} {sc}")
        # for pos, fish_d_cnt in fish_pos.items():
        #     for d, cnt in fish_d_cnt.items():
        #         if cnt > 0:
        #             print("pos:", pos, "fish:", d, "cnt:", cnt)

    ans = 0
    for pos, fish_d_cnt in fish_pos.items():
        for d, cnt in fish_d_cnt.items():
            ans += cnt

    print(ans)


if __name__ == '__main__':
    main()