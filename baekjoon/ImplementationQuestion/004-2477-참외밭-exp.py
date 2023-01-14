# https://www.acmicpc.net/source/53949889

n = int(input())
arr = [0,0,0,0,0,0]
for i in range(6) :
    temp, arr[i] = map(int,input().split())
x = arr.index(max(arr))
if arr[(x + 1) % 6] < arr[(x + 5) % 6] :
    y = (x + 5) % 6
    sx = (x + 2) % 6
    sy = (x + 3) % 6
else :
    y = (x + 1) % 6
    sx = (x + 4) % 6
    sy = (x + 3) % 6

print(n * (arr[x] * arr[y] - arr[sx] * arr[sy]))