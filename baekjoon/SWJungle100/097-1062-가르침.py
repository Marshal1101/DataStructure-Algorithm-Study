import sys
from itertools import combinations


def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())

    basic = set(["a", "n", "t", "i", "c"])
    P = K - 5

    if P < 0:
        print(0)
        return

    words = []
    new_char = set()
    for k in range(N):
        word = input().rstrip()
        s = set()
        learn = 0
        for i in range(4, len(word)-4):
            if not word[i] in basic and not word[i] in s:
                s.add(word[i])
                learn += 1

        if learn <= P:
            words.append(s)
            new_char.update(s)

    if len(words) == 0:
        print(0)
        return

    if len(new_char) <= P:
        print(len(words))
        return

    max_cnt = 0
    for case in combinations(list(new_char), P):
        cnt = 0
        s_case = set(case)
        for word in words:
            if len(word - s_case) == 0:
                cnt += 1

        if cnt > max_cnt:
            max_cnt = cnt

    print(max_cnt)


if __name__ == "__main__":
    main()