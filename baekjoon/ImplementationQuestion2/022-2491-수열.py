N = int(input())
nums = list(map(int, input().split()))
ans = 0

if N == 1:
    print(1)

else:
    cnt = 2
    if nums[1] > nums[0]:
        opt = 1
    elif nums[1] < nums[0]:
        opt = -1
    else:
        opt = 0

    same = 0
    prev = nums[1]
    for i in range(2, N):
        if nums[i] > prev:
            if opt != -1:
                cnt += 1
            else:
                if cnt > ans:
                    ans = cnt
                cnt = 2 + same
            opt = 1
            same = 0

        elif nums[i] < prev:
            if opt != 1:
                cnt += 1
            else:
                if cnt > ans:
                    ans = cnt
                cnt = 2 + same
            opt = -1
            same = 0
        
        else:
            same += 1
            cnt += 1
        
        prev = nums[i]

    print(max(cnt, ans))