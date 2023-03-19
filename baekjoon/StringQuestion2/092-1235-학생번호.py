import sys


def check(idx, N, nums, i_arr):
    end = len(nums[0])-1
    stk = [[] for _ in range(10)]
    for i in i_arr:
        num = nums[i][idx]
        stk[num].append(i)
    
    flag = True
    for s in stk:
        if len(s) > 1:
            ret = check(idx-1, N, nums, s)
            if end > ret:
                end = ret
                flag = False
    
    if flag:
        return idx

    return end


def main():
    input = sys.stdin.readline
    N = int(input())
    nums = [list(map(int, input().rstrip())) for _ in range(N)]
    idx = check(len(nums[0])-1, N, nums, list(range(N)))
    print(len(nums[0])-idx)


if __name__ == '__main__':
    main()
