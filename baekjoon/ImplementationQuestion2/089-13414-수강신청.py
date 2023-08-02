import sys


def main():
    input = sys.stdin.readline
    K, L = map(int, input().split())
    wait = dict()
    for i in range(1, L+1):
        sn = input().rstrip()
        wait[sn] = i

    print(*map(lambda x: x[0], sorted(list(wait.items()), key=lambda x: x[1])[:K]), sep='\n')


if __name__ == '__main__':
    main()
