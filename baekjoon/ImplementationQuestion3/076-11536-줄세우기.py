def main():
    N = int(input())
    names = [input().rstrip() for _ in range(N)]
    inc = dec = False
    for i in range(1, N):
        if names[i] > names[i-1]:
            inc = True
        if names[i] < names[i-1]:
            dec = True
    
    if inc and dec:
        print("NEITHER")
    elif inc:
        print("INCREASING")
    else:
        print("DECREASING")


if __name__ == '__main__':
    main()