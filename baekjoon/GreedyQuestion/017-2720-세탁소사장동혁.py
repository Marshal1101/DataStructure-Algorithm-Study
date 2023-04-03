import sys

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        c = int(input())
        coin = [25, 10, 5, 1]
        cnt = [0, 0, 0, 0]
        i = 0
        while i < 4:
            cnt[i] += c // coin[i]
            c = c % coin[i]
            i += 1
        print(*cnt)

if __name__ == '__main__':
    main()