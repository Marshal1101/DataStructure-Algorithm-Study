N = int(input())
arr = sorted(map(int, input().split()), reverse=True)

dday = 1
for i in range(N):
    if i + arr[i] > dday:
        dday = i + arr[i]
print(dday+2)