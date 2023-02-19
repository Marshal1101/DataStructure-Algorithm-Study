import sys


def main():
    input = sys.stdin.readline
    N, T, P = map(int, input().split())
    arr = list(map(int, input().split()))
    if N == 0:
        print(1)
        return
    
    arr.sort(reverse=True)
    rank = 1
    flag = False
    i = 0
    while i < len(arr):
        if T > arr[i]:
            print(rank)
            return
        
        elif T == arr[i]:
            flag = True

        if not flag:
            rank += 1

        i += 1

    if i < P:
        print(rank)
    else:
        print(-1)


if __name__ == '__main__':
    main()