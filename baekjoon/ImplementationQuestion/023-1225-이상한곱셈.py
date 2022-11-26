import sys

strA, strB = sys.stdin.readline().split()
total = 0
for a in strA:
    for b in strB:
        total += int(a) * int(b)

print(total)