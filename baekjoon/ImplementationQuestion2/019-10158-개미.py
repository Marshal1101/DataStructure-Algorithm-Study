import sys


input = sys.stdin.readline
W, H = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

refl_p, pos_p = divmod(t+p, W)
refl_q, pos_q = divmod(t+q, H)

if refl_p % 2 != 0:
    pos_p = W - pos_p

if refl_q % 2 != 0:
    pos_q = H - pos_q

print(pos_p, pos_q)