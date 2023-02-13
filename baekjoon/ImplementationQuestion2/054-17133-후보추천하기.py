import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    R = int(input())
    vote = list(map(int, input().split()))
    rec = dict()
    for k in range(R):
        n = vote[k]

        if n in rec:
            rec[n][0] += 1
        else:
            if len(rec) < N:
                rec[n] = [1, k]
            else:
                key, value = sorted(rec.items(), key=lambda x: x[1])[0]
                del rec[key]
                rec[n] = [1, k]

    for key in sorted(rec.keys()):
        print(key, end=" ")


if __name__ == '__main__':
    main()