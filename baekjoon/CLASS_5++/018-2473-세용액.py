import sys
from bisect import bisect_left


def main() :
    input = sys.stdin.readline

    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    lp = 0
    rp = N - 1
    num1 = 0
    num2 = 0
    num3 = 0
    min_gap = sys.maxsize
    while lp + 1 < rp :
        lr = arr[lp] + arr[rp]
        p = bisect_left(arr[lp+1:rp], -lr)
        ep = rp - lp
        if 0 < p < ep - 1 :
            temp1 = lr + arr[(mp := lp + p)]
            temp2 = lr + arr[(mp := lp+1 + p)]
            s = temp1 if abs(temp1) < abs(temp2) else temp2 
        else :
            s = lr + arr[(mp := lp + 1)]

        if abs(s) < min_gap :
            min_gap = s
            num1 = arr[lp]
            num2 = arr[rp]
            num3 = arr[mp]
        if s > 0 :
            rp -= 1
        elif (s == 0) :
            return (arr[lp], arr[mp], arr[rp])
        else :
            lp += 1

    return (num1, num3, num2)

if __name__ == '__main__' :
    print(*main())