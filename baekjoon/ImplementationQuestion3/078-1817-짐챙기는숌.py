def main():
    N, M = map(int, input().split())
    ans = 0
    box = 0
    if N == 0:
        print(0)
        return
    
    for book in map(int, input().split()):
        box += book
        if box > M:
            ans += 1
            box = book

    print(ans+1)

if __name__ == '__main__':
    main()