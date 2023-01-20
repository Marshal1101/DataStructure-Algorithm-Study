import sys


def conversion(M, nums: list, A, B):
    deci = 0
    for i in range(M-1):
        deci += nums[i] * A ** (M-i-1)
    deci += nums[-1]

    ans = []
    while deci > 0:
        n, r = divmod(deci, B)
        ans.append(r)
        deci = n
    return ans[::-1]

def main():
    input = sys.stdin.readline
    A, B = map(int, input().split())
    M = int(input())
    nums = list(map(int, input().split()))
    print(*conversion(M, nums, A, B))


if __name__ == '__main__':
    main()