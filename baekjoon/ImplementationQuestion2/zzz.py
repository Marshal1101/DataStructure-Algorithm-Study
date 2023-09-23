a = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# b = zip(a)
for b in zip(*a):
    b = list(b)
    b.reverse()
    print(b)