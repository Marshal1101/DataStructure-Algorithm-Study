hc = 0
for dd in map(int, input().split(":")):
    if 1 <= dd < 13:
        hc += 1
    elif dd >= 60:
        print(0)
        break
else:
    print(hc * 2)