import sys


def main():
    input = sys.stdin.readline
    total = 0
    all_point = 0
    for i in range(20):
        sub, point, grade = input().split()
        if grade[0] == "P":
            continue
        tot = 0
        for c in grade:
            if c == "+":
                tot += 0.5
            elif c == "A":
                tot += 4
            elif c == "B":
                tot += 3
            elif c == "C":
                tot += 2
            elif c == "D":
                tot += 1
        total += tot * float(point)
        all_point += float(point)

    print(round((total / all_point), 6))


if __name__ == "__main__":
    main()