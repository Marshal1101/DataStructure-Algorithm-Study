is_home_win = False
is_away_win = False
hp = ap = 0
for h, a in zip(list(map(int, input().split())), list(map(int, input().split()))):
    hp += h
    if hp > ap:
        is_home_win = True
        is_away_win = False
    ap += a
    if ap > hp:
        is_away_win = True

if is_home_win and is_away_win:
    print("Yes")
else:
    print("No")