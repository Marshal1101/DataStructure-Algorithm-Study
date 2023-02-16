import sys


# A[p..r]을 오름차순 정렬한다.
def merge_sort(arr, tar, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, tar, start, mid)
        merge_sort(arr, tar, mid+1, end)
        merge(arr, tar, start, mid, end)

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
def merge(arr, tar, start, mid, end):
    global tmp, tp
    i = start
    j = mid + 1
    t = 0
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            tmp[t] = arr[i]
            i += 1
        else:
            tmp[t] = arr[j]
            j += 1
        t += 1


    # 왼쪽 배열 부분이 남은 경우
    while i <= mid:
        tmp[t] = arr[i]
        t += 1
        i += 1


    # 오른쪽 배열 부분이 남은 경우
    while j <= end:
        tmp[t] = arr[j]
        t += 1
        j += 1


    k = start
    t = 0
    # 결과를 A[p..r]에 저장
    while k <= end:
        arr[k] = tmp[t]
        while arr[tp] == tar[tp]:
            tp += 1
            if tp == N:
                print(1)
                exit(0)
        k += 1
        t += 1



def main():
    input = sys.stdin.readline
    global tmp, tp, N
    N = int(input())
    tp = 0
    arr = list(map(int, input().split()))
    tar = list(map(int, input().split()))
    
    if arr == tar:
        print(1)
        exit(0)

    tmp = [0] * N
    merge_sort(arr, tar, 0, N-1)
    print(0)


if __name__ == '__main__':
    main()