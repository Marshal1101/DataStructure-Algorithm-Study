N = int(input())
arr = sorted(map(int, input().split()))
if N % 2: print(arr[N//2])
else: print(arr[N//2-1])

"""
index 0부터 시작
arr[ceil(N/2)-1]
아래와 같다.
if N % 2: print(arr[N//2])
else: print(arr[N//2-1])


index 1부터 시작
arr[ceil(N/2)]
아래와 같다.
if N % 2: print(arr[N//2+1])
else: print(arr[N//2])
"""