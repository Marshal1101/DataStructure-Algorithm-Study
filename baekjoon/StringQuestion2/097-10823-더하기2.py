import sys


ans = 0
line = sys.stdin.read().replace("\n", "").split(",")
for word in line:
    if word != '':
        ans += int(word)

print(ans)