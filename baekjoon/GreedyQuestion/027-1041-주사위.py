N = int(input())
arr = [*map(int, input().split())]
top = arr[0] if arr[0] < arr[5] else arr[5]

if N == 1:
    print(sum(arr) - max(arr))
    exit()

side = min(arr[1]+arr[2], arr[2]+arr[4], arr[4]+arr[3], arr[3]+arr[1]) 
min_s = 1e6+1
for i in range(1, 5):
    if arr[i] < min_s:
        min_s = arr[i]

if top <= min_s:
    one = top
    two = top + min_s
else:
    one = min_s
    two = side if side < top + min_s else top + min_s
three = top + side


total = 4*(N-1)**2 + N**2 
block3 = 4
block2 = (N-1) * 4 + (N-2) * 4
block1 = total - block3 - block2
ans = block3 * three + block2 * two + block1 * one
print(ans)