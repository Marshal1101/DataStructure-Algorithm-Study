import sys
input = sys.stdin.readline


def bsearch(N, M, arr):
    ans  = arr[-1]
    tleft = arr[0]
    tright = arr[-1]
    while tleft <= tright:
        ttmax = 0
        prev_end = 0
        d = (tleft + tright) // 2
        now = arr[0]
        count = 1
        for i in range(1, N+1):
            if (tt := arr[i] - now) <= d:
                prev_end = i
                if tt > ttmax: ttmax = tt
                
            else:
                count += 1
                now = arr[prev_end]
                if (tt := arr[i] - now) <= d:
                    prev_end = i
                    if tt > ttmax: ttmax = tt
                else:
                    count = M + 1
                    break

        if count <= M:
            if ttmax < ans:
                ans = ttmax
            tright = d - 1
        else:
            tleft = d + 1

    return ans


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    for i in range(1, N+1):
        arr[i] += arr[i-1]
    
    print(bsearch(N, M, arr))

if __name__ == '__main__':
    main()
