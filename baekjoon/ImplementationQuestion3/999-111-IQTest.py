def trie(idx, a, b, nums, ans):
    if idx == len(nums) - 1:
        ans.append(nums[idx] * a + b)
        return
    
    if nums[idx+1] == nums[idx] * a + b:
        trie(idx+1, a, b, nums, ans)


def main():
    N = int(input())
    nums = list(map(int, input().split()))
    ans = []

    if N == 1:
        print("A")

    elif N == 2:
        p1 = nums[0]
        p2 = nums[1]
        if p1 == p2:
            print(p2)
        else:
            print("A")
    else:
        p1 = nums[0]
        p2 = nums[1]
        p3 = nums[2]
        if p2 - p1 != 0:
            if (p2**2 - p1*p3) % (p2 - p1) == 0:
                b = (p2**2 - p1*p3) // (p2 - p1)
                if p2 - b == 0:
                    if p1 == 0:
                        trie(1, 1, b, nums, ans)
                    else:
                        trie(1, 0, b, nums, ans)
                    if len(ans):
                        print(*ans)
                        return
                elif p1 != 0 and (p2 - b) % p1 == 0:
                    a = (p2 - b) // p1
                    trie(1, a, b, nums, ans)
                    if len(ans):
                        print(*ans)
                        return
        elif p3 == p2:
            trie(1, 0, p3, nums, ans)
            if len(ans):
                print(*ans)
                return
        
        print("B")


if __name__ == '__main__':
    main()