def main():
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    chk = 0
    for num in arr:
        if chk + 1 >= num:
            chk += num
        else:
            print(chk + 1)
            return

    print(chk + 1)


if __name__ == '__main__':
    main()