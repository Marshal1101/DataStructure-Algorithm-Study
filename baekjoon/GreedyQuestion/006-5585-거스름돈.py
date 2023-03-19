price = 1000 - int(input())
change = [500, 100, 50, 10, 5, 1]
ans = i = 0
while price != 0:
    if price >= change[i]:
        price -= change[i]
        ans += 1
    else:
        i += 1

print(ans)