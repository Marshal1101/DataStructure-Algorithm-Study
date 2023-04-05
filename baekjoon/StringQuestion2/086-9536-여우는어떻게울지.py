import sys; input = sys.stdin.readline

T = int(input())
for _ in range(T):
    rec = input().split()
    while (cry := input().split()[-1]) != "say?":
        rec = [word for word in rec if word != cry]
    print(*rec)