N, M = map(int, input().split())
minus = []
plus = []
for v in map(int, input().split()):
    if v < 0: minus.append(v)
    else: plus.append(v)
ans = 0
last = 0
if minus:
    minus.sort()
    # print(f"minus: {minus}")
    for i in range(0, len(minus), M):
        ans += -minus[i] * 2
if plus:
    plus.sort(reverse=True)
    # print(f"plus: {plus}")
    for i in range(0, len(plus), M):
        ans += plus[i] * 2

if not minus:
    ans -= plus[0]
elif not plus:
    ans -= -minus[0]
else:
    if -minus[0] > plus[0]:
        ans -= -minus[0]
    else:
        ans -= plus[0]

print(ans)