import sys; input = sys.stdin.readline


def cal(K, arr):
    ret = 0
    arr.sort(reverse=True)
    seat = K
    i = 0
    while i < len(arr):
        if seat == K:
            a = arr[i][1] // seat
            b = arr[i][1] % seat
            r = 1 if b > 0 else 0
            ret += 2 * arr[i][0] * (a + r)
            seat = K - b
            i += 1
        else:
            if seat - arr[i][1] > 0:
                seat -= arr[i][1]
                i += 1
            elif seat - arr[i][1] == 0:
                seat = K
                i += 1
            else:
                arr[i][1] -= seat
                seat = K
    return ret


N, K, S = map(int, input().split())
left = []
right = []
for _ in range(N):
    p, v = map(int, input().split())
    if p < S:
        left.append([S-p, v])
    else:
        right.append([p-S, v])

ans = 0
if left: ans += cal(K, left)
if right: ans += cal(K, right)
print(ans)