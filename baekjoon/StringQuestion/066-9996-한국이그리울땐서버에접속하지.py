import sys, re; input = sys.stdin.readline

N = int(input())
prefix, suffix = input().rstrip().split("*")
reg = re.compile(f'^{prefix}[a-z]*{suffix}$')
for _ in range(N):
    if reg.match(input().rstrip()): print("DA")
    else: print("NE")