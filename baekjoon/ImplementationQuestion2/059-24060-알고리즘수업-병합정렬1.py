import sys


# A[p..r]을 오름차순 정렬한다.
def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)
        merge(arr, start, mid, end)

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
def merge(arr, start, mid, end):
    global cnt, tmp
    i = start
    j = mid + 1
    t = 0
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            tmp[t] = arr[i]
            t += 1
            i += 1
        else:
            tmp[t] = arr[j]
            t += 1
            j += 1
        cnt += 1
        if cnt == K:
            print(tmp[t-1])
            exit(0)
    
    # 왼쪽 배열 부분이 남은 경우
    while i <= mid:
        tmp[t] = arr[i]
        t += 1
        i += 1
        cnt += 1
        if cnt == K:
            print(tmp[t-1])
            exit(0)

    # 오른쪽 배열 부분이 남은 경우
    while j <= end:
        tmp[t] = arr[j]
        t += 1
        j += 1
        cnt += 1
        if cnt == K:
            print(tmp[t-1])
            exit(0)

    i = start
    t = 0

    # 결과를 A[p..r]에 저장
    while i <= end:
        arr[i] = tmp[t]
        i += 1
        t += 1
        

def main():
    input = sys.stdin.readline
    global cnt, K, tmp
    cnt = 0
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    tmp = [0] * N
    merge_sort(arr, 0, N-1)
    print(-1)


if __name__ == '__main__':
    main()