import sys

N = int(sys.stdin.readline())
cards = [i for i in range(1, N+1)]
ans = []
while len(cards) > 1:
    ans.append(cards.pop(0))
    cards.append(cards.pop(0))

if cards: ans.append(cards.pop())
print(*ans)