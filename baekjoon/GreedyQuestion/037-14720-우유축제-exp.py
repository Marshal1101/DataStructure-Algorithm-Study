input()
c = 0
for n in list(map(int, input().split())):
    c += c % 3 == n
print(c)
