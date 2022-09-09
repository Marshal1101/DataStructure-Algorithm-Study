import sys; input = sys.stdin.readline

def GCD(a, b):
    while b > 0:
        tmp = a % b
        a = b
        b = tmp
    return a

T = int(input())
ret = []
for i in range(T):
    total = 0
    arr = list(map(int, input().split()))
    for j in range(1, arr[0]+1):
        for k in range(1, j):
            total += GCD(arr[k], arr[j])
    ret.append(total)

for r in ret:
    print(r)