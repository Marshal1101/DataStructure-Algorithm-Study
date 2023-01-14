import sys


def check(p1: tuple, p2: tuple, N, nums):
    i1, j1 = p1
    i1, j2 = p2
    d = j2 - j1
    if (i2 := i1 + d) < N and nums[i2][j1] == nums[i2][j2] == nums[i1][j1]:
        # print(f"{nums[i1][j1]} {nums[i1][j2]} {nums[i2][j2]} {nums[i2][j1]}")
        # print(p1, (i1, j2), p2, (i2, j1))
        return d + 1
    else:
        return 0

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    nums = [list(map(int, input().rstrip())) for _ in range(N)]
    max_size = 1
    for i in range(N-1):
        if N - i < max_size: break
        chk = set()
        for j in range(M):
            if nums[i][j] in chk:
                for k in range(j):
                    if nums[i][k] == nums[i][j] \
                        and j - k < N \
                        and max_size < j - k + 1 \
                        and (tmp := check((i, k), (i, j), N, nums)):
                            max_size = tmp
            chk.add(nums[i][j])

    print(max_size**2)


if __name__ == '__main__':
    main()