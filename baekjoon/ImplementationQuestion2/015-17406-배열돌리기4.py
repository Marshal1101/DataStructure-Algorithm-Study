import sys
from itertools import permutations


def rotate(v1, v2, arr):
    # print(f"rotate: v1={v1}, v2={v2}")
    # for a in arr:
        # print(a)
    for k in range((v2[0]-v1[0]+1)//2):
        # 회전 양끝
        r1, c1 = v1[0]+k, v1[1]+k
        r2, c2 = v2[0]-k, v2[1]-k

        print(f"k={k}, v1={r1, c1}, v2={r2, c2}")
        # 우측이동
        r1c2 = arr[r1][c2]
        for j in range(c2, c1, -1):
            arr[r1][j] = arr[r1][j-1]

        # 아래이동
        r2c2 = arr[r2][c2]
        for i in range(r2, r1+1, -1):
            arr[i][c2] = arr[i-1][c2]
        arr[r1+1][c2] = r1c2

        # 좌측이동
        r2c1 = arr[r2][c1]
        for j in range(c1, c2-1):
            arr[r2][j] = arr[r2][j+1]
        arr[r2][c2-1] = r2c2

        # 위로이동
        for i in range(r1, r2-1):
            arr[i][c1] = arr[i+1][c1]
        arr[r2-1][c1] = r2c1

        # for a in arr:
        #         print(a)

def get_arr_val(N, M, arr):
    total = 5001
    for i in range(N):
        total = tmp  if (tmp:=sum(arr[i])) < total else total
    return total

def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # for a in arr:
    #     print(a)
    rot_case = [tuple(map(int, input().split())) for _ in range(K)]

    min_ans = 250001
    for order in permutations(range(K), K):
        # print("=========order:", order)
        copy_arr= [a[:] for a in arr]
        for i in order:
            r, c, s = rot_case[i]
            v1 = (r-1-s, c-1-s)
            v2 = (r-1+s, c-1+s)
            rotate(v1, v2, copy_arr)

        ans = get_arr_val(N, M, copy_arr)
        if ans < min_ans: min_ans = ans

    print(min_ans)

if __name__ == '__main__':
    main()