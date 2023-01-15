import sys

input = sys.stdin.readline
N = int(input())

def moo(N, prev_moo, inter_zero):
    new_moo = prev_moo + inter_zero+1 + prev_moo
    if N <= new_moo:
        if N == 
    else:
        return moo(N, new_moo, inter_zero+1)

moo(N, 0, 3)