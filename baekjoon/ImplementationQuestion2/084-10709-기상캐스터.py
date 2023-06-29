import sys


def main():
    input = sys.stdin.readline
    H, W = map(int, input().split())
    for _ in range(H):
        prev = -1
        for sky in input().rstrip():
            if sky == 'c':
                print(0, end=" ")
                prev = 0
            elif prev != -1:
                prev += 1
                print(prev, end=" ")
            else:
                print(-1, end=" ")
                prev = -1
        print()
    

if __name__ == '__main__':
    main()