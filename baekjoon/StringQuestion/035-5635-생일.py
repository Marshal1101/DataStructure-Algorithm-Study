import sys


input = sys.stdin.readline
N = int(input())

map = dict()
birthList = list()
for _ in range(N):
    name, day, month, year = input().split()
    day = day.zfill(2)
    print("day:", day)
    month = month.zfill(2)
    print("month:", month)
    birthday = int(year + month + day)
    birthList.append(birthday)
    map[birthday] = name

birthList.sort()
print(map[birthList[len(birthList)-1]])
print(map[birthList[0]])