import sys


cons = [
    'q', 'w', 'e', 'r', 't',
    'a', 's', 'd', 'f', 'g',
    'z', 'x', 'c', 'v'
    ]

input = sys.stdin.readline
N = int(input())
if input().rstrip()[-1] in cons:
    print(1)
else:
    print(0)
