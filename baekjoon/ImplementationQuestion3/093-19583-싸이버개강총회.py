import sys


# def time_to_num(time: str) -> int:
#     hh, mm = time.split(":")
#     return int(hh)*100 + int(mm)

# def main():
#     input = sys.stdin.readline
#     S, E, Q = map(time_to_num, input().split())
#     attendant = set()
#     ans = 0
#     while (line := input()) != "":
#         time, id = line.split()
#         hm = time_to_num(time)
#         if hm <= S:
#             attendant.add(id)
#         if E <= hm <= Q and id in attendant:
#             attendant.remove(id)
#             ans += 1

#     print(ans)

def main():
    input = sys.stdin.readline
    S, E, Q = input().split()
    attendant = set()
    ans = 0
    while (line := input()) != "":
        time, id = line.split()
        if time <= S:
            attendant.add(id)
        if E <= time <= Q and id in attendant:
            attendant.remove(id)
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()