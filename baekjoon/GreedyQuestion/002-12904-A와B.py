import sys


input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

N = len(T)
sb = 0
tb = 0
for s in S:
    if s == "A":
        sb = (sb << 1) + 1
    else:
        sb = sb << 1
    print(s, format(sb, 'b'))
print(S)
print(format(sb, 'b'))
print("==========")
for t in T:
    if t == "A":
        tb = (tb << 1) + 1
    else:
        tb = tb << 1
    print(t, format(tb, 'b'))
print(T)
print(format(tb, 'b'))

def flip(sb, tb, N):
    if sb > tb: return

    