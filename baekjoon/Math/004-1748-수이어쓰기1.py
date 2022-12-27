import sys

N = sys.stdin.readline().rstrip()
arr = [i * (10**i - 10**(i-1)) for i in range(1, 9)]
for i in range(1, 8):
    arr[i] += arr[i-1]
arr = [0, 0] + arr
print(arr[len(N)] + len(N)*(int(N)+1 - 10**(len(N)-1)))