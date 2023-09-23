import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    arr = sorted([int(input()) for _ in range(N)])
    seqlen = 5
    ans = 4
    for i in range(N):
        cnt = 1
        for j in range(i+1, i+seqlen):
            if j >= N:
                break
            if arr[j] < arr[i] + 5:
                cnt += 1
            else:
                break
        if seqlen - cnt < ans:
            ans = seqlen - cnt

    print(ans)



if __name__ == '__main__':
    main()