import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

"""
입력 > GCF
      ACDEB

각 숫자들을 더하여 최댓값을 만들기 위해선 높은 자릿 수의 값이 커야함
ACDEB
  GCF
=>  A > B > D,G > E,C > B,F 순

따라서 각 알파벳에 대해 자릿수 개념을 곱하여 계산하면, 해당 알파벳이 얼마 만큼의 영향을 끼치는지 알 수 있음
(10000A + 1000C + 100D + 10E + 1B) + (100G + 10C + 1B)
= 10000A + 1B + 1010C + 100D + 10E + 1F + 100G
=> A:9, C:8, (D:7, G:6), E:5, (B:4, F:3)

"""

def solution():
    for i in range(n):
        tmp = input().strip()
        for j in range(len(tmp)):
            alpha[ord(tmp[j]) - 65] += 10 ** (len(tmp) - j - 1)

    alpha.sort()

    ans = 0
    num = 9
    for i in range(25, -1, -1):
        if alpha[i] == 0:
            continue
        ans += alpha[i] * num
        num -= 1

    print(ans)


if __name__ == "__main__":
    n = int(input())
    alpha = [0 for _ in range(26)]
    solution()
