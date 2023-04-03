import sys


def main():
    arr = list(map(int, sys.stdin.readlines()))
    cur = arr[-1]
    ans = 0
    for i in range(len(arr)-2, 0, -1):
        if arr[i] >= cur:
            ans += arr[i] - cur + 1
            cur = cur - 1
        else:
            cur = arr[i]

    print(ans)


if __name__ == '__main__':
    main()