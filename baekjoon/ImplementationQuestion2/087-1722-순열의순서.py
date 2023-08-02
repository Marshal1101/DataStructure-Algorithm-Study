def serial(n, k):
    nums = [i for i in range(1, n+1)]
    step = 1
    for i in nums:
        step *= i
    idx = []
    while n > 0:
        step //= n
        for i in range(n-1, -1, -1):
            if k > i * step:
                idx.append(i)
                k -= i * step
                break
        n -= 1
    for i in idx:
        print(nums.pop(i), end=" ")
    print()


def order(n, idx):
    ret = 1
    nums = [i for i in range(1, n+1)]
    step = 1
    for i in nums:
        step *= i
    for i in idx:
        step //= n
        k = nums.index(i)
        ret += k * step
        nums.pop(k)
        n -= 1
    print(ret)



def main():
    N = int(input())
    query = list(map(int, input().split()))
    if query[0] == 1:
        serial(N, query[1])
    else:
        order(N, query[1:])


if __name__ == '__main__':
    main()