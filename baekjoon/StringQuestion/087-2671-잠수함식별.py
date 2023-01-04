import sys, re

def check(s):
    p = re.compile('^(100+1+|01)+$')
    if p.match(s): return True
    else: return False

s = sys.stdin.readline().rstrip()
if check(s): print("SUBMARINE")
else: print("NOISE")