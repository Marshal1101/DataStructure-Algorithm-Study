import sys
from itertools import combinations

input = sys.stdin.readline

while (pot := input().split())[0] != "0":
    N = pot.pop(0)
    for case in combinations(pot, 6):
        print(*case)
    print()