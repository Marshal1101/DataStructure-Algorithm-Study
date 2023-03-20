import sys


def main():
    input = sys.stdin.readline
    flush = sys.stdout.flush
    write = sys.stdout.write
    N = int(input())   
    while True:
        write("? 1\n")
        flush()
        ans = input().rstrip()
        if ans == 'Y':
            write(f"! 1\n")
            flush()
            sys.exit(0)

if __name__ == '__main__':
    main()