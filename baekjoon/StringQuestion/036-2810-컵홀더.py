import sys

input = sys.stdin.readline
N = int(input())
cnt = 0
prev = "S"
hand = "L"
for cur in input().rstrip():
    if hand == "L":
        if prev == "S":
            cnt += 1
            prev = cur
        elif prev == "L":
            cnt += 1
            prev = ""
            hand = "R"
    else:
        if prev == "" or prev == "S":
            if cur == "S":
                cnt += 1
            prev = cur
        elif prev == "L":
            cnt += 1
            prev = ""

print(cnt)