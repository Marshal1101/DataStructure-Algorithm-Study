def main():
    N, K = map(int, input().split())
    if K >= N:
        print(-1)
        return
    
    basic = K*(K+1)//2
    rest = N - basic
    if rest < 0:
        print(-1)
        return
    basic_plus = rest // K
    mn = 1 + basic_plus
    mx = K + basic_plus
    if rest % K > 0:
        mx += 1
    
    print(mx-mn)


if __name__ == '__main__':
    main()